# 🖼️ Image Processing Pipeline — NumPy + PIL + SciPy

A beginner-friendly yet powerful image processing pipeline built with Python. Load any image and apply Grayscale, Brightness, Flip, Blur, Sharpen, and Edge Detection — all from scratch using NumPy arrays. No deep learning required!

---

## 🚀 Features

* 🎨 Convert RGB images to Grayscale
* ☀️ Adjust brightness (brighter or darker)
* 🪞 Flip image horizontally (mirror effect)
* 🔄 Rotate image 90 degrees
* 🌫️ Gaussian Blur — smooth out noise
* ✨ Sharpen — make edges crisp and clear
* 🔍 Edge Detection — find object boundaries using Sobel
* 📊 Display all results in one window side by side
* 🖼️ Supports multiple images in one run (batch processing)

---

## 🛠️ Tech Stack

* Python 3.11
* NumPy — pixel-level array operations
* Pillow (PIL) — image loading
* SciPy — convolution, Gaussian filter, Sobel
* Matplotlib — image display and subplots

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/nikhilkumar210h-debug/image-processing-pipeline
cd image-processing-pipeline
```

Install dependencies:

```bash
pip install numpy pillow scipy matplotlib
```

---

## ▶️ Usage

Add your images to the `images/` folder, then run:

```bash
python main.py
```

To use your own images, edit this line in `main.py`:

```python
imag  = ["images/indoor.jpg", "images/cow.jpg", "images/sunset.jpg"]
names = ["indoor", "cow", "sunset"]
```

---

## 🎨 Filters and Functions

| Function | What it does |
|---|---|
| `load_image(path)` | Image load karo NumPy array mein |
| `to_grayscale(img)` | RGB → Grayscale (0.299R + 0.587G + 0.114B) |
| `adjust_brightness(img, factor)` | factor > 1 bright, factor < 1 dark |
| `flip_horizontal(img)` | Mirror image banao |
| `rotate_90(img)` | 90 degree counter-clockwise rotate |
| `apply_blur(img, sigma)` | Gaussian blur — sigma badhao = zyada blur |
| `apply_sharpen(img)` | Kernel convolution se edges sharp karo |
| `apply_edges(img)` | Sobel X + Y se edge magnitude nikalo |

---

## 📊 Output

Har image ke liye ek window mein 8 results ek saath dikhte hain:

```
Original | Grayscale | Bright Gray | Bright Color | Flipped | Blur | Sharpen | Edges
```

## 📂 Project Structure

```
image-processing-pipeline/
│
├── main.py              # Main application
├── README.md            # This file
└── images/
    ├── indoor.jpg       # Sample image 1
    ├── cow.jpg          # Sample image 2
    └── sunset.jpg       # Sample image 3
```

---

## 🧠 How It Works

Har image ek NumPy array hai — shape `(rows, cols, 3)` jahan 3 = R, G, B channels.

```python
img.shape  # (3742, 3144, 3)
#             rows  cols  RGB
```

Filters ek **3x3 kernel** ko image ke upar slide karte hain. Har pixel ke liye uske aaspaas ke 9 pixels se calculation hoti hai:

```
Blur kernel:        Sharpen kernel:     Sobel X:
1/9  1/9  1/9       0  -1   0          -1  0  1
1/9  1/9  1/9      -1   5  -1          -2  0  2
1/9  1/9  1/9       0  -1   0          -1  0  1
```

---

## ⚠️ Requirements

* Windows / Mac / Linux
* Python 3.10+
* Images in `images/` folder

---

## 🔮 Future Improvements

* 🎛️ GUI — slider se brightness aur blur control karo
* 📷 Webcam se live filter apply karo
* 🤖 ML model add karo — object detection
* 💾 Processed images save karo automatically
* 🌈 Color-based filters (sepia, negative, etc.)

---

## 🤝 Contributing

Feel free to fork this repo and add new filters. Pull requests are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 💡 Author

Made with ❤️ by **Nikhil Kumar**
