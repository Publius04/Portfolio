from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import numpy as np
import time

# GLOBALS
R = 3.8 # Between 0 and 4
X0 = 0.1 # Between 0 and R
MAX_ITER = 100

def f(x, r):
    return x * (r - x)

def plot_spiral():
    fig, ax = plt.subplots()

    # Parabola
    X = np.linspace(0, R, 50)
    Y = f(X, R)
    plt.plot(X, Y)

    # Line
    X = np.linspace(0, 4, 50)
    Y = X
    plt.plot(X, Y)

    # Points
    X = [X0]
    Y = [0]
    for _ in range(MAX_ITER):
        # Point on parab
        X.append(X[len(X)-1])
        Y.append(f(X[len(X)-1], R))

        # Point on line
        val = Y[len(Y)-1]
        X.append(val)
        Y.append(val)

    plt.plot(X, Y)
    plt.show()

def plot_tree():
    def get_y(R):
        Y = [X0]
        for _ in X:
            Y.append(f(Y[len(Y)-1], R))
        Y = Y[:-1]
        return Y

    X = np.linspace(X0, 4, MAX_ITER)
    fig, ax = plt.subplots()
    l, = plt.plot(X, get_y(R))
    plt.subplots_adjust(left=0.25, bottom=0.25)

    axR = plt.axes([0.1, 0.25, 0.0225, 0.63])
    rSlider = Slider(
        ax=axR,
        label='r',
        valmin=0,
        valmax=10,
        valinit=R,
        orientation="vertical"
    )

    def update(val):
        l.set_ydata(get_y(rSlider.val))
        fig.canvas.draw_idle()

    rSlider.on_changed(update)

    plt.show()

def pitchfork():
    _,_ = plt.subplots()
    r = np.linspace(1, 4, 100000)
    X = []
    Y = []
    for i in r:
        x0 = 0.5
        for _ in range(1000):
            x0 = f(x0, i)
        X.append(i)
        Y.append(x0)
        tmp = x0
        x0 = f(x0, i)
        for _ in range(1000):
            if abs(x0 - tmp) < 0.0001 * tmp:
                break
            X.append(i)
            Y.append(x0)
            x0 = f(x0, i)
    plt.scatter(X, Y, s = 0.1)
    plt.show()

def main():
    # plot_spiral()
    pitchfork()

if __name__ == "__main__":
    main()

