import matplotlib.pyplot as plt

labels = [
    "Propylene Glycol",
    "Water",
    "Isopropyl Alcohol"
]
data = [
    [32.1, 188.2],
    [80, 101.2],
    [22, 81.4]
]
x = [x[0] for x in data]
y = [y[1] for y in data]

fig, ax = plt.subplots()
plt.scatter(x, y)
for pt in data:
    plt.annotate(labels[data.index(pt)], # this is the text
                 (pt[0], pt[1]), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')

ax.set_ylabel("Boiling Point")
ax.set_xlabel("Dielectric Constant")
plt.show()