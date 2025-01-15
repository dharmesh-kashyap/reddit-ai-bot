<br/>
<div align="center">
  <img src="https://github.com/user-attachments/assets/95a508e7-2ca8-4b73-89b7-aa007bb29877" alt="Logo" width="150" height="150">
</div>

<h1 align="center">
	Reddit-AI-Bot
</h1>

<h3 align="center">
	 An automated Reddit bot that leverages AI to generate engaging posts and comments
</h3>

## Overview
This project consists of two separate scripts:
1. **Post Bot (`post_bot.py`)**: Automatically posts AI-generated content to a specified subreddit.
2. **Comment Bot (`comment_bot.py`)**: Identifies posts with specific keywords and posts AI-generated comments.

Both scripts leverage the Groq AI API for content generation and the Reddit API for interaction with subreddits.

---

## Features
- **Post Bot**:
  - Generates and posts AI-driven content.
- **Comment Bot**:
  - Identifies posts with specific keywords.
  - Generates contextually relevant comments.

---

## Tech stack
- Reddit API
- Groq AI API
- Python

---

## Requirements
- Python 3.8 or higher
- Reddit API Credentials
- Groq AI API Key

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/reddit-ai-bot.git
cd reddit-ai-bot
```
### 2. Install Dependencies
Use the `requirements.txt` file to install all necessary libraries:
```bash
pip install -r requirements.txt
```
### 3. Set Up Credentials
Create a `.env` file in the project root and add the following:
```plaintext
# Groq API Key
GROQ_API_KEY=your_groq_api_key

# Reddit API Credentials
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_SECRET=your_reddit_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
USER_AGENT=RedditBot/0.1 by your_reddit_username
```
### 4. Verify Installation
Run the following commands to ensure all dependencies and configurations are correct:
```bash
python post_bot.py
python comment_bot.py
```
---

## Running the Scripts

### 1. Run the Post Bot
To generate and post AI content to a subreddit:
```bash
python post_bot.py
```
- By default, the script posts motivational or AI-related content.
- Edit the script to customize the post title, content prompt, and subreddit.
### 2. Run the Comment Bot
To identify posts with specific keywords and post comments:
```bash
python comment_bot.py
```
- By default, the script looks for posts containing the keyword "AI" in the subreddit test.
- Edit the script to customize the subreddit and keyword.
---

## Customization
- Subreddit:
  - Modify the `subreddit_name` variable in each script to target your desired subreddit.
- Keywords (for Comment Bot):
  - Update the `keyword` variable in `comment_bot.py` to target specific topics.
- Prompts:
  - Customize the `prompt` argument in the `generate_content` function for unique AI-generated content.
---

## Project Screenshot
### Post Bot output: 
![image](https://github.com/user-attachments/assets/0ad632e5-ee75-40b0-99cb-e9c4b03e6600)

### Comment Bot output: 
  ![image](https://github.com/user-attachments/assets/ab3a3f78-7374-404e-ab49-e42851ad7f10)


---
## Contact
<img align="left" src="https://avatars.githubusercontent.com/dharmesh-kashyap?size=100">

Made with ❤️ by [Dharmesh Kashyap](https://github.com/dharmesh-kashyap), get in touch!

<a href="mailto:dharmeshkashyap46@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Email-D14836?style=flat&logo=gmail&logoColor=white" alt="Email Badge" height="25"></a>&nbsp;
<a href="https://www.linkedin.com/in/dharmesh-kashyap" target="_blank"><img src="https://img.shields.io/badge/Linkedin-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Badge" height="25"></a>&nbsp;

<br clear="left"/>


