import pyttsx3
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Get PDF file path using GUI popup
def get_pdf_file_via_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )
    return file_path

# Read and speak the PDF file
def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        total_pages = len(reader.pages)
        print(Fore.CYAN + f"📄 Total pages: {total_pages}")

        speaker = pyttsx3.init()
        speaker.setProperty('rate', 170)
        speaker.setProperty('volume', 1.0)

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and text.strip():
                print(Fore.LIGHTWHITE_EX + f"🔊 Reading page {i + 1}")
                speaker.say(text)
                speaker.runAndWait()
            else:
                print(Fore.YELLOW + f"⚠️ Skipping empty or unreadable page {i + 1}")

        speaker.stop()
        print(Fore.GREEN + "\n✅ Finished reading the PDF.")

    except Exception as e:
        print(Fore.RED + f"❌ Error reading PDF: {e}")

# Main program
if __name__ == "__main__":
    print(Fore.CYAN + "\n📖 Text-to-Audio PDF Reader\n")
    file_path = get_pdf_file_via_popup()

    if file_path:
        print(Fore.GREEN + f"✅ Selected file: {file_path}\n")
        read_pdf(file_path)
    else:
        print(Fore.RED + "❌ No file selected. Exiting.")
