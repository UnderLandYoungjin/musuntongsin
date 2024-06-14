#챗GPT가 작성한 코드 그대로 첨부 하는거라 참조하실때 유의 부탁드립니다!

import math

# Constants
c = 3e8  # Speed of light in m/s
k = 1.38e-23  # Boltzmann's constant in J/K

# Given parameters
R = 100e6  # Data rate in bps
fc = 24e9  # Carrier frequency in Hz
PEIRP_dBm = 45  # PEIRP in dBm
D = 0.1  # Antenna diameter in m
eta = 0.5  # Antenna efficiency
T = 400  # Antenna temperature in K
d = 10e3  # Distance in m
margin_dB = 2  # Margin in dB
other_losses_dB = 2  # Other losses in dB

# Converting PEIRP from dBm to Watts
PEIRP_W = 10 ** ((PEIRP_dBm - 30) / 10)

# Free Space Path Loss (FSPL)
FSPL_dB = 20 * math.log10(d) + 20 * math.log10(fc) + 20 * math.log10(4 * math.pi / c)

# Antenna Gain
Gt_dB = 10 * math.log10(eta * (math.pi * D * fc / c) ** 2)
Gr_dB = Gt_dB  # Assuming transmit and receive antenna gains are the same

# Link Budget
link_budget_dB = PEIRP_dBm - FSPL_dB + Gr_dB - other_losses_dB - margin_dB

# Bandwidth (assuming same as data rate for BFSK)
B = R

# Receiver Noise Power
N = k * T * B
N_dBm = 10 * math.log10(N) + 30  # Convert to dBm

# Signal to Noise Ratio (SNR)
SNR_dB = link_budget_dB - N_dBm

# Maximum allowable Noise Figure
NF_dB = SNR_dB

# Output results
print(f"Maximum allowable Noise Figure (NF): {NF_dB:.2f} dB")

# Part (b) - Doubling the Data Rate
R_new = 2 * R
B_new = 2 * B
N_new = k * T * B_new
N_dBm_new = 10 * math.log10(N_new) + 30
SNR_dB_new = link_budget_dB - N_dBm_new
NF_dB_new = SNR_dB_new

print(f"Part (b): New Noise Figure with doubled data rate: {NF_dB_new:.2f} dB")

# Part (c) - Doubling the Carrier Frequency
fc_new = 2 * fc
FSPL_dB_new = 20 * math.log10(d) + 20 * math.log10(fc_new) + 20 * math.log10(4 * math.pi / c)
link_budget_dB_new = PEIRP_dBm - FSPL_dB_new + Gr_dB - other_losses_dB - margin_dB
SNR_dB_new = link_budget_dB_new - N_dBm
NF_dB_new = SNR_dB_new

print(f"Part (c): New Noise Figure with doubled carrier frequency: {NF_dB_new:.2f} dB")

# Part (d) - Doubling the Antenna Diameter
D_new = 2 * D
Gt_dB_new = 10 * math.log10(eta * (math.pi * D_new * fc / c) ** 2)
Gr_dB_new = Gt_dB_new
link_budget_dB_new = PEIRP_dBm - FSPL_dB + Gr_dB_new - other_losses_dB - margin_dB
SNR_dB_new = link_budget_dB_new - N_dBm
NF_dB_new = SNR_dB_new

print(f"Part (d): New Noise Figure with doubled antenna diameter: {NF_dB_new:.2f} dB")

# Part (e) - Halving the Distance
d_new = d / 2
FSPL_dB_new = 20 * math.log10(d_new) + 20 * math.log10(fc) + 20 * math.log10(4 * math.pi / c)
link_budget_dB_new = PEIRP_dBm - FSPL_dB_new + Gr_dB - other_losses_dB - margin_dB
SNR_dB_new = link_budget_dB_new - N_dBm
NF_dB_new = SNR_dB_new

print(f"Part (e): New Noise Figure with half the distance: {NF_dB_new:.2f} dB")
