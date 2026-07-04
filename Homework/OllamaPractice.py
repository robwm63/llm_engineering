# imports

import ollama
from openai import OpenAI
openai = OpenAI()

# what does this do? purpose?
OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')


def summarize(url):
    website = fetch_website_contents(url)
    response = OpenAI.chat.completions.create(
        model = "gpt-oss:latest",
        messages = messages_for(website)
    )
    return response.choices[0].message.content

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

def display_summary(url):
    summary = summarize(url)
    display(Markdown(summary))


summarize("https://edwarddonner.com")



