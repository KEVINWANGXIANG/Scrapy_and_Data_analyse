from pylab import *
import numpy as np
import matplotlib.pylab as pyl
#创建等差数列
'''
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
pyl.plot(X, C, color="blue", alpha=1.00, linewidth=1.0, linestyle="-.", label="cosine")
pyl.plot(X, S, color="red", alpha=1.00, linewidth=1.0, linestyle="-.", label="sine")
xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, -np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$'])
yticks([-1, 0, 1],
       [r'$-1$', r'$0$', r'$+1$'])
# legend(loc='upper right')
# pyl.xlim(-4.0, 4.0)
# pyl.ylim(-1.0, 1.0)
# pyl.show()
'''

'''
print("---------------------散点图----------------------")
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
pyl.scatter(X, Y)
pyl.show()
'''

'''
print("----------------------条形图----------------------")
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

pyl.bar(X, +Y1, facecolor="blue", edgecolor='white')
pyl.bar(X, -Y2, facecolor="red", edgecolor="white")
for x, y in zip(X, Y1):
    text(x + 0.05, y + 0.05, '%.2f' % y, ha="center", va="bottom")
for x, y in zip(X, Y2):
    text(x + 0.05, -y - 0.05, '%.2f' % y, ha="center", va="top")
pyl.ylim(-1.25, +1.25)
pyl.show()
'''

'''
print("----------------------等高线图----------------------")
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
C = contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
pyl.show()
'''

'''
print("------------------灰度图---------------------")
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
imshow(f(X, Y)), show()
'''

'''
print("---------------------饼状图------------------------")
n = 20
Z = np.random.uniform(0, 1, n)
pie(Z), show()
'''

'''
print("-------------------网格---------------------")
axes = gca()
axes.set_xlim(0, 4)
axes.set_ylim(0, 3)
axes.set_xticklabels([])
axes.set_yticklabels([])
pyl.show()
'''

'''
print("----------------------极轴图--------------------")
axes([0, 0, 1, 1])
N = 20
theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(cm.jet(r / 10.))
    bar.set_alpha(0.5)
show()
'''

'''
print("--------------------图中图------------------")
fig = pyl.figure(figsize=(10, 6))
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
#大图
left, bottom, width, weight = 0.1, 0.1, 0.8, 0.8
ax1 = fig.add_axes([left, bottom, width, weight])
ax1.plot(x, y, 'r')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$xxInterestingxx$')
#左上小图
left, bottom, width, weight = 0.2, 0.6, 0.25, 0.25
ax1 = fig.add_axes([left, bottom, width, weight])
ax1.plot(y, x, 'r')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$title\ inside \$')

#右下小图
left, bottom, width, weight = 0.6, 0.2, 0.25, 0.25
ax1 = fig.add_axes([left, bottom, width, weight])
ax1.plot(y[::-1], x, 'r')
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$title\ inside \$')
pyl.show()
'''

print("---------------------Animation动画-------------------")
from matplotlib import animation
fig, ax = pyl.subplots()
x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
def animate(i):
    line.set_ydata(np.sin(x + i / 100))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)
pyl.show()





















































