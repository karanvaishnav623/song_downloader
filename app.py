import csv
import subprocess
import os


CSV_FILE = "Liked_Songs.csv"
COLUMN = "Track Name"

OUTPUT_DIR = "/storage/emulated/0/Music/Mydsongs"


def download(song):

    # Make folder if not exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_template = os.path.join(OUTPUT_DIR, "%(title)s.%(ext)s")

    cmd = [
        "python",
        "-m",
        "yt_dlp",
        "-x",
        "--audio-format", "wav",
        "--audio-quality", "0",
        "-o", output_template,
        f"ytsearch1:{song}"
    ]

    subprocess.run(cmd)


def main():

    with open(CSV_FILE, encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            song = row[COLUMN].strip()

            if not song:
                continue

            print("🎵 Downloading:", song)

            download(song)

            print("✅ Saved in offline_songs:", song, "\n")


if __name__ == "__main__":
    main()
