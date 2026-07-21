"""
main.py
-------
This is the main file that ties the three steps together:

    User speaks     -->  (Speech-to-Text)   -->  text
    Text            -->  (LLM / Cohere)      -->  text reply
    Text reply      -->  (Text-to-Speech)    -->  audio the user hears

Run this file directly after setting up the requirements:
    python main.py
"""

from speech_to_text import listen_and_transcribe
from llm_chat import generate_response
from text_to_speech import speak


def run_voice_assistant():
    print("=" * 50)
    print("🚀 Starting the Voice-to-Voice AI Assistant")
    print("Press Ctrl+C at any time to stop the program")
    print("=" * 50)

    while True:
        try:
            # 1) Convert speech to text
            user_text = listen_and_transcribe()

            # 2) Send the text to the LLM and get a reply
            reply_text = generate_response(user_text)

            # 3) Convert the reply text to speech and play it
            speak(reply_text)

        except KeyboardInterrupt:
            print("\n👋 Voice assistant stopped. Goodbye!")
            break


if __name__ == "__main__":
    run_voice_assistant()
