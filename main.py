from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, gaussian_filter, sobel
import numpy as np

# ----------------------------
# Load image and convert to array
# ----------------------------
def load_image(path):
    """
    Load image from path and return NumPy array (RGB)
    """
    img = Image.open(path).convert("RGB")
    img_array = np.array(img)
    return img_array
# ----------------------------
# Convert RGB image to Grayscale
# ----------------------------
def to_grayscale(img_array):
    """
    Convert RGB image array to grayscale using standard formula
    """
    gray = 0.299*img_array[:,:,0] + 0.587*img_array[:,:,1] + 0.114*img_array[:,:,2]
    return gray.astype(np.uint8)

    # ─────────────────────────────────────────
# Blur
# ─────────────────────────────────────────
def apply_blur(img, sigma=2):
    """
    Gaussian blur apply karo
    sigma badhao = zyada blur
    """
    gray = to_grayscale(img)
    return gaussian_filter(gray, sigma=sigma)


# ─────────────────────────────────────────
# Sharpen
# ─────────────────────────────────────────
def apply_sharpen(img):
    """
    Sharpen filter — edges aur details sharp karo
    """
    gray = to_grayscale(img)
    kernel = np.array([[0,-1,0],
                       [-1,5,-1],
                       [0,-1,0]], dtype=float)
    result = convolve(gray.astype(float), kernel)
    return np.clip(result, 0, 255).astype(np.uint8)


# ─────────────────────────────────────────
# Edge Detection
# ─────────────────────────────────────────
def apply_edges(img):
    """
    Sobel edge detection — boundaries dhundho
    """
    gray = to_grayscale(img)
    gx = sobel(gray.astype(float), axis=1)
    gy = sobel(gray.astype(float), axis=0)
    magnitude = np.sqrt(gx**2 + gy**2)
    return np.clip(magnitude, 0, 255).astype(np.uint8)



#------------------------------------
# Brightness adjustment
#------------------------------------
def adjust_brightness(img_array, factor=1.2):
    """
    Adjust brightness of an image array.
    factor > 1 → brighter
    factor < 1 → darker
    Works for grayscale or RGB images
    """
    bright = img_array * factor
    bright = np.clip(bright, 0, 255)  # values stay in 0-255
    return bright.astype(np.uint8)

#-----------------------------
#Rotate operations
#-----------------------------
def flip_horizontal(img_array):
    """
    Flip image horizontally (mirror image)
    Works for grayscale or RGB
    """
    return np.flip(img_array, axis=1)

def rotate_90(img_array):
    """
    Rotate image 90 degrees counter-clockwise
    Works for grayscale or RGB
    """
    return np.rot90(img_array)


# ----------------------------
# Display image
# ----------------------------
def show_image(img_array, title="Image", cmap=None):
    plt.imshow(img_array, cmap=cmap)
    plt.title(title)
    plt.axis("off")
    plt.show()



imag  = ["images/indoor.jpg", "images/cow.jpg", "images/sunset.jpg"]
names = ["indoor", "cow", "sunset"]
images = [load_image(p) for p in imag]

for name, img in zip(names, images):
    gray      = to_grayscale(img)
    bright_g  = adjust_brightness(gray, factor=1.5)
    bright_c  = adjust_brightness(img, factor=1.2)
    flipped   = flip_horizontal(img)
    rotated   = rotate_90(img)
    blurred   = apply_blur(img, sigma=2)
    sharpened = apply_sharpen(img)
    edges     = apply_edges(img)

    plt.figure(figsize=(20, 4))
    plt.suptitle(f"Image: {name}", fontsize=14)

    plt.subplot(1,8,1); plt.imshow(img);              plt.title("Original");       plt.axis("off")
    plt.subplot(1,8,2); plt.imshow(gray, cmap='gray');plt.title("Grayscale");      plt.axis("off")
    plt.subplot(1,8,3); plt.imshow(bright_g,cmap='gray');plt.title("Bright Gray"); plt.axis("off")
    plt.subplot(1,8,4); plt.imshow(bright_c);         plt.title("Bright Color");   plt.axis("off")
    plt.subplot(1,8,5); plt.imshow(flipped);          plt.title("Flipped");        plt.axis("off")
    plt.subplot(1,8,6); plt.imshow(blurred,cmap='gray');plt.title("Blur");         plt.axis("off")
    plt.subplot(1,8,7); plt.imshow(sharpened,cmap='gray');plt.title("Sharpen");    plt.axis("off")
    plt.subplot(1,8,8); plt.imshow(edges,cmap='gray');plt.title("Edges");          plt.axis("off")

    plt.tight_layout()
    plt.show()