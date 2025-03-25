# subtitle_app
It ai power subtitle app



📌 Features

✅ Upload Audio Files (WAV, MP3, M4A)
✅ AI-Powered Subtitle Search using LangChain & ChromaDB
✅ Google Gemini AI Integration for intelligent answers
✅ Efficient Whisper Transcription to convert audio into text
✅ Optimized Parquet File Handling for fast loading
✅ GPU Acceleration Support (torch.cuda)

⸻

📌 Tech Stack

Technology	Purpose
Python	Core Programming
Streamlit	Interactive UI
LangChain	AI Pipeline
ChromaDB	Vector Storage
Google Gemini AI	Natural Language Understanding
Whisper AI	Audio Transcription
PyTorch & Torchaudio	GPU Acceleration



⸻

🚀 Installation Guide

🔹 1. Clone the Repository

git clone https://github.com/yourusername/ai-subtitle-search.git
cd ai-subtitle-search

🔹 2. Create a Virtual Environment

python3 -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate      # Windows

🔹 3. Install Dependencies

pip install -r requirements.txt

🔹 4. Set Up API Keys

1️⃣ Create a .env file:

nano .env

2️⃣ Add your Google Gemini API Key inside:

API_KEY=your_google_gemini_api_key

🔹 5. Run the Application

streamlit run app.py

✅ Now, upload an audio file & search for subtitles with AI!

⸻

📌 Usage

🎤 Upload Audio & Get AI-Generated Subtitles

1️⃣ Upload an audio file (WAV, MP3, M4A)
2️⃣ Whisper AI transcribes it into text
3️⃣ Google Gemini AI finds relevant subtitles
4️⃣ View AI-generated answers & subtitle sources

📸 Screenshot


⸻

📌 Troubleshooting

Issue	Solution
ModuleNotFoundError	Run pip install -r requirements.txt
API_KEY missing	Ensure .env contains API_KEY=your_google_gemini_api_key
ChromaDB not found	Delete chroma_db folder & restart
CUDA Not Available	Use CPU by setting DEVICE="cpu"



⸻

📌 Contributors

👨‍💻 Your Name – Lead Developer
📧 your.email@example.com
🔗 GitHub Profile

⸻

📌 License

📝 This project is licensed under the MIT License.

