# ☕ The Cozy Roast — AI-Powered Cafe Ordering System

An interactive full-stack cafe ordering web application built with **Python (Flask)**, a responsive **HTML5/Tailwind CSS** UI, and an **LLM-driven AI Barista** that generates real-time pairing recommendations during checkout.

---

## 🌟 Key Features

- **Dynamic Food Catalog & Interactive Tray**: Live item selection with real-time subtotal and 5% GST calculation.
- **AI Barista Upsell Engine**: Uses an LLM to analyze current cart items and recommend the best complementary pairing before checkout.
- **Server-Side Order Verification**: Flask verifies pricing and calculations to ensure accurate, tamper-proof receipts.
- **Official Order Receipt**: Generates a clean digital receipt modal with itemized pricing, tax breakdowns, and print support.
- **Environment Variable Security**: Keeps private API keys and endpoints safe using `.env` and `.gitignore`.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, `python-dotenv`
- **Frontend**: HTML5, Tailwind CSS, Lucide Icons, Vanilla JavaScript (`Fetch API`)
- **AI Integration**: OpenAI Python SDK (compatible with OpenAI, Gemini proxies, Groq, etc.)
- **Version Control**: Git & GitHub

---

## 📂 Project Structure

```text
cafe/
├── hotelmenu.py       # Flask backend server, business logic & API routes
├── index.html         # Responsive cafe interface, order tray & receipt modal
├── .env               # Private API keys and URLs (ignored by Git)
├── .gitignore         # Prevents sensitive files from being pushed
└── README.md          # Project documentation
```
# 🚀 Getting Started
## 1. Clone the Repository
```bash
git clone [https://github.com/knAshvita/cafe-menu-app.git](https://github.com/knAshvita/cafe-menu-app.git)
cd cafe-menu-app
```
## 2. Install Required Dependencies
```bash
pip install flask openai python-dotenv
```
## 3. Setup Environment Variables
Create a .env file in the root folder:
```bash
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_BASE_URL=your_actual_base_url_here
MODEL_NAME=gemini-2.5-flash
```
## 4. Run the Application
```bash
python hotelmenu.py
```
## 5. Open in Browser
```bash
Visit http://127.0.0.1:5000 to use the app.
```
## 📡 API Endpoints
## 📡 API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `GET` | `/` | Serves the cafe frontend UI |
| `GET` | `/api/menu` | Retrieves the list of available items and prices |
| `POST` | `/api/recommend` | Analyzes cart items and returns an AI pairing suggestion |
| `POST` | `/api/order` | Verifies prices, computes taxes, and generates the final bill |
# 🛡️ Security
```bash
This project uses a .gitignore file to ensure sensitive .env secrets and Python cache files (__pycache__/) are never uploaded to GitHub.
```