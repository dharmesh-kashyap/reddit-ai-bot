import praw
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),  # Get the Groq API key from the .env file
)

# Reddit API Credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_SECRET = os.getenv("REDDIT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = os.getenv("USER_AGENT")

# Initialize the Reddit client
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=USER_AGENT,
)

# Function to generate content using Groq's chat completion
def generate_content(prompt="Write an engaging post about AI innovations.", model="llama-3.3-70b-versatile"):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model,
        )
        generated_text = chat_completion.choices[0].message.content
        return generated_text
    except Exception as e:
        print(f"Error generating content: {e}")
        return None

# Function to post to Reddit
def post_to_reddit(subreddit_name="test", title="Daily AI Insights", prompt="Write an engaging post about AI innovations."):
    try:
        # Generate content using Groq
        content = generate_content(prompt)
        if content:
            # Post to the subreddit
            subreddit = reddit.subreddit(subreddit_name)
            subreddit.submit(title=title, selftext=content)
            print(f"Successfully posted to r/{subreddit_name}")
        else:
            print("Failed to generate content. Skipping post.")
    except Exception as e:
        print(f"Error posting to Reddit: {e}")

# Test the bot
if __name__ == "__main__":
    subreddit_name = "test"  # Replace with your desired subreddit
    post_title = "Daily Developer Motivation"
    post_prompt = "Write a motivational post for developers."
    post_to_reddit(subreddit_name=subreddit_name, title=post_title, prompt=post_prompt)
