## AI-Powered Browser Automation – Way2Automation Test

End-to-end automated form test powered by Browser-Use + OpenAI GPT-4o-mini, orchestrated with pytest.
This project demonstrates next-generation QA Automation, where natural language instructions drive the browser to perform real UI actions.

The test automatically:

Opens Way2Automation demo site

Types each field slowly (human-like typing)

Fills name, phone, email, country, city, username, password

Submits the form

Verifies expected message

Uses AI to interpret the task and autonomously operate the browser

This repository forms part of my QA Automation portfolio, showcasing modern approaches to testing using AI-driven automation.

#Features

✔ Automated UI interaction using Browser-Use (AI Agent)
✔ Natural language test instructions
✔ Controlled typing speed (slowMo, type_delay)
✔ Non-headless browser for visual demonstration
✔ Pytest integration
✔ Environment variables via dotenv

--
## Project Structure

| ai_way2automation_test

│

├── tests/

│   └── test_way2automation.py

│

├── .env

├── README.md
├── requirements.txt
└── .gitignore

--

## Installation & Setup

# 1. Clone the repo
git clone https://github.com/tuusuario/ai_way2automation_test.git
cd ai_way2automation_test

# 2.- Install dependencies
pip install -r requirements.txt

# 3.- Install dependencies
OPENAI_API_KEY=your_key_here

# 4.- Run!
pytest -s

The browser will open and the AI will begin performing the form automation.
 
--

## Tech Stack

Python 3.10+

Browser-Use (AI Browser Agent)

OpenAI GPT-4o-mini

Pytest

Dotenv for API key management

--

## Author
Ivan Huerta (Voxdeilex)

QA Automation Engineer

GitHub: https://github.com/voxdeilex
