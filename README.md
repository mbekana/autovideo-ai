# 🎬 AutoVideo: Automated Video Editing with Python + Free AI Tools

**AutoVideo** is a production-ready, modular Python framework for automating high-quality video creation using **free tools** like:

- 🎙️ AI-powered text-to-speech (TTSMaker or local engines)
- 🧠 OpenAI Whisper for transcription
- 🎞️ DaVinci Resolve scripting API (Ubuntu supported)
- 🧰 FFmpeg and MoviePy for automated editing

Built for content creators, educators, and developers who want to **automate YouTube, TikTok, and Shorts content** from script to export — all from Python.

---

## 🚀 Features

- ✅ Full script-to-video pipeline automation  
- 🧠 AI-powered text-to-speech & subtitles  
- 🎬 DaVinci Resolve timeline creation via Python API  
- 🎞️ Fallback video composition using FFmpeg or MoviePy  
- 🎧 Audio sync, subtitle prep, and visual block parsing  
- 🪵 Robust logging and modular architecture  
- 💻 100% offline-capable (no paid APIs required)  

---

## 📁 Project Structure

```plaintext
autovideo/
├── autovideo/
│   ├── audio/           # TTS + transcription
│   ├── video/           # DaVinci + FFmpeg editors
│   ├── workflow/        # Pipeline logic
│   ├── utils/           # File ops, logging
│   ├── config.py
│   └── logger.py
├── scripts/             # CLI entrypoints
│   └── generate_video.py
├── tests/               # Unit tests
├── requirements.txt     # Pip requirements
├── pyproject.toml       # Poetry support (optional)
└── README.md
```

## 🧠 How It Works

1. **Input:** A script text file + a folder of video assets (`clip_1.mp4`, etc.)

2. **Audio:** The script is converted to audio using TTS (TTSMaker by default)

3. **Parsing:** The script is split into visual blocks and matched to clips

4. **Editing:**
   - 📍 If DaVinci Resolve is installed (on Ubuntu): it builds a timeline automatically
   - 🔁 Otherwise, it uses FFmpeg to auto-compose the video

5. **Export:** The final video with voiceover and visuals is exported for publishing


## 🧪 Requirements

- Python 3.9+  
- Ubuntu 20.04+ (tested)  
- DaVinci Resolve (Free or Studio, optional)  
- FFmpeg  
- OpenAI Whisper  

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Pipeline

```bash
python scripts/generate_video.py \
  --script script.txt \
  --assets assets \
  --output final_video.mp4 \
  --davinci
  ```
