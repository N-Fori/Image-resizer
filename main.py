import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("400x450")
        self.image_path = None

        tk.Label(root, text="Image Resizer", font=("Arial", 16)).pack(pady=10)

        self.load_button = tk.Button(root, text="Choose Image", command=self.load_image)
        self.load_button.pack(pady=10)

        self.path_label = tk.Label(root, text="No image selected", wraplength=380)
        self.path_label.pack()

        tk.Label(root, text="Width:").pack(pady=5)
        self.width_entry = tk.Entry(root)
        self.width_entry.pack()

        tk.Label(root, text="Height:").pack(pady=5)
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        self.resize_button = tk.Button(root, text="Resize and Save", command=self.resize_image)
        self.resize_button.pack(pady=20)

    def load_image(self):
        filetypes = [("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        path = filedialog.askopenfilename(filetypes=filetypes)
        if path:
            self.image_path = path
            self.path_label.config(text=os.path.basename(path))

    def resize_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please choose an image first.")
            return

        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Width and Height must be numbers.")
            return

        img = Image.open(self.image_path)
        resized_img = img.resize((width, height), Image.LANCZOS)

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])

        if save_path:
            resized_img.save(save_path)
            messagebox.showinfo("Success", f"Image saved to:\n{save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()