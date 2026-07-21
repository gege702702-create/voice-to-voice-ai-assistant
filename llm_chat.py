"""
llm_chat.py
-----------
Step 2 of the task: send the transcribed text to a Large Language Model (LLM)
and get back a suitable text reply.

We use the Cohere API here (as suggested in the task instructions), but this
can be swapped for any other LLM (e.g. OpenAI) using the same idea: send text,
receive a reply.

Requirements:
- Install the library:  pip install cohere
- Get a free API key from: https://dashboard.cohere.com/api-keys
- Put the key in a .env file under the name COHERE_API_KEY
"""

import cohere
from config import COHERE_API_KEY

# Create the Cohere client once
co = cohere.ClientV2(api_key=COHERE_API_KEY)


def generate_response(user_text: str) -> str:
    """
    Sends the user's text to the Cohere model and returns the model's reply.

    Args:
        user_text (str): The text coming from the Speech-to-Text step.

    Returns:
        str: The LLM's text reply.
    """
    if not user_text or not user_text.strip():
        return "I didn't hear anything clearly, could you try again?"

    response = co.chat(
        model="command-r-plus-08-2024",  # a current Cohere chat model
        messages=[
            {"role": "user", "content": user_text}
        ],
    )

    reply_text = response.message.content[0].text
    print(f"🤖 Model reply: {reply_text}")
    return reply_text


if __name__ == "__main__":
    # Quick standalone test of this file
    sample = "Hello, how are you?"
    generate_response(sample)
