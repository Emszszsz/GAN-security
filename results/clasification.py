import matplotlib.pyplot as plt

loss_values = [0.00010172255050429571, 7.508795025874849e-05, 6.258381612963546e-05,
               5.490780788673341e-05, 4.956955575738186e-05, 4.557509409299298e-05,
               4.243798772478613e-05, 3.98879189569267e-05, 3.7760904966459616e-05,
               3.595084922732471e-05]
iterations = [i for i in range(10)]

plt.plot(iterations, loss_values)
plt.xlim(0, 10)
#plt.ylim(0, 1)
plt.title('Loss function in text classification network')
plt.xlabel("iterations")
plt.ylabel("loss")
plt.show()