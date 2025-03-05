import numpy as np
# Isaac Legault 3/4/2025
# Both problems are solved using Iterative Gauss-Seidel Method to solve the system of equations

# Problem 1: 4-Node Thermal System

def solve_problem1():
    print("\nProblem 1: 4-Node Thermal System")
    TA, TB, TC, TD = 300.0, 300.0, 300.0, 300.0
    tolerance = 0.1
    max_iter = 1000
    converged = False

    for iter in range(max_iter):
        old = [TA, TB, TC, TD]

        # Update equations
        TA = (900 + TB) / 3
        TB = (500 + TA + TC) / 3
        TC = (500 + TB + TD) / 3
        TD = (500 + TC) / 2

        # Check residuals
        residuals = np.abs([TA - old[0], TB - old[1], TC - old[2], TD - old[3]])
        if np.all(residuals < tolerance):
            converged = True
            break

    if converged:
        print(f"Converged in {iter + 1} iterations")
        print(f"TA = {TA:.1f} °C\nTB = {TB:.1f} °C\nTC = {TC:.1f} °C\nTD = {TD:.1f} °C")
    else:
        print("Problem 1 did not converge")


# Problem 2: 12-Node Thermal System

def solve_problem2():
    print("\nProblem 2: 12-Node Thermal System")
    T = {f'T{i}': 100.0 for i in range(1, 13)}
    tolerance = 0.1
    max_iter = 1000
    converged = False

    for iter in range(max_iter):
        old_T = T.copy()
        residuals = []

        # Update equations for each node
        # First row (insulated top)
        T['T1'] = (2 * T['T4'] + T['T2'] + 100) / 4
        residuals.append(abs(T['T1'] - old_T['T1']))

        T['T2'] = (2 * T['T5'] + T['T3'] + T['T1']) / 4
        residuals.append(abs(T['T2'] - old_T['T2']))

        # T3 has right heat flux
        T['T3'] = (T['T2'] + T['T6'] + 400 / 400) / 2  # 400 W/m² flux converted to ΔT
        residuals.append(abs(T['T3'] - old_T['T3']))

        # Second row
        T['T4'] = (T['T1'] + T['T7'] + T['T5'] + 100) / 4
        residuals.append(abs(T['T4'] - old_T['T4']))

        T['T5'] = (T['T2'] + T['T8'] + T['T6'] + T['T4']) / 4
        residuals.append(abs(T['T5'] - old_T['T5']))

        T['T6'] = (T['T5'] + T['T3'] + T['T9'] + 400 / 400) / 3
        residuals.append(abs(T['T6'] - old_T['T6']))

        # Third row
        T['T7'] = (T['T4'] + T['T8'] + T['T10'] + 100) / 4
        residuals.append(abs(T['T7'] - old_T['T7']))

        T['T8'] = (T['T5'] + T['T7'] + T['T9'] + T['T11']) / 4
        residuals.append(abs(T['T8'] - old_T['T8']))

        T['T9'] = (T['T6'] + T['T8'] + T['T12'] + 400 / 400) / 3
        residuals.append(abs(T['T9'] - old_T['T9']))

        # Fourth row (convection bottom)
        h = 1000
        k = 400
        T_inf = 20
        T['T10'] = (k * T['T7'] + k * T['T11'] + h * T_inf) / (2 * k + h)
        residuals.append(abs(T['T10'] - old_T['T10']))

        T['T11'] = (k * T['T10'] + k * T['T12'] + k * T['T8'] + h * T_inf) / (3 * k + h)
        residuals.append(abs(T['T11'] - old_T['T11']))

        T['T12'] = (k * T['T11'] + k * T['T9'] + 400 + h * T_inf) / (2 * k + h)
        residuals.append(abs(T['T12'] - old_T['T12']))

        if max(residuals) < tolerance:
            converged = True
            break

    if converged:
        print(f"Converged in {iter + 1} iterations")
        for i in range(1, 13):
            print(f"T{i} = {T[f'T{i}']:.1f} °C")
    else:
        print("Problem 2 did not converge")


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    solve_problem1()
    solve_problem2()