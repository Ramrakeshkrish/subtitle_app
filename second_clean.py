import pandas as pd
import re

# Load your dataset (Change the file path if needed)
file_path = "/Users/jrudram/Downloads/cleaned_data.csv" 
df = pd.read_csv(file_path)

# List of unwanted phrases
unwanted_phrases = [
    "api.opensubtitles", "timing and subtitles", "watch any video online",
    "support us and become vip", "advertisement", "subtitles by", 
    "opensubtitles free browser extension", "previously on", 
    "srt file by", "download subtitles from", "subtitles downloaded from"
]

# Function to clean subtitles using Pandas string functions
def clean_text(text):
    if pd.isna(text) or not isinstance(text, str):  # Skip empty or non-string values
        return ""

    text = text.lower().strip()  # Convert to lowercase and remove leading/trailing spaces

    # Remove timestamps
    text = text.replace("\n", " ").replace("\r", " ")  # Normalize line breaks
    text = re.sub(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text)

    # Remove numbering at the start of subtitles
    text = text.replace("1 ", "").replace("2 ", "").replace("3 ", "")

    # Remove unwanted phrases
    for phrase in unwanted_phrases:
        text = text.replace(phrase, "")

    # Apply Pandas string functions for better cleaning
    text = pd.Series(text).str.replace(r"<.*?>", "", regex=True)  # Remove HTML tags
    text = pd.Series(text).str.replace(r"[^\w\s]", "", regex=True)  # Remove special characters
    text = pd.Series(text).str.replace(r"\s+", " ", regex=True).str.strip()  # Remove extra spaces

    return text.iloc[0]  # Get cleaned text from Pandas Series

# Apply cleaning function to the "cleaned_subtitles" column
df["cleaned_subtitles"] = df["cleaned_subtitles"].apply(clean_text)

# Save the new cleaned dataset
new_csv_path = "/Users/jrudram/Downloads/cleaned_subtitles_final.csv"
df.to_csv(new_csv_path, index=False)

print(f"New cleaned dataset saved as: {new_csv_path}")