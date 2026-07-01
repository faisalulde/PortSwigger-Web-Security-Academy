# Authentication Labs

**14 / 14 labs completed** — May 9-June 2, 2026

---

## Lab Completion Record

| # | Lab | Difficulty | Vulnerability | Key Technique |
|---|---|---|---|---|
| 1 | Username enumeration via different responses | Apprentice | Username enumeration | Grep-Match on distinct error message; Burp Intruder Sniper |
| 2 | Username enumeration via subtly different responses | Practitioner | Username enumeration | Grep-Match on full error string including trailing full stop |
| 3 | Username enumeration via response timing | Practitioner | Username enumeration + rate limit bypass | X-Forwarded-For header rotation; Pitchfork attack; long password to amplify timing difference |
| 4 | Broken brute-force protection, IP block | Practitioner | Brute-force protection bypass | Python script interleaving valid credentials every 3rd attempt to reset lockout counter |
| 5 | Username enumeration via account lock | Practitioner | Username enumeration | Cluster Bomb with Null Payloads to trigger lockout on valid username only |
| 6 | Broken brute-force protection, multiple credentials per request | Expert | Brute-force protection bypass | JSON array injection - passing full password list as array value in single request |
| 7 | 2FA simple bypass | Apprentice | 2FA bypass | Direct navigation to authenticated endpoint after first login step; skipping /login2 entirely |
| 8 | 2FA broken logic | Practitioner | 2FA broken logic | Forged `verify` cookie to target victim; brute-forced 4-digit MFA code (Python multithreaded script) |
| 9 | 2FA bypass using a brute-force attack | Expert | 2FA bypass | Full session rotation with CSRF token extraction per attempt (Python + BeautifulSoup); Burp macros |
| 10 | Brute-forcing a stay-logged-in cookie | Practitioner | Insecure credential storage | Decoded Base64 cookie → identified MD5 hash → generated wordlist via Python; Burp Payload Processing |
| 11 | Offline password cracking | Practitioner | Stored XSS + insecure credential storage | Stored XSS payload to exfiltrate stay-logged-in cookie via exploit server; decoded Base64/MD5 chain |
| 12 | Password reset broken logic | Apprentice | Broken password reset | Token not validated on form submission - blanked token in body while targeting different username |
| 13 | Password reset poisoning via middleware | Practitioner | Header injection | X-Forwarded-Host injection redirected reset link to attacker-controlled server; stolen token used to reset victim password |
| 14 | Password brute-force via password change | Practitioner | Brute-force via error message differences | Change-password endpoint reflected different errors for correct vs incorrect current password; bypassed lockout by mismatching new passwords |

---

## Scripts

Python exploit scripts written during these labs are in the [scripts folder](scripts/):

| Script | Lab |
|---|---|
| [ip-block-bypass.py](scripts/ip-block-bypass.py) | Lab 4 - Broken brute-force protection, IP block |
| [array-injection.py](scripts/array-injection.py) | Lab 6 - Multiple credentials per request |
| [mfa-bruteforcer.py](scripts/mfa-bruteforcer.py) | Lab 8 - 2FA broken logic |
| [mfa-session-rotation.py](scripts/mfa-session-rotation.py) | Lab 9 - 2FA bypass using brute-force attack |
| [stayloggedin-cookie-gen.py](scripts/stayloggedin-cookie-gen.py) | Lab 10 - Brute-forcing a stay-logged-in cookie |

---

## Key Techniques Practiced

- Username enumeration via distinct and subtly different error messages
- Response timing analysis to identify valid usernames under generic error messages
- X-Forwarded-For header spoofing to bypass IP-based rate limiting
- Interleaved credential injection to bypass account lockout (Python scripted)
- Cluster Bomb with Null Payloads to trigger account lockout on valid usernames
- JSON array injection to test multiple passwords in a single request
- 2FA bypass via direct endpoint navigation (skipping the MFA step entirely)
- 2FA broken logic exploitation via forged account cookie + MFA brute-force
- Full session rotation with automated CSRF extraction for 2FA brute-force
- Stay-logged-in cookie decoding and brute-force via Base64/MD5 reversal
- Stored XSS cookie exfiltration via exploit server
- Password reset token manipulation (blank token + arbitrary username)
- X-Forwarded-Host header injection to redirect password reset links
- Error message differencing to brute-force passwords via the change-password endpoint

---

## Notes

Full concepts, techniques, and prevention methods:
[Web-Security / Authentication](https://github.com/faisalulde/web-security/blob/main/Authentication/authentication.md)
