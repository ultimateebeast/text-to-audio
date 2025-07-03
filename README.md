# 🔊 Text-to-Audio PDF Reader (Python)

A Python-based tool that reads aloud the content of a PDF file using text-to-speech (TTS). This application extracts all printable text from a PDF (such as books or documents) and speaks it using the system's default voice.

---

## 📚 Features

- 📄 Reads and extracts text from any PDF file
- 🔊 Converts extracted text into audio using TTS
- 🎧 Speaks content aloud in real-time
- 🧠 Simple, efficient, and offline — no internet required

---

## 🛠 Requirements

Install the required libraries using `pip`:

bash
pip install PyPDF2
pip install pyttsx3
pip install pyaudio

▶️ How to Use
Clone the repository or download the script:

git clone https://github.com/ultimateebeast/text-to-audio
cd text-to-audio

Run the Python script:
python text_to_audio.py

Enter the PDF file path when prompted.
The program will extract the text and start reading it aloud.

📌 Note
This tool reads all printable text from the given PDF.

Non-standard or image-based PDFs may not produce meaningful results.

Works offline using your system’s built-in voice engine.

🧑‍💻 Author
Pratyush Jain
🔗 GitHub: @ultimateebeast

📄 License
This project is licensed under the MIT License
