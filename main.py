import numpy as np

# Initialize temperatures
TA, TB, TC, TD = 300.0, 300.0, 300.0, 300.0
iterations = 0
tolerance = 0.1
max_iter = 1000  # Prevent infinite loop

while True:
    iterations += 1
    # Store old values for residual calculation
    old = [TA, TB, TC, TD]

    # Update equations derived from finite difference method
    TA_new = (900 + TB) / 3
    TB_new = (500 + TA_new + TC) / 3
    TC_new = (500 + TB_new + TD) / 3
    TD_new = (500 + TC_new) / 2

    # Assign new values
    TA, TB, TC, TD = TA_new, TB_new, TC_new, TD_new

    # Calculate residuals
    residuals = np.abs([TA - old[0], TB - old[1], TC - old[2], TD - old[3]])

    # Check convergence
    if np.all(residuals < tolerance) or iterations >= max_iter:
        break

print(f"Converged in {iterations} iterations")
print(f"TA = {TA:.1f} °C")
print(f"TB = {TB:.1f} °C")
print(f"TC = {TC:.1f} °C")
print(f"TD = {TD:.1f} °C")
