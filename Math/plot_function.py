import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
# Types of plots: 2d elementary function, 2d differential equation, 2d implicit equation
color1 = [1, 0, 0]
color2 = [0, 0, 1]
y0_separation = 1
y0_max = 10
y0_min = -10


def plot_dif_eq(function):
    fig, ax = plt.subplots()
    function = function.replace("DY", "A")
    # y0s = range(y0_min, y0_max, y0_separation)
    # for Y0 in y0s:
    #     X = 1
    #     y0 = Y0
    #     func = function.replace("Y0", str(y0))
    #     Y1 = sp.Symbol("Y1")
    #     y1 = sp.solve(eval(func), Y1)[0]
    #     y, x = [y0], [X]
    #     for _ in range(round((max - 0) / increment)):
    #         y0 += y1 * increment
    #         X = x[len(x) - 1]
    #         func = function.replace("Y0", str(y0))
    #         y1 = sp.solve(eval(func), Y1)[0]
    #         x.append(x[len(x) - 1] + increment)
    #         y.append(y0)
    #     const = (Y0 - y0_min) / (y0_max - y0_min)
    #     color = tuple(const * color1[i] + (1 - const) * color2[i] for i in range(3))
    #     plt.plot(x, y, color = color)
    # test_y = [np.e ** val for val in x]
    # ax.spines['left'].set_position('center')
    # plt.plot(x, test_y, color = "blue")

    x_dom = list(range(-5, 5, 1))
    y_dom = list(range(-5, 5, 1))
    for x in x_dom:
        for y in y_dom:
            A = sp.Symbol("A")
            slope = sp.solve(eval(function.replace("X", str(x)).replace("Y", str(y))), A)[0]
            length = (slope**2 + 1) ** 0.5
            dx = float(1 / length)
            dy = float(slope / length)
            ax.quiver(x, y, dx, dy)
    plt.show()

def plot_harmonic(function):
    function = function.replace("DDY", "A")
    fig, ax = plt.subplots()
    DY = 0
    x_dom = list(range(-5, 5, 1))
    y_dom = list(range(-10, 10, 1))
    for x in x_dom:
        for y in y_dom:
            A = sp.Symbol("A")
            slope = sp.solve(eval(function.replace("X", str(x)).replace("Y", str(y))), A)[0]
            length = (slope ** 2 + 1) ** 0.5
            dx = float(1 / length)
            dy = float(slope / length)
            ax.quiver(x, y, dx, dy)
    plt.show()

def main():
    # f = input("Enter function: ")
    f = "DDY-3*Y+2*X"
    plot_harmonic(f)

if __name__ == "__main__":
    main()