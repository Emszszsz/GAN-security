import matplotlib.pyplot as plt

loss_values = [4.6746, 3.5598, 2.7099, 2.1895, 1.8851, 1.5989, 1.3672, 1.2257, 1.0509, 0.9267, 0.8131,
               0.7378, 0.6291, 0.5565, 0.4915, 0.4531, 0.3965, 0.3634, 0.3212, 0.2908]
epochs = [i for i in range(20)]

loss_values = [4.6727, 3.5110, 2.6576, 2.1764, 1.8363, 1.6110, 1.3768, 1.2197, 1.0462, 0.9192]
epochs = [i for i in range(10)]


loss_values = [4.7790, 3.6358, 2.7211, 2.2344,
1.9192, 1.6764, 1.4765, 1.2542,
1.1116, 0.9942, 0.8643, 0.7487,
0.6614, 0.6101, 0.5372, 0.4647,
0.4149, 0.3764, 0.3342, 0.3065]
epochs = [i for i in range(20)]

loss_values = [4.7840, 3.6616, 2.7529, 2.2899, 1.9849, 1.7047, 1.4723, 1.2620, 1.1316, 0.9975]
epochs = [i for i in range(10)]

plt.plot(epochs, loss_values)
plt.xlim(0, 10)
plt.ylim(0, 5)
plt.title('Loss function in text generating network fourth training')
plt.xlabel("epochs")
plt.ylabel("loss")
plt.show()


