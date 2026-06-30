# PortSwigger Web Security Academy

Completed labs, progress tracking, and exploit scripts from [PortSwigger Web Security Academy](https://portswigger.net/web-security).

Notes and concepts are maintained separately in [Web-Security](https://github.com/faisalulde/Web-Security).

---

## Progress

| Topic | Status | Labs |
|---|---|---|
| SQL Injection | Complete | 18 / 18 |
| Authentication | Complete | 14 / 14 |
| Access Control | Complete | 13 / 13 |
| Business Logic | In Progress | - |

---

## Scripts

Python scripts written during Authentication labs to automate exploitation techniques.

| Script | Lab | Technique |
|---|---|---|
| [ip-block-bypass.py](authentication/scripts/ip-block-bypass.py) | Broken brute-force protection, IP block | Generates interleaved wordlists injecting valid credentials every 3rd attempt to reset the lockout counter |
| [array-injection.py](authentication/scripts/array-injection.py) | Multiple credentials per request | Converts a password wordlist to JSON array format for bypassing brute-force protection via array injection |
| [mfa-bruteforcer.py](authentication/scripts/mfa-bruteforcer.py) | 2FA broken logic | Multithreaded MFA code brute-forcer using 10 concurrent threads |
| [mfa-session-rotation.py](authentication/scripts/mfa-session-rotation.py) | 2FA bypass using brute-force attack | Full session rotation MFA brute-forcer — extracts CSRF tokens via BeautifulSoup and rotates sessions every 2 attempts |
| [stayloggedin-cookie-gen.py](authentication/scripts/stayloggedin-cookie-gen.py) | Brute-forcing a stay-logged-in cookie | Generates Base64(username:MD5(password)) encoded wordlist for stay-logged-in cookie attacks |

---

## Tools Used

- Burp Suite
- Python - requests, threading, BeautifulSoup, hashlib, base64, json
- Kali Linux

---

## Related

- [Web-Security](https://github.com/faisalulde/Web-Security) - concepts, techniques, and payloads by topic
- [security-writeups](https://github.com/faisalulde/security-writeups) - CTF writeups applying these techniques

---

## Connect

- [LinkedIn](https://linkedin.com/in/faisal-ulde)
- [GitHub](https://github.com/faisalulde)
