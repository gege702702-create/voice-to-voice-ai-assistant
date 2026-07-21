"""
text_to_speech.py
------------------
Step 3 of the task: convert the LLM's text reply into speech that the user
can hear directly.

We use the RealtimeTTS library because it streams audio immediately
(real-time streaming) instead of waiting for the whole file to be generated
before playback.

Requirements:
- Install the library:  pip install RealtimeTTS
"""

from RealtimeTTS import TextToAudioStream, SystemEngine


def speak(text: str) -> None:
    """
    Takes a text string, converts it to speech, and plays it through the
    speakers immediately.

    Args:
        text (str): The text to speak (the LLM's reply).
    """
    if not text or not text.strip():
        return

    engine = SystemEngine()  # uses the operating system's built-in TTS voice
    stream = TextToAudioStream(engine)

    print("🔊 Playing the voice reply now...")
    stream.feed(text)
    stream.play()


if __name__ == "__main__":
    # Quick standalone test of this file
    speak("Hello, this is a test of text to speech conversion.")
