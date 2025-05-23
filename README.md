# 🔍 Automated Pytest Workflow

This project uses **GitHub Actions** to run automated tests with **Pytest** daily and optionally sends test status notifications to **Slack**.

## 📁 Project Structure
project-root/
│
├── tests/
│ └── sample_test.py
│
├── payloads/
│ └── sample_payloads.json
│
├── .github/workflows/
│ └── pytest-daily.yml # GitHub Actions workflow file
│
├── requirements.txt
└── README.md\

## ⚙️ Workflow Summary

The CI workflow (`pytest-daily.yml`) is triggered:

- ✅ Automatically **every day at 7:00 AM UTC**
- 🛠️ Or manually via the GitHub Actions **"Run workflow"** button

## 🔧 Steps Performed

1. **Checkout Code**  
   Pulls the latest version of your repository.

2. **Set Up Python**  
   Installs the specified Python version (default: 3.x).

3. **Install Dependencies**  
   Uses `requirements.txt` to install Pytest and other dependencies.

4. **Run Pytest**  
   Runs all tests in the `tests/` directory.

5. **Slack Notification** *(Optional)*  
   Sends a Slack message with the test result using a webhook.

## ✅ Setup Instructions

1. Add your tests in the `tests/` folder.
2. Create a `requirements.txt` with:
   ```text
   pytest
   requests