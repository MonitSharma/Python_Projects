import pyttsx3   # pip install pyttsx3
import PyPDF2    # pip install PyPDF2
from tkinter.filedialog import *

# To select PDF File from your folder
book = askopenfilename()

# To open and read the selected file
pdfreader = PyPDF2.PdfFileReader(book)

# To count total no.of pages in your PDF file
pages = pdfreader.numPages

# To read PDF file from 1st page to the last page
for num in range(0, pages):
  page = pdfreader.getPage(num)
  text = page.extractText()
  player = pyttsx3.init()
  player.say(text)
  player.runAndWait()