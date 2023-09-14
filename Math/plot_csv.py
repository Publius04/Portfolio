import matplotlib.pyplot as plt
import csv

def plot_csv(path):
    x = []
    y = []
    with open(path) as f:
        data = csv.reader(f)
        for row in data:
            x.append(row[0])
            y.append(row[1])

    fig, ax = plt.subplots()
    plt.tick_params(axis="both", which='both', left=False, right=False, bottom=False, top=False, labelbottom=False, labelleft=False)
    plt.plot(x, y, color = "red")
    plt.show()
    


def main():
    p = input("Enter path: ")
    plot_csv(p)

if __name__ == "__main__":
    main()