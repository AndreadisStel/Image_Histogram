# Histogram Equalization and Matching Toolkit

This repository provides a Python implementation of several histogram-based image enhancement techniques for grayscale images. It includes histogram equalization, histogram matching, and multiple transformation modes: **greedy**, **non-greedy**, and **post-disturbance**.  
The toolkit is designed for experimentation and research in image processing.

---

## Table of Contents
- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Functions Overview](#functions-overview)
- [Examples](#examples)
- [License](#license)

---

## Features
- Compute histograms of grayscale images (normalized and non-normalized).
- Perform histogram equalization:
  - Greedy
  - Non-Greedy
  - Post-Disturbance (adds small uniform noise before equalization)
- Perform histogram matching to a reference image.
- Save images and plot histograms for visualization.

---

## Dependencies
The code requires the following Python packages:
- `Python 3.8+`
- `numpy`
- `Pillow` (`PIL`)
- `matplotlib`

Install dependencies using pip:

```bash
pip install numpy pillow matplotlib
```

---

## Installation
Clone or download this repository:

```bash
git clone https://github.com/AndreadisStel/Image_Histogram
cd Image_Histogram
```

---

## Usage
The code is modular and can be imported as a library, with the `__main__` section serving as a demonstration workflow.\
Run the script with Python: 

```bash
python demo.py
```

This will:

- Load input_img.jpg and ref_img.jpg.
- Perform histogram equalization and matching in three modes:
  - greedy
  - non-greedy
  - post-disturbance
- Save the resulting images:
  - Equalized: equalized_greedy.png, equalized_nongreedy.png, equalized_post.png
  - Matched: matched_greedy.png, matched_nongreedy.png, matched_post.png
- Plot the histograms for visualization.

---

## Examples 

```python
from PIL import Image
import numpy as np
from hist_modif import perform_hist_eq, perform_hist_matching, save_img

img = Image.open("hw1_images/input_img.jpg").convert("L")
input_img = np.array(img).astype(float) / 255.0

img_ref = Image.open("hw1_images/ref_img.jpg").convert("L")
ref_img = np.array(img_ref).astype(float) / 255.0

eq_greedy = perform_hist_eq(input_img, "greedy")
save_img(eq_greedy, "equalized_greedy.png")

matched_post = perform_hist_matching(input_img, ref_img, "post-disturbance")
save_img(matched_post, "matched_post.png")
```

## License

