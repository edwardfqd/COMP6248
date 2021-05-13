import matplotlib.pyplot as plt

x=[1,10,15]

cifar10=[28.09,45.23,47.64]
cifar10shang=[29.25,45.57,47.67]
cifar10xia=[26.92,44.66,47.5]

fashion=[70.47,82.55,82.68]
fashions = [71.34,82.8,82.8]
fashionx = [69.93,82.28,82.5]

svhn = [31.15,76.12,78.2]
svhns = [33.79,77.23,78.9]
svhnx = [29.1,75.5,78]

mnist = [91.94,97.25,97.78]
mnists = [92.46,97.5,97.8]
mnistx = [90.79,97.1,97.6]


plt.figure(figsize=(8,8), dpi=80)
plt.figure(1)
ax1 = plt.subplot(221)
ax1.plot(x, mnist, color="r",linestyle = "-",label = "MNIST")
ax1.fill_between(x, mnists, mnistx,
        facecolor='red',
        edgecolor='red',
        alpha=0.3)
ax1.legend()

ax2 = plt.subplot(222)
ax2.plot(x, fashion,color="r",linestyle = "-",label = "FashionMNIST")
ax2.fill_between(x, fashions, fashionx,
        facecolor='red',
        edgecolor='red',
        alpha=0.3)
ax2.legend()

ax3 = plt.subplot(223)
ax3.plot(x, svhn,color="r",linestyle = "-",label="SVHN")
ax3.fill_between(x, svhns, svhnx,
        facecolor='red',
        edgecolor='red',
        alpha=0.3)
ax3.legend()

ax4 = plt.subplot(224)
ax4.plot(x, cifar10,color="r",linestyle = "-",label="CIFAR10")
ax4.fill_between(x, cifar10shang, cifar10xia,
        facecolor='red',
        edgecolor='red',
        alpha=0.3)
ax4.legend()

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
plt.show