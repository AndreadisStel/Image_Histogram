# Image_Histogram

This project implements histogram modification techniques for grayscale images, including histogram equalization and histogram matching. Three modes are supported: **greedy**, **non-greedy**, and **post-disturbance**.

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
- `numpy`
- `Pillow` (`PIL`)
- `matplotlib`
- `typing` (built-in in Python 3.5+)

Install dependencies using pip:

```bash
pip install numpy pillow matplotlib
