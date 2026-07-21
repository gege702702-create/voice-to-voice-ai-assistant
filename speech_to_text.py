"""
speech_to_text.py
------------------
Step 1 of the task: convert speech (from the microphone) into text.

We use the RealtimeSTT library (internally powered by OpenAI's Whisper
model) because it handles microphone recording and real-time transcription
for us, without having to write the recording logic by hand.

Requirements:
- Install the library:  pip install RealtimeSTT
- Install FFmpeg on your machine (tutorial link is in the task's README).
"""

from RealtimeSTT import AudioToTextRecorder


def listen_and_transcribe() -> str:
    """
    Opens the microphone, listens to the user speaking, and once they stop
    talking (a short silence is detected) returns the transcribed text.

    Returns:
        str: The text transcribed from speech.
    """
    recorder = AudioToTextRecorder(
        model="base",          # can be tiny / small / medium / large depending on your hardware
        language="en",         # change to "ar" if you want Arabic recognition
        spinner=False,
    )

    print("🎤 Speak now... (recording stops automatically on silence)")
    text = recorder.text()
    print(f"📝 Transcribed text: {text}")
    return text


if __name__ == "__main__":
    # Quick standalone test of this file
    listen_and_transcribe()
