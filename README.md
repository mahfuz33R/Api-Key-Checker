# Api-Key-Checker

![License](https://img.shields.io/github/license/mahfuz33R/apikey-checker)
![Python Version](https://img.shields.io/badge/python-3.x-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)
![Issues](https://img.shields.io/github/issues/mahfuz33R/apikey-checker)
![Stars](https://img.shields.io/github/stars/mahfuz33R/apikey-checker?style=social)


**ApiKey Checker** is a free, open-source command-line tool written in Python that helps you validate API keys across multiple popular services quickly and easily. Whether you are a developer, security researcher, or cybersecurity engineer, this tool allows you to test API keys from web and mobile applications to identify which keys are active, unauthorized, or invalid.

The tool supports a wide range of services including:
- ✅ Google APIs: Maps Geocoding, Static Maps, Places, Firebase Firestore, Cloud Billing, Cloud Storage, YouTube Data, OAuth Token
- ✅ Facebook Graph API
- ✅ AWS API Gateway
- ✅ OpenAI API Key

When an API key is valid, **ApiKey Checker** provides you with a direct test URL (or header info) so you can manually verify or investigate further. For invalid or unauthorized keys, the tool returns a clean, minimal response like **"INVALID"** or **"UNAUTHORIZED"**, keeping your workflow fast and efficient.

The command-line interface is clean and user-friendly, featuring a large, centered ASCII art banner (powered by `pyfiglet`) and developer signature for a professional touch.

---

## 🔥 Features

- 🚀 **Multi-service API key validation**
- 🌐 **Test URLs for manual verification of valid keys**
- 🧩 **Simple and extendable Python codebase**
- ❌ **Minimal output for invalid or unauthorized keys**
- 📜 **Free and open-source under the MIT License**

---

## 📸 Screenshot

![apichecker](https://github.com/user-attachments/assets/2e63dc5d-47e0-4461-881c-2ca51244f491)


---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/apikey-checker.git
cd apikey-checker

2. **(Optional) Create a virtual environment:**

python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

🧩 Dependencies

3. **Install dependencies:**

requests
pyfiglet

pip3 install -r requirements.txt

🛠️ Usage
Run the tool in your terminal:

python apikey_checker.py

When prompted, enter your API keys separated by commas:

Enter your API keys (comma-separated):
AIzaSy..., sk-abc123..., fb-access-token...

The tool will automatically check each key across all supported services and display the results.

📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

👨‍💻 Developer
Developed and maintained by mahfuz33r.github.io

Contributions are welcome!
Feel free to fork the project, submit issues, or open pull requests.

🌟 Give a Star!
If you find this tool helpful, please consider giving the repository a ⭐️ on GitHub!




