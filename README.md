# Path Loss Exponent Estimation using RSSI Data

## Overview

This project estimates the **Path Loss Exponent (PLE)** in an unknown environment using RSSI (Received Signal Strength Indicator) measurements. It leverages the **log-distance path loss model** to analyze signal strength decay with distance and uses this model to estimate unknown distances based on RSSI.

> Developed using **Python** as part of a Computer Networking course assignment.

---

##  Dataset Description

###  HW2_part1.csv
- Column A: Distances (in meters)
- Columns B–N: RSSI values (in dBm) recorded at those distances

###  HW2_part2.csv
- Column A: Actual distances (used only to evaluate error)
- Columns B–P: RSSI values (in dBm) to estimate distance from RSSI

---

##  Tasks and Features

###  Task 1: Estimate Path Loss Exponent
- Average RSSI values for each distance
- Plot **RSSI vs log10(distance)**
- Fit a **best-fit line**
- Calculate:
  - **Slope (m)** of the line
  - **Path Loss Exponent (n)** = |slope| / 10
  - **Variance** of RSSI values w.r.t the fitted line

###  Task 2: Distance Estimation Using PLE
- Assume `d₀ = 1 meter`
- Calculate `Pr(d₀)` as the average RSSI at 1 meter
- Use the formula:

  \[
  d = d₀ \times 10^{\frac{P(d₀) - P(d)}{10n}}
  \]

- Estimate distance from RSSI values
- Compare with ground truth
- Report average error over 5 samples

---

##  Sample Output

```bash
Estimated Path Loss Exponent (n): 2.71
Variance of RSSI samples: 1.93 dBm²

--- Distance Estimation Results ---
Actual: 3.0 m, Estimated: 2.85 m, Error: 0.15 m
Actual: 5.0 m, Estimated: 4.66 m, Error: 0.34 m
Actual: 8.0 m, Estimated: 7.42 m, Error: 0.58 m
Actual: 10.0 m, Estimated: 9.21 m, Error: 0.79 m
Actual: 15.0 m, Estimated: 14.12 m, Error: 0.88 m

Average Estimation Error: 0.55 meters
