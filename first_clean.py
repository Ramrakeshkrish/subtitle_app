import sqlite3
import pandas as pd
import re
import zipfile
import io


db_path ="/Users/jrudram/Downloads/eng_subtitles_database.db"  
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Read the `zipfiles` table
df = pd.read_sql_query("SELECT * FROM zipfiles", conn)

# Sample 30% of the data for faster processing
df = df.sample(frac=0.3, random_state=42)

# Function to extract subtitles from ZIP files
def extract_subtitles(binary_data):
    try:
        with zipfile.ZipFile(io.BytesIO(binary_data), "r") as z:
            for file in z.namelist():
                if file.endswith(".srt"):  # Process only .srt subtitle files
                    with z.open(file) as subtitle_file:
                        return subtitle_file.read().decode("latin-1")
    except zipfile.BadZipFile:
        try:
            return binary_data.decode("latin-1")  # Directly decode non-zip text
        except:
            return None  # If decoding fails

# Apply extraction to the `content` column
df["subtitles"] = df["content"].apply(extract_subtitles)

# Drop rows where extraction failed
df = df.dropna(subset=["subtitles"])

# Improved subtitle cleaning function
def clean_text(text):
    if pd.isna(text) or not isinstance(text, str):  # Skip empty or non-string values
        return ""

    text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces

    # Remove timestamps (e.g., 00:00:06,000 --> 00:00:12,074)
    text = re.sub(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text)

    # Remove numbering (lines like "1", "2" at the start)
    text = re.sub(r"^\d+\s*", "", text, flags=re.MULTILINE)

    # List of unwanted metadata phrases
    unwanted_phrases = [
        "api.opensubtitles", "timing and subtitles", "watch any video online",
        "support us and become vip", "advertisement", "subtitles by", 
        "opensubtitles free browser extension", "previously on", 
        "srt file by", "download subtitles from", "subtitles downloaded from"
    ]
    for phrase in unwanted_phrases:
        text = re.sub(r"\b" + re.escape(phrase.lower()) + r"\b", "", text, flags=re.IGNORECASE)

    # Remove HTML tags, special characters, and symbols
    text = re.sub(r"<.*?>", "", text)  # Remove HTML tags like <i>, <b>
    text = re.sub(r"[\[\]\(\)\{\}\-\_]", "", text)  # Remove [], (), {}, -, _
    text = re.sub(r"[\r\n]+", " ", text)  # Replace multiple newlines with a space
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces

    return text

# Apply cleaning
df["cleaned_subtitles"] = df["subtitles"].apply(clean_text)

# Save the cleaned data
csv_path = "/Users/jrudram/Downloads/cleaned_data.csv"
df.to_csv(csv_path, index=False)
print(f"Processed and saved cleaned subtitles: {len(df)} entries in {csv_path}")

# Close database connection
conn.close()