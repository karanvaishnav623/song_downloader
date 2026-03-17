import csv
import subprocess
import os

CSV_FILE = "Liked_Songs.csv"
TITLE_COLUMN = "Track Name"
DURATION_COLUMN = "Duration (ms)"

OUTPUT_DIR = "songs"
MAX_DURATION = 600000  # 10 minutes


def run_command(cmd):
    result = subprocess.run(cmd)
    return result.returncode == 0


def download(song):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_template = os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s")

    print("🔎 Searching:", song)

    # Try WAV first
    wav_cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "wav",
        "--audio-quality", "0",
        "-o", output_template,
        f"ytsearch1:{song}"
    ]

    success = run_command(wav_cmd)

    if success:
        print("✅ Downloaded in WAV\n")
        return

    print("⚠ WAV not available, trying MP3...")

    mp3_cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "-o", output_template,
        f"ytsearch1:{song}"
    ]

    success = run_command(mp3_cmd)

    if success:
        print("✅ Downloaded in MP3\n")
    else:
        print("❌ Failed:", song, "\n")


def main():

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(CSV_FILE, encoding="utf-8") as f:

        reader = csv.DictReader(f)

        # Check if duration column exists
        has_duration = DURATION_COLUMN in reader.fieldnames

        for row in reader:

            song = row.get(TITLE_COLUMN, "").strip()

            if not song:
                continue

            # Apply duration filter only if column exists
            if has_duration:
                duration_value = row.get(DURATION_COLUMN, "").strip()

                if duration_value.isdigit():
                    duration_ms = int(duration_value)

                    if duration_ms > MAX_DURATION:
                        print(f"⏭ Skipping (>10 min): {song}")
                        continue

            print("🎵 Processing:", song)

            download(song)


if __name__ == "__main__":
    main()
