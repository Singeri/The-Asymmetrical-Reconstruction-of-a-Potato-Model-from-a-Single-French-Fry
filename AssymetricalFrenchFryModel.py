#2D Mathematical model for reconstruction of a potato based on a singular french fry made by Singeri and posted on github. 


import numpy as np

H_fry = 10 # original fry length
fry_width = 2 #thickness of the cut
S_top = 13 # slope adjustment for the top (degrees)
S_bottom = 15 # slope adjustment for the bottom (degrees)

L = H_fry / 2
alpha_deg = np.degrees(2 * np.arctan(0.5))

def calculate_peak(slope):
    denominator = 2 * np.tan(np.radians((180 - (alpha_deg + slope)) / 2))
    return L / denominator

h_top = calculate_peak(S_top)
h_bottom = calculate_peak(S_bottom)

H_total = H_fry + h_top + h_bottom


def calculate_width(h):
    return ((L / 2)**2 + h**2) / h

W_top = calculate_width(h_top)
W_bottom = calculate_width(h_bottom)

W_total = max(W_top, W_bottom)

print("Results:")
print(f"\nTotal height: {round(H_total, 2)} cm")
print(f"\nTotal width: {round(W_total, 2)} cm")
print(f"\nTop Peak: {round(h_top, 2)} cm")
print(f"\nBottom peak: {round(h_bottom, 2)} cm")
