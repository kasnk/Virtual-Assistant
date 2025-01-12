# Virtual Assistant

This is a Python-based virtual assistant built to perform various tasks like answering questions, setting reminders, fetching news, and performing web searches. The assistant uses APIs like OpenAI for conversational AI, NewsAPI for retrieving news, and other custom functionalities for integration with external services.

## Features
- **Conversational Assistant**: Powered by OpenAI's GPT model for answering queries and carrying on conversations.
- **News Fetcher**: Retrieve the latest news headlines using NewsAPI.
- **Web Search**: Use a custom web scraping function to fetch results from the web.
- **Voice Assistant**: Interaction via text-to-speech and speech-to-text.
- **Task Management**: Ability to set reminders and perform other tasks.

## Requirements

- Python 3.x
- Required libraries (listed below)
    speech_recognition as sr
    webbrowser
    pyttsx3
    pyaudio
    setuptools
    os
    musicLibrary
    requests
    dotenv 
    os
## Setup

### 1. Clone the repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/your-username/virtual-assistant.git
cd virtual-assistant

python -m venv .venv

.venv\Scripts\activate

source .venv/bin/activate

pip install -r requirements.txt

OPENAI_API_KEY=your-openai-api-key-here
NEWS_API_KEY=your-news-api-key-here

python client.py

virtual-assistant/
│
├── .venv/               # Virtual environment (don't upload this to GitHub)
├── client.py            # Main script to run the assistant
├── .env                 # Store sensitive API keys
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── assistant/           # Folder containing helper modules (news_fetcher.py, etc.)




##Contributing
If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request with your changes.

##Author
Shekhar Nipane
