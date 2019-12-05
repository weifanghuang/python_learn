import matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [pow(x, 3) for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Greens, s=0.2)

# Setting icon title and add labels to the axis
plt.title("Cube Numbers", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# Setting the size of tick marks
plt.tick_params(axis='both', which='major', labelsize=14)

# Setting the value range of the coordinate axis
plt.axis([0, 5100, 0, 125000000100])

plt.show()
