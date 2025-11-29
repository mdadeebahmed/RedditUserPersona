import os
import re
import praw
from dotenv import load_dotenv
from openai import OpenAI

# Load API keys from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Reddit API credentials
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="UserPersonaScript/1.0"
)

# Function to extract username from Reddit profile URL
def extract_username(url):
    match = re.search(r"reddit\.com\/user\/([^\/]+)", url)
    return match.group(1) if match else None

# Function to get comments and posts
def get_user_data(username, limit=50):
    redditor = reddit.redditor(username)
    comments = []
    posts = []

    try:
        for comment in redditor.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "link": f"https://www.reddit.com{comment.permalink}"
            })

        for post in redditor.submissions.new(limit=limit):
            posts.append({
                "title": post.title,
                "selftext": post.selftext,
                "link": f"https://www.reddit.com{post.permalink}"
            })

        return comments, posts

    except Exception as e:
        print(f"Error fetching data: {e}")
        return [], []

# Function to generate user persona using GPT
def generate_persona(username, comments, posts):
    messages = [
        {
            "role": "system",
            "content": "You are an analyst that builds user personas from Reddit activity."
        },
        {
            "role": "user",
            "content": f"""
Create a detailed user persona for the Reddit user '{username}' based on the following content.

Include:
- Name (if available)
- Age (estimated)
- Occupation / Studies
- Interests and hobbies
- Personality traits
- Social/Political views (if available)
- Reddit usage behavior
- Pain points or frustrations
- A representative quote
- Cite specific links from the provided posts/comments for each trait.

Posts:
{[f"{p['title']} - {p['selftext']} (Link: {p['link']})" for p in posts]}

Comments:
{[f"{c['body']} (Link: {c['link']})" for c in comments]}
"""
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1500
        )
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return "Failed to generate persona."

# Main execution
if __name__ == "__main__":
    input_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(input_url)

    if not username:
        print("Invalid Reddit URL.")
        exit(1)

    print(f"Extracting data for user: {username}")
    comments, posts = get_user_data(username)

    if not comments and not posts:
        print("No data found for user.")
        exit(1)

    print("Generating persona...")
    persona = generate_persona(username, comments, posts)

    output_path = f"users/{username}_persona.txt"
    os.makedirs("users", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {output_path}")
