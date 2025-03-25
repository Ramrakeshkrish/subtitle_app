## **🎮 AI Subtitle Search Engine with RAG**
**Find subtitles easily using AI-powered search & audio transcription**  

![Subtitle Search Engine](https://via.placeholder.com/800x400?text=AI+Subtitle+Search+Engine)  

---

### **📌 Features**
👉 **Upload Audio Files** (WAV, MP3, M4A)  
👉 **AI-Powered Subtitle Search** using **LangChain & ChromaDB**  
👉 **Google Gemini AI Integration** for intelligent answers  
👉 **Efficient Whisper Transcription** to convert audio into text  
👉 **Optimized Parquet File Handling** for fast loading  
👉 **GPU Acceleration Support** (`torch.cuda`)  

---

### **📌 Tech Stack**
| **Technology** | **Purpose** |
|--------------|------------|
| **Python** | Core Programming |
| **Streamlit** | Interactive UI |
| **LangChain** | AI Pipeline |
| **ChromaDB** | Vector Storage |
| **Google Gemini AI** | Natural Language Understanding |
| **Whisper AI** | Audio Transcription |
| **PyTorch & Torchaudio** | GPU Acceleration |

---

## **🚀 Installation Guide**
### **🔹 1. Clone the Repository**
```bash
git clone https://github.com/yourusername/ai-subtitle-search.git
cd ai-subtitle-search
```

### **🔹 2. Create a Virtual Environment**
```bash
python3 -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate      # Windows
```

### **🔹 3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **🔹 4. Set Up API Keys**
1. Create a **`.env`** file:  
```bash
nano .env
```
2. Add your **Google Gemini API Key** inside:
```
API_KEY=your_google_gemini_api_key
```

### **🔹 5. Run the Application**
```bash
streamlit run app.py
```
💚 **Now, upload an audio file & search for subtitles with AI!**

---

## **📌 Usage**
### **🎤 Upload Audio & Get AI-Generated Subtitles**
1. **Upload an audio file** (WAV, MP3, M4A)  
2. **Whisper AI transcribes it into text**  
3. **Google Gemini AI finds relevant subtitles**  
4. **View AI-generated answers & subtitle sources**  

### **🖼️ Screenshot**
![App Screenshot](https://via.placeholder.com/800x400?text=App+Screenshot)

---

## **📌 Troubleshooting**
| **Issue** | **Solution** |
|-----------|-------------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `API_KEY missing` | Ensure `.env` contains `API_KEY=your_google_gemini_api_key` |
| `ChromaDB not found` | Delete `chroma_db` folder & restart |
| `CUDA Not Available` | Use CPU by setting `DEVICE="cpu"` |



---

## **📌 License**
📝 This project is licensed under the **MIT License**.  

---

### **🚀 Now Your Project Has a Professional README! 🚀**

