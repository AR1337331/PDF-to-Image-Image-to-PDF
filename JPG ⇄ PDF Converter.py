#MADE BY CHATGPT

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import fitz  # PyMuPDF
import os

class JPGPDFConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JPG ⇄ PDF Converter")
        self.geometry("400x250")
        self.configure(bg="#1e1e1e")

        tk.Label(self, text="Choose an option below", bg="#1e1e1e", fg="white", font=("Arial", 14)).pack(pady=20)

        tk.Button(self, text="Convert JPGs to PDF", command=self.convert_jpgs_to_pdf, width=30).pack(pady=10)
        tk.Button(self, text="Convert PDF to JPGs", command=self.convert_pdf_to_jpgs, width=30).pack(pady=10)

        tk.Label(self, text="All processing done locally.", bg="#1e1e1e", fg="gray").pack(side=tk.BOTTOM, pady=10)

    def convert_jpgs_to_pdf(self):
        files = filedialog.askopenfilenames(title="Select JPG Files", filetypes=[("JPG files", "*.jpg *.jpeg")])
        if not files:
            return
        images = [Image.open(f).convert("RGB") for f in sorted(files)]
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF file", "*.pdf")])
        if save_path:
            images[0].save(save_path, save_all=True, append_images=images[1:])
            messagebox.showinfo("Success", f"PDF saved to:\n{save_path}")

    def convert_pdf_to_jpgs(self):
        pdf_path = filedialog.askopenfilename(title="Select a PDF File", filetypes=[("PDF files", "*.pdf")])
        if not pdf_path:
            return
        output_folder = filedialog.askdirectory(title="Select Output Folder")
        if not output_folder:
            return
        try:
            doc = fitz.open(pdf_path)
            for i, page in enumerate(doc):
                pix = page.get_pixmap(dpi=200)
                output_path = os.path.join(output_folder, f"page_{i+1}.jpg")
                pix.save(output_path)
            messagebox.showinfo("Done", f"{len(doc)} JPG(s) saved in:\n{output_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert PDF:\n{e}")

# Run the app
if __name__ == "__main__":
    app = JPGPDFConverterApp()
    app.mainloop()

#MADE BY CHATGPT
