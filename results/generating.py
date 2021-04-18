import matplotlib.pyplot as plt

loss_values = [4.6746, 3.5598, 2.7099, 2.1895, 1.8851, 1.5989, 1.3672, 1.2257, 1.0509, 0.9267, 0.8131,
               0.7378, 0.6291, 0.5565, 0.4915, 0.4531, 0.3965, 0.3634, 0.3212, 0.2908]
epochs = [i for i in range(20)]

plt.plot(epochs, loss_values)
plt.xlim(0, 20)
plt.ylim(0, 5)
plt.title('Loss function in text generating network')
plt.xlabel("epochs")
plt.ylabel("loss")
plt.show()