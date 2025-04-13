## 🔁 Automation Workflows Covered

- ✅ Login with valid credentials
- ✅ Navigate to PIM module
- ✅ Add 3 employees
- ✅ Verify employees are present in the Employee List
- ✅ Log out after test
- ✅ Desktop notification on successful verification (Win10Toast)

## 🧪 Tools Used
- Selenium WebDriver
- Python
- Win10Toast (desktop notifications)




## 🐞 Known Issues / Bugs (Login API)

Below are a few bugs identified during manual testing of the OrangeHRM Login API:

### 1. Incorrect HTTP Status Code for Failed Login
- **Description:** API returns `200 OK` even when login fails.
- **Expected:** Should return `401 Unauthorized` or `403 Forbidden`.
- **Impact:** Breaks RESTful conventions and confuses consumers.

### 2. No Rate Limiting on Login Attempts
- **Description:** No throttling or CAPTCHA on repeated failures.
- **Expected:** Temporary block or rate limit after multiple failed attempts.
- **Impact:** Vulnerable to brute-force attacks.

### 3. Missing CSRF Protection
- **Description:** Login API works without any CSRF tokens or secure headers.
- **Expected:** Require CSRF tokens or anti-forgery headers.
- **Impact:** Susceptible to CSRF attacks in browser environments.







