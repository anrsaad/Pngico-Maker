
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def png_to_ico(png_file, size=(32, 32)):
    """Converts a PNG image to an ICO file.

    Args:
        png_file (str): Path to the PNG image file.
        size (tuple, optional): Desired size of the ICO image. Defaults to (32, 32).
    """

    # Open the PNG image
    img = Image.open(png_file)

    # Resize the image if necessary
    if img.size != size:
        img = img.resize(size)

    # Convert the image to RGB mode (if not already)
    if img.mode != "RGB":
        img = img.convert("RGB")

    # Create a new ICO image
    ico = Image.new("RGB", (size[0], size[1]))

    # Paste the resized image onto the ICO image
    ico.paste(img, (0, 0))

    # Get the ICO file path by replacing the extension
    ico_file = png_file.replace(".png", ".ico")

    # Save the ICO image
    ico.save(ico_file, format="ICO")

    # Show a success message
    success_label.config(text="Conversion successful!")

def browse_png():
    png_file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if png_file:
        png_entry.delete(0, tk.END)
        png_entry.insert(0, png_file)

def convert_image():
    png_file = png_entry.get()
    if png_file:
        size = (int(width_entry.get()), int(height_entry.get()))
        png_to_ico(png_file, size)

# Create the main window
window = tk.Tk()
window.title("PNGICO Maker")

# Prevent the window from being maximized
window.resizable(False, False)

# Create labels and entry fields
png_label = tk.Label(window, text="PNG File:")
png_label.grid(row=0, column=0, padx=10, pady=10)
png_entry = tk.Entry(window, width=50)
png_entry.grid(row=0, column=1, padx=10, pady=10)

browse_button = tk.Button(window, text="Browse", command=browse_png)
browse_button.grid(row=0, column=2, padx=10, pady=10)

width_label = tk.Label(window, text="Width:")
width_label.grid(row=1, column=0, padx=10, pady=10)
width_entry = tk.Entry(window, width=10)
width_entry.grid(row=1, column=1, padx=10, pady=10)

height_label = tk.Label(window, text="Height:")
height_label.grid(row=1, column=2, padx=10, pady=10)
height_entry = tk.Entry(window, width=10)
height_entry.grid(row=1, column=3, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert_image)
convert_button.grid(row=2, column=1, padx=10, pady=10)

success_label = tk.Label(window, text="", fg="green")
success_label.grid(row=3, column=1, padx=10, pady=10)

# Set default values
width_entry.insert(0, 32)
height_entry.insert(0, 32)

# Start the GUI
window.mainloop()