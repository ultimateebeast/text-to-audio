# 🔊 Text-to-Audio PDF Reader (Python)

A modern, Python-based tool that reads aloud the content of any PDF file using text-to-speech (TTS). Built with `PyPDF2`, `tkinter`, and `pyttsx3`, this application extracts all readable text from a PDF (such as books or documents) and speaks it using your system's voice engine. It now features a visual file picker popup for selecting files easily.

---

## 📚 Features

- 📂 Choose PDF file via file picker (no path typing!)
- 📄 Extracts text from standard, searchable PDF files
- 🔊 Reads the extracted text aloud using TTS
- 🧠 Works completely offline — no internet required
- 🎧 System voice support with adjustable rate/volume
- 📝 Optional support for summarizing the spoken content *(coming soon)*

---

## 🛠 Requirements

Install the required Python libraries:

pip install PyPDF2 pyttsx3 pyaudio colorama
🧠 tkinter comes pre-installed with Python, no need to install it separately.

▶️ How to Use
Clone the repository:

git clone https://github.com/ultimateebeast/text-to-audio
cd text-to-audio
Run the script:

python main.py
Choose a PDF file using the popup file selector.

The program will extract the text and start reading it aloud using your system's default voice.

📌 Notes
Works best with searchable PDFs (not scanned/image-based ones).

Pages without readable text will be skipped automatically.

All processing is done locally — your data never leaves your device.

🧑‍💻 Author
Pratyush Jain
🔗 GitHub: @ultimateebeast

📄 License
This project is licensed under the MIT License.
