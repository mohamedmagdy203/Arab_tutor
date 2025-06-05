# 🎥 Arab tutor - AI Dubbing & Summarization API

This project provides an AI-powered API for automatic **video dubbing** and **summarization**. Users upload a video in English, and receive:

* 🎧 Arabic voice-over
* 💬 Arabic summarization
* 📽️ A new downloadable dubbed video with synchronized lips

---

## 🌐 API Overview

### POST `/dub`

Upload an English video to start the dubbing pipeline.

#### Request

* `multipart/form-data`
* Field: `file` (MP4 video)

#### Response

```json
{
  "summary": "...Arabic summary...",
  "download_url": "https://<your-ngrok-url>/download/output_xxx.mp4"
}
```

---

### GET `/download/{filename}`

Download the final video using the filename returned from the `/dub` response.

---

## 🚀 Technologies Used

* FastAPI (backend)
* Whisper (transcription)
* BART (summarization)
* XTTS (Arabic TTS)
* MoviePy & ffmpeg
* Wav2Lip (lip-sync)
* Deep Translator
* ngrok (expose locally hosted API to internet)

---

## ⚙️ How to Run Locally

### 1. Clone the Repo

```bash
git clone <repo-url>
cd graduate_project
```

### 2. Install Requirements

Create a conda/venv env and run:

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Start ngrok Tunnel

```bash
ngrok config add-authtoken <your-token>
ngrok http 8000
```

### 5. Open API Docs

Visit:

```
https://<your-ngrok-subdomain>.ngrok.io/docs
```

---

## 🔎 API Flow (For Frontend/Full-Stack)

1. Send `POST /dub` with video file (MP4)
2. Receive response:

   * `summary`: Arabic text summary
   * `download_url`: link to final dubbed video
3. Call `GET /download/{filename}` to get the video

---

## ⚠️ Notes

* The server must stay running during use (hosted locally)
* All file processing is done on your machine
* Wav2Lip is called via subprocess in a separate conda env

---

## 🙌 Author

* Mohamed Magdy
* AI/ML Engineering | Deep Learning | NLP
* Graduation Project 2025

---
