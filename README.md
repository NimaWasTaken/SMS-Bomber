<div align="center">
  <h1>💣 SMS Bomber 💣</h1>
</div>
<div align="center">
  <p>A freely available and open-source SMS bombing application tailored for use in Iran.</p>
</div>

## 📌 Notice
**Important information before using the SMS Bomber:**

1. **Active Internet Connection:** Ensure that your device has an active internet connection to contact the required APIs.

2. **No Charges for SMS:** You will not be charged for any SMS dispatched as a consequence of using this script.

3. **Python 3 and Latest Version:** Always ensure that you are using the latest version of the SMS Bomber and have Python 3 installed on your system.

4. **No Harmful Use:** This application must not be used to cause harm, discomfort, or trouble to others. Respect the privacy and well-being of individuals.

## ✅ Installation
Clone the github repo
```bash
$ git clone https://github.com/NimaWasTaken/SMS-Bomber.git
```
Change Directory
```bash
$ cd SMS-Bomber
```

Use the package manager [pip](https://pip.pypa.io/en/stable/getting-started/) to install the requirements.
```bash
$ pip install -r requirements.txt
```

## ❓ Usage
To use the SMS bombing tool, you can run the `main.py` script with the appropriate command-line arguments. Here's an overview of the available options:

```bash
usage: main.py target [-h] [-c COUNT] [-t THREADS] [-v] [-x PROXY]

\033[1;36mSMS Bombing Tool\033[0m

\033[1mpositional arguments:\033[0m
  \033[93mtarget\033[0m                         The target phone number (format: 09xxxxxxxxx)

\033[1moptional arguments:\033[0m
  \033[93m-h, --help\033[0m                     show this help message and exit
  \033[93m-c COUNT, --count COUNT\033[0m        Number of times to bomb the target phone number (default is 1)
  \033[93m-t THREADS, --threads THREADS\033[0m  Number of concurrent threads to use for bombing (default is 5)
  \033[93m-v, --verbose\033[0m                  Display additional information during the bombing process
  \033[93m-x PROXY, --proxy PROXY\033[0m        Set a proxy server for requests (http/https)
```
### Example Usage
To bomb a phone number with default settings:
```bash
$ python main.py 09123456789
```
To specify the number of bombing times and threads:
```bash
$ python main.py 09123456789 -c 10 -t 3
```
To enable verbose mode and set a proxy server:
```bash
$ python main.py 09123456789 -v -x http://proxy.example.com:8080
```
