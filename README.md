# Voice-to-Voice AI Assistant 🎙️🤖🔊

A voice-based AI assistant that listens to the user, converts speech to text,
sends that text to a Large Language Model (LLM) to generate a smart reply,
and converts the reply back into speech that the user hears directly.

---

## 🧠 Project Concept

The project is built around 3 core, sequential steps:
🎤 User's voice
   │
   ▼
1) Speech-to-Text   (convert speech into text)     → via RealtimeSTT / Whisper
   │
   ▼
2) LLM Processing   (process text, generate reply) → via Cohere API
   │
   ▼
3) Text-to-Speech   (convert reply into speech)    → via RealtimeTTS
   │
   ▼
🔊 User hears the reply

---

## 📂 File Structure

| File | Purpose |
|---|---|
| main.py | The main entry point; runs the three steps in a continuous loop |
| speech_to_text.py | Step 1: opens the microphone and converts speech into text |
| llm_chat.py | Step 2: sends the text to the Cohere model and receives a reply |
| text_to_speech.py | Step 3: converts the model's reply into speech and plays it |
| config.py | Loads the Cohere API key from a .env file |
| .env.example | A template for the settings file — copy it, rename to .env, and add your key |
| requirements.txt | The list of all Python libraries required to run the project |

---

## ⚙️ Installation & Setup Steps

### 1) Install Python
Make sure you have Python 3.9 or newer installed on your machine.

### 2) Install FFmpeg (needed for Whisper / RealtimeSTT)
FFmpeg processes audio in the background and is required for speech
recognition to work. A tutorial for installing it on Windows:
https://www.youtube.com/watch?v=22vmzTs5BoE

⚠️ Important: Restart your computer after installing FFmpeg and after
installing Whisper-related packages.

### 3) Clone the project and install the librariesgit clone <your-repository-url>
cd voice_assistant
pip install -r requirements.txt

### 4) Get a Cohere API key
- Create a free account at: https://dashboard.cohere.com/api-keys
- Copy your key.
- Copy the .env.example file and rename it to .env.
- Put your key in it like this:COHERE_API_KEY=your_key_here

### 5) Run the voice assistantpython main.py
Once running: speak into your microphone, wait for the program to transcribe
your speech into text, send it to the model, and then it will automatically
speak the reply back to you. Press Ctrl+C to stop the program.

---

## 🔍 Detailed Explanation of Each Step

### 1️⃣ Speech-to-Text (`speech_to_text.py`)
We use the RealtimeSTT library (built on top of OpenAI's Whisper
model) because it:
- Opens the microphone and starts recording automatically.
- Detects when the user stops speaking (a short silence) and stops
  recording on its own.
- Transcribes the recorded audio directly into text with no extra steps.

### 2️⃣ LLM Processing (`llm_chat.py`)
The text produced by the previous step is sent to Cohere
(model `command-r-plus-08-2024`) via its API, and we get back a smart,
context-appropriate text reply. Cohere can be swapped for any other LLM
(such as OpenAI's GPT) using the same logic: send text, receive a reply.

### 3️⃣ Text-to-Speech (`text_to_speech.py`)
The text reply from the previous step is passed to RealtimeTTS, which
converts it immediately into speech and plays it through the device's
speakers — no need to save an intermediate audio file.

### 🔁 Connecting the Three Steps (`main.py`)
The main file keeps repeating this loop:
listen → transcribe to text → send to the model → receive reply →
convert to speech → play it.

---

## 📌 Additional Notes

- The code is written in Python and split into separate modules for easier
  reading and editing.
- If you run into installation issues with RealtimeSTT or RealtimeTTS, make
  sure FFmpeg is installed correctly and restart your machine first.
- You can switch the recognition language from English to Arabic (or any
  other supported language) by changing the language value in
  speech_to_text.py.
- Every function in this project was written following the official
  documentation of RealtimeSTT, RealtimeTTS, and Cohere. Since the code
