# Access Control Labs

**13 / 13 labs completed** — June 9-20, 2026

---

## Lab Completion Record

| # | Lab | Difficulty | Vulnerability |
|---|---|---|---|
| 1 | Unprotected admin functionality | Apprentice | Vertical privilege escalation via robots.txt disclosure |
| 2 | Unprotected admin functionality with unpredictable URL | Apprentice | Information disclosure via JavaScript in page source |
| 3 | User role controlled by request parameter | Apprentice | Cookie-based role forgery |
| 4 | User role can be modified in user profile | Apprentice | Mass assignment via JSON parameter injection |
| 5 | URL-based access control can be circumvented | Practitioner | X-Original-URL header bypass |
| 6 | Method-based access control can be circumvented | Practitioner | HTTP method bypass (POSTX non-standard method) |
| 7 | User ID controlled by request parameter | Apprentice | Horizontal privilege escalation via IDOR |
| 8 | User ID controlled by request parameter, with unpredictable user IDs | Apprentice | IDOR with GUID-based user IDs exposed in blog posts |
| 9 | User ID controlled by request parameter with data leakage in redirect | Apprentice | Sensitive data exposed in redirect response body |
| 10 | User ID controlled by request parameter with password disclosure | Apprentice | Horizontal to vertical privilege escalation - password disclosed in profile HTML |
| 11 | Insecure direct object references | Apprentice | IDOR via incrementing filename on static chat transcripts |
| 12 | Multi-step process with no access control on one step | Practitioner | Access control missing on confirmation step of multi-step flow |
| 13 | Referer-based access control | Practitioner | Access control bypass via forged Referer header |

---

## Key Techniques Practiced

- Browsing to unprotected admin endpoints disclosed via `robots.txt` and JavaScript source
- Forging role-based cookies (`Admin=false` → `Admin=true`)
- JSON parameter injection to mass-assign privileged roles (`roleid: 2`)
- Bypassing URL-based access controls using `X-Original-URL` header
- Bypassing HTTP method restrictions using non-standard methods (POSTX)
- Horizontal privilege escalation via predictable and GUID-based user IDs
- Extracting sensitive data from redirect response bodies
- Escalating horizontal to vertical privilege by targeting admin accounts via IDOR
- IDOR via incrementing filenames on server-side static files
- Skipping access-controlled steps in multi-step processes
- Forging `Referer` headers to bypass sub-page access controls

---

## Notes

Full concepts, techniques, and prevention methods:
[Web-Security / Access Control](https://github.com/faisalulde/web-security/blob/main/Access-Control/access-control.md)
