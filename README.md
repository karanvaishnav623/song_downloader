# 🎵 Spotify CSV Song Downloader

This tool downloads songs listed in a **Spotify exported CSV file** using **yt-dlp**.
Songs are downloaded as **WAV (preferred)** or **MP3 (fallback)** and saved locally.

---

## 📂 Project Structure

```
song_downloader/
│
├── app.py
├── Liked_Songs.csv
├── requirements.txt
│
└── songs/
```

Downloaded songs will be saved automatically inside the **songs/** folder.

---

## ⚙️ Requirements

* Python **3.8+**
* **ffmpeg**
* Python package:

  * `yt-dlp`

---

## 🐍 Setup Environment

Create a virtual environment:

```
python3 -m venv venv
```

Activate it:

**Linux / Mac**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

Install dependencies:

```
pip install yt-dlp
```

---

## 🎧 Install FFmpeg

`yt-dlp` requires **ffmpeg** to convert audio.

### Linux

```
sudo apt install ffmpeg
```

### Mac

```
brew install ffmpeg
```

### Windows

Download from:

```
https://ffmpeg.org/download.html
```

---

## ▶️ Running the Script

Place your **Spotify CSV file** in the same folder as `app.py`.

Run:

```
python app.py
```

Songs will start downloading into the **songs/** folder.

---

## 📋 CSV Requirements

The CSV file must contain:

* `Track Name`

Optional column:

* `Duration (ms)`

Example:

```
Track Name,Duration (ms)
Tania,215000
Ikky,198000
```

If **`Duration (ms)` is present**, songs longer than **10 minutes** will be skipped.

If the **duration column is missing**, the script will **continue downloading all songs without duration filtering**.

---

## ⚡ Download Behavior

The script follows these rules:

* ⏱ Skips songs longer than **10 minutes** *(only if duration column exists)*
* 🎧 Attempts **WAV download first**
* 🎧 Falls back to **MP3 (highest quality)** if WAV is unavailable
* 📁 Saves files to the **songs/** directory

---

## 🚀 Example Output

```
🎵 Processing: Tania
🔎 Searching: Tania
✅ Downloaded in WAV

🎵 Processing: Ikky
⚠ WAV not available, trying MP3...
✅ Downloaded in MP3
```

---
