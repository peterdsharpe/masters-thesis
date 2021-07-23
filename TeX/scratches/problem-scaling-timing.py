import aerosandbox as asb
import aerosandbox.numpy as np

def solve_noscaling():

    ### Parameters
    N = 100  # Number of discretization points
    time_final = 100  # seconds
    time = np.linspace(0, time_final, N)

    ### Constants
    mass_initial = 500e3  # Initial mass, 500 metric tons
    y_final = 100e3  # Final altitude, 100 km
    g = 9.81  # Gravity, m/s^2
    alpha = 1 / (300 * g)  # kg/(N*s), Inverse of specific impulse, basically - don't worry about this

    ### Environment
    opti = asb.Opti()

    ### Variables
    y = opti.variable(init_guess=np.linspace(0, y_final, N), scale=1)  # Altitude
    velocity = opti.variable(init_guess=y_final / time_final, scale=1, n_vars=N)  # Velocity
    mass = opti.variable(init_guess=mass_initial, scale=1, n_vars=N)  # Mass
    u = opti.variable(init_guess=g * mass_initial, scale=1, n_vars=N)  # Control vector

    ### Dynamics (implemented manually for now, we'll show you more sophisticated ways to do this in the Trajectory
    # Optimization part of the tutorial later on)
    opti.subject_to([  # Forward Euler, implemented manually for now
        np.diff(y) == velocity[:-1] * np.diff(time),
        np.diff(velocity) == (u[:-1] / mass[:-1] - g) * np.diff(time),
        np.diff(mass) == (-alpha * u[:-1]) * np.diff(time)
    ])

    ### Boundary conditions
    opti.subject_to([
        y[0] == 0,
        velocity[0] == 0,
        mass[0] == mass_initial,
        y[-1] == y_final
    ])

    ### Path constraints
    opti.subject_to([
        mass >= 0,
        u >= 0
    ])

    ### Objective
    opti.minimize(-mass[-1])  # Maximize the final mass == minimize fuel expenditure

    ### Solve
    sol = opti.solve(verbose=False)

def solve_scaling():
    ### Parameters
    N = 100  # Number of discretization points
    time_final = 100  # seconds
    time = np.linspace(0, time_final, N)

    ### Constants
    mass_initial = 500e3  # Initial mass, 500 metric tons
    y_final = 100e3  # Final altitude, 100 km
    g = 9.81  # Gravity, m/s^2
    alpha = 1 / (300 * g)  # kg/(N*s), Inverse of specific impulse, basically - don't worry about this

    ### Environment
    opti = asb.Opti()

    ### Variables
    y = opti.variable(init_guess=np.linspace(0, y_final, N))  # Altitude
    velocity = opti.variable(init_guess=y_final / time_final, n_vars=N)  # Velocity
    mass = opti.variable(init_guess=mass_initial, n_vars=N)  # Mass
    u = opti.variable(init_guess=g * mass_initial, n_vars=N)  # Control vector

    ### Dynamics (implemented manually for now, we'll show you more sophisticated ways to do this in the Trajectory
    # Optimization part of the tutorial later on)
    opti.subject_to([  # Forward Euler, implemented manually for now
        np.diff(y) == velocity[:-1] * np.diff(time),
        np.diff(velocity) == (u[:-1] / mass[:-1] - g) * np.diff(time),
        np.diff(mass) == (-alpha * u[:-1]) * np.diff(time)
    ])

    ### Boundary conditions
    opti.subject_to([
        y[0] == 0,
        velocity[0] == 0,
        mass[0] == mass_initial,
        y[-1] == y_final
    ])

    ### Path constraints
    opti.subject_to([
        mass >= 0,
        u >= 0
    ])

    ### Objective
    opti.minimize(-mass[-1])  # Maximize the final mass == minimize fuel expenditure

    ### Solve
    sol = opti.solve(verbose=False)

if __name__ == '__main__':
    import time

    for f in [solve_noscaling, solve_scaling]:
        def timeit():
            start = time.time()
            f()
            return time.time() - start

        times = np.array([
            timeit()
            for i  in range(10)
        ])

        print(np.median(times))