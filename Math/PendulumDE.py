import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
g = 9.807
l = 1
mu = 0.2
theta_0 = 0
dtheta_0 = 7

def ddtheta(dtheta, theta):
    return -mu * dtheta - (g / l) * np.sin(theta)

def theta(t):
    theta = theta_0
    dtheta = dtheta_0
    
    for i in np.arange(0, t, dt):
        dtheta += ddtheta(dtheta, theta) * dt
        theta += dtheta * dt

    return theta

def main():
    fig, ax = plt.subplots()
    # x_dom = list(np.arange(0, 10, dt))
    # y = [theta(x) for x in x_dom]
    # # y_dom = list(range(0, 10, 1))
    # plt.plot(x_dom, y)

    # x is theta, y is dtheta
    x_dom = list(np.arange(0, 10, np.pi/8))
    y_dom = list(np.arange(-5, 5, 0.5))
    for x in x_dom:
        for y in y_dom:
            dx = y
            dy = ddtheta(y, x)
            ax.quiver(x, y, dx, dy, units="width")


    theta = theta_0
    dtheta = dtheta_0
    X = []
    Y = []
    for i in np.arange(0, 5, dt):
        theta += dtheta * dt
        dtheta += ddtheta(dtheta, theta) * dt
        X.append(theta)
        Y.append(dtheta)


    plt.plot(X, Y)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()