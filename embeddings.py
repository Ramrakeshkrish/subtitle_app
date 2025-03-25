import os
import pandas as pd
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# ✅ Step 1: Load API Key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("❌ API_KEY is missing! Please check your .env file.")

# ✅ Step 2: Load the cleaned subtitles dataset
csv_path = "/Users/jrudram/Downloads/intership/shazam/data/cleaned_subtitles_final.csv"
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"❌ CSV file not found at {csv_path}")

df = pd.read_csv(csv_path)

if "cleaned_subtitles" not in df.columns:
    raise ValueError("❌ Column 'cleaned_subtitles' not found in CSV file!")

# ✅ Step 3: Convert subtitles into LangChain Document format
documents = [Document(page_content=row["cleaned_subtitles"]) for _, row in df.iterrows()]

if not documents:
    raise ValueError("❌ No subtitles found to process!")

# ✅ Step 4: Load Google Gemini embeddings model
try:
    embedding_model = GoogleGenerativeAIEmbeddings( 
    model="models/embedding-001", google_api_key=API_KEY)
except Exception as e:
    raise RuntimeError(f"❌ Error loading GoogleGenerativeAIEmbeddings: {e}")

# ✅ Step 5: Ensure ChromaDB directory exists
chroma_db_path = "/Users/jrudram/Downloads/intership/shazam/data/chroma_db"
os.makedirs(chroma_db_path, exist_ok=True)

# ✅ Step 6: Store embeddings in ChromaDB
try:
    vector_db = Chroma.from_documents(documents, embedding_model, persist_directory=chroma_db_path)
    print("✅ Subtitle embeddings stored successfully in ChromaDB!")
except Exception as e:
    raise RuntimeError(f"❌ Error storing embeddings in ChromaDB: {e}")