## Install dependencies
pip install -r requirements.txt

## Add your API keys
Create a .env file with the following:
OPENAI_API_KEY=your_openai_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret

## How to Use
In cmd: python reddit_persona.py

Enter the Reddit profile URL when prompted (e.g. https://www.reddit.com/user/kojied/)

The script will:
Extract username

Scrape recent comments and posts

Generate a detailed persona using OpenAI GPT

Save the output to users/{username}_persona.txt

## Technologies Used
praw – Reddit API wrapper

openai – For persona generation using GPT

dotenv – For secure API key handling

Python 3.8+

## License
This project is for evaluation purposes only and is not intended for production use. Generated content belongs to the respective users or OpenAI where applicable.
