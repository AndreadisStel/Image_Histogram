import numpy as np
from PIL import Image
from typing import Dict
import matplotlib.pyplot as plt



# === hist_utils === #
def calculate_hist_of_img(img_array: np.ndarray, return_normalized: bool) -> Dict:
    flat = img_array.flatten()
    hist = {}
    for val in flat:
        hist[val] = hist.get(val, 0) + 1
    if return_normalized:
        total = len(flat)
        for key in hist:
            hist[key] /= total
    return dict(sorted(hist.items()))

def apply_hist_modification_transform(img_array: np.ndarray, modification_transform: Dict) -> np.ndarray:
    flat = img_array.flatten()
    modified_flat = np.array([modification_transform[val] for val in flat])
    return modified_flat.reshape(img_array.shape)



# === helpful functions for results === #
def save_img(img_array: np.ndarray, filename: str):
    img_uint8 = (img_array * 255).clip(0, 255).astype(np.uint8)
    Image.fromarray(img_uint8).save(filename)

def plot_histogram(img_array: np.ndarray, title: str):
    hist = calculate_hist_of_img(img_array, return_normalized=True)
    plt.figure()
    plt.bar(hist.keys(), hist.values(), width=0.01, color='black')
    plt.title(title)
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.show()



# === The core of the algorithm === #
def perform_hist_modification(img_array: np.ndarray, hist_ref: Dict, mode: str) -> np.ndarray:
    if mode == "post-disturbance":
        # Add uniform noise in [-d/2, d/2]
        unique_levels = np.sort(np.unique(img_array))
        if len(unique_levels) < 2:
            d = 1.0 / 255  
        else:
            d = unique_levels[1] - unique_levels[0]
        noise = np.random.uniform(-d / 2, d / 2, img_array.shape)
        img_array = (img_array + noise).clip(0, 1) 

    hist_input = calculate_hist_of_img(img_array, return_normalized=False)
    N = img_array.size

    input_levels = list(hist_input.keys())
    output_levels = list(hist_ref.keys())

    input_counts = [hist_input[level] for level in input_levels]
    desired_counts = [N * hist_ref[level] for level in output_levels]

    mod_transform = {}
    i = 0  
    j = 0  

    while i < len(input_levels) and j < len(output_levels):
        current_sum = 0
        start_i = i

        while i < len(input_levels):
            current_sum += input_counts[i]

            if mode == "greedy":
                if current_sum >= desired_counts[j]:
                    break

            elif mode == "non-greedy":
                deficiency = desired_counts[j] - sum(input_counts[start_i:i])
                if deficiency < input_counts[i] / 2:
                    break

            elif mode == "post-disturbance":
                if current_sum >= desired_counts[j]:
                    break

            i += 1

        for k in range(start_i, i + 1):
            if k < len(input_levels):
                mod_transform[input_levels[k]] = output_levels[j]
        j += 1
        i += 1

    # Assign remaining input levels to last output level
    while i < len(input_levels):
        mod_transform[input_levels[i]] = output_levels[-1]
        i += 1

    return apply_hist_modification_transform(img_array, mod_transform)




# === hist_modif === #
def perform_hist_eq(img_array: np.ndarray, mode: str) -> np.ndarray:
    hist = calculate_hist_of_img(img_array, return_normalized=False)
    L = len(hist)
    levels = np.linspace(0, 1, L)
    hist_ref = {lvl: 1 / L for lvl in levels}
    return perform_hist_modification(img_array, hist_ref, mode)

def perform_hist_matching(img_array: np.ndarray, img_array_ref: np.ndarray, mode: str) -> np.ndarray:
    hist_ref = calculate_hist_of_img(img_array_ref, return_normalized=True)
    return perform_hist_modification(img_array, hist_ref, mode)



# === Testing === #
if __name__ == "__main__":
    img = Image.open("hw1_images/input_img.jpg").convert("L")
    input_img = np.array(img).astype(float) / 255.0

    img_ref = Image.open("hw1_images/ref_img.jpg").convert("L")
    ref_img = np.array(img_ref).astype(float) / 255.0

    # Equalization
    eq_greedy = perform_hist_eq(input_img, "greedy")
    eq_non_greedy = perform_hist_eq(input_img, "non-greedy")
    eq_post = perform_hist_eq(input_img, "post-disturbance")

    save_img(eq_greedy, "equalized_greedy.png")
    save_img(eq_non_greedy, "equalized_nongreedy.png")
    save_img(eq_post, "equalized_post.png")

    # Matching
    matched_greedy = perform_hist_matching(input_img, ref_img, "greedy")
    matched_non_greedy = perform_hist_matching(input_img, ref_img, "non-greedy")
    matched_post = perform_hist_matching(input_img, ref_img, "post-disturbance")

    save_img(matched_greedy, "matched_greedy.png")
    save_img(matched_non_greedy, "matched_nongreedy.png")
    save_img(matched_post, "matched_post.png")

    
    #save_img(input_img, "input_img_bw.png")

    # Histograms
    plot_histogram(ref_img, "Reference Image Histogram")
    plot_histogram(input_img, "Original Image Histogram")
    plot_histogram(eq_greedy, "Equalized Image (Greedy) Histogram")
    plot_histogram(eq_non_greedy, "Equalized Image (Non-Greedy) Histogram")
    plot_histogram(eq_post, "Equalized Image (Post-Disturbance) Histogram")
    plot_histogram(matched_greedy, "Matched Image (Greedy) Histogram")
    plot_histogram(matched_non_greedy, "Matched Image (Non-Greedy) Histogram")
    plot_histogram(matched_post, "Matched Image (Post-Disturbance) Histogram")
