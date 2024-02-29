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
### Options
- `-h, --help`: Show help message and exit.
- `-t TARGET, --target TARGET`: Specify the target phone number.
- `-n TIMES, --times TIMES`: Specify the number of bombing times, default is 1.
- `--process PROCESS`: Specify the number of processes, default is 5.
- `-v, --verbose`: Display additional info.
- `-x PROXY, --proxy PROXY`: Set the proxy for requests (http/https).
### Example
```bash
$ python bomber.py -t 09xxxxxxxxx -n 5 --process 3 -v --proxy http://your-proxy-url:port
```
