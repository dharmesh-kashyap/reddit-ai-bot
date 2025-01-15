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
def generate_content(prompt="Write a comment for this post", model="llama-3.3-70b-versatile"):
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

# Function to post comments on subreddit posts
def comment_on_posts(subreddit_name="test", keyword="AI"):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        # Fetch the top 10 hot posts in the subreddit
        for submission in subreddit.hot(limit=10):
            # Skip if already commented
            if submission.comments.list():
                continue

            # Check if the post contains the keyword
            if keyword.lower() in submission.title.lower():
                print(f"Found a post to comment on: {submission.title}")
                # Generate a comment using Groq
                prompt = f"Write a comment for this post: {submission.title}"
                comment_content = generate_content(prompt)
                if comment_content:
                    # Post the comment
                    submission.reply(comment_content)
                    print(f"Commented on post: {submission.title}")
                else:
                    print("Failed to generate a comment.")
    except Exception as e:
        print(f"Error commenting on posts: {e}")

# Test the bonus feature
if __name__ == "__main__":
    subreddit_name = "test"  # Replace with your desired subreddit
    keyword = "AI"  # Replace with your desired keyword to filter posts
    print("Running the bot to comment on posts...")
    comment_on_posts(subreddit_name=subreddit_name, keyword=keyword)
