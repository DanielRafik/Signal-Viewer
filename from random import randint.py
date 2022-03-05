from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
x = []
y = []
fig, ax = plt.subplots()
def animate(i):
    pt = randint(1,9) # grab a random integer to be the next y-value in the animation
    x.append(i)
    y.append(pt)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,20])
    ax.set_ylim([0,10])
anim = FuncAnimation(fig, animate, frames=60, interval=90, repeat=False)

plt.show()