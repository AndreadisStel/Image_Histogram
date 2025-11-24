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
Clone or download this repository, and make sure to adjust the input and reference images paths and names.

```bash
git clone https://github.com/AndreadisStel/Image_Histogram
cd Image_Histogram
```
