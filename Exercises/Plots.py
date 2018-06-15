import pylab as plb
import matplotlib.image as img
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def bar_graph():
    k = 8
    x = plb.arange(k)
    for z in x:
        y1 = plb.rand(k) * (1 - x / k)
        y2 = plb.rand(k) * (1 - x / k)
        plb.axes([0.075, 0.075, .88, .88])

        plb.bar(x, +y1, facecolor='#9922aa', edgecolor='green')
        plb.bar(x, -y2, facecolor='#ff3366', edgecolor='green')

        for a, b in zip(x, y1):
            plb.text(a+0.41, b+0.08, '%.3f' % b, ha='center', va='bottom')
        for a, b in zip(x, y2):
            plb.text(a+0.41, b+0.08, '%.3f' % b, ha='center', va='top')

        plb.xlim(-.5, k), plb.ylim(-1.12, +1.12)
        plb.grid(True)
        plb.pause(1)
        plb.cla()


def scatter_1():
    count = 5
    for x in range(count):
        x = plb.rand(1, 2, 1500)
        y = plb.rand(1, 2, 1500)
        plb.axes([0.075, 0.075, .88, .88])

        plb.cla()
        plb.scatter(x, y, s=65, alpha=.75, linewidths=.125, c=plb.arctan2(x, y))

        plb.grid(True)
        plb.xlim(-0.085, 1.085), plb.ylim(-0.085, 1.085)
        plb.pause(1)


def scatter_2():
    count = 5
    for x in range(count):
        plb.cla()
        array = plb.random((80, 120))
        plb.imshow(array, cmap=plb.cm.gist_rainbow)
        plb.pause(1)


def user_image():
    image = img.imread('/Users/jeblat/Pictures/03_Gretel.jpg')
    plt.imshow(image)
    plt.pause(1)
    luminosity = image[:, :, 0]
    plt.imshow(luminosity)
    plt.pause(1)
    plt.imshow(luminosity, cmap='hot')
    plt.pause(1)
    plt.imshow(luminosity, cmap='Spectral')
    plt.pause(1)
    plt.imshow(luminosity, cmap='Wistia')
    plt.pause(1)
    plt.imshow(luminosity, cmap='afmhot')
    plt.pause(1)
    plt.imshow(luminosity, cmap='bone')
    plt.pause(1)


def histogram_1():
    plb.figure(1)
    gaus_dist = plb.normal(-2, 2, size=512)
    plb.hist(gaus_dist, normed=True, bins=24)
    plb.title('Gaussian distribution / Histogram')
    plb.xlabel('Value')
    plb.ylabel('Frequency')
    plb.grid(True)
    plb.pause(5)


def histogram_2():
    plb.figure(2)
    gaus_dist = plb.normal(-2, 2, size=512)
    unif_dist = plb.uniform(-5, 5, size=512)
    plb.hist(unif_dist, bins=24, histtype='stepfilled', normed=True, color='cyan', label='Uniform')
    plb.hist(gaus_dist, bins=24, histtype='stepfilled', normed=True, color='orange', label='Gaussian', alpha=0.65)
    plb.legend(loc='upper right')
    plb.title('Gaussian vs Uniform distribution / Histrogram')
    plb.xlabel('Value')
    plb.ylabel('Frequency')
    plb.grid(True)
    plb.pause(5)


def pie_chart():
    plb.figure("How do we get to work")
    plb.axes([.035, 0.035, 0.9, 0.9])
    l = 'car', 'truck', 'boat', 'dingie', 'train', 'plane', 'bus', 'rocket', 'tram', 'other'
    b = plb.round_(plb.random(10), decimals=2)
    c = ['blue', 'red', 'green', 'gray', 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'cyan', 'orange']
    e = (0, 0, 0, 0, 0, 0, 0, 0.05, 0, 0)
    plb.cla()
    plb.pie(b, explode=e, labels=l, colors=c, radius=.75, autopct='%1.0f%%', shadow=True, startangle=15)
    plb.axis('equal')
    plb.xticks(()); plb.yticks(())
    plb.pause(5)


def contour_plot():
    def f(x, y):
        return (2 - x/3 + x**6 + 2.125*y) * plb.exp(-x**2, -y**2)
    n = 128
    x = plb.linspace(-2, 2, n)
    y = plb.linspace(-1, 1, n)
    a, b = plb.meshgrid(x, y)
    plb.cla()
    plb.axes([0.075, 0.075, 0.92, 0.92])
    plb.contourf(a, b, f(a, b), 12, alpha=.50, cmap=plb.cm.gist_rainbow)
    c = plb.contour(a, b, f(a, b), 8, colors='black', linewidth=.65)
    plb.clabel(c, inline=1, fontsize=14)
    plb.xticks(()); plb.yticks(())
    plb.pause(5)


def polar_plot_3d():
    plb.axes([0.065, 0.065, 0.88, 0.88], polar=True)
    q = 24
    t = plb.arange(0.015, 3*plb.pi, 3*plb.pi / q)
    rad = 12 * plb.rand(q)
    w = plb.pi / 4 * plb.rand(q)
    ba = plb.bar(t, rad, width=w)

    for r, bar in zip(rad, ba):
        bar.set_facecolor(plb.cm.jet(r/12.))
        bar.set_alpha(0.75)

        plb.pause(5)


def surface_plot():
    ax = Axes3D(plb.figure())
    x = plb.arange(-6, 3, 0.35)
    y = plb.arange(-6, 6, 0.35)
    x, y = plb.meshgrid(x, y)
    k = plb.sqrt(x**2 + y**2)
    z = plb.sin(k)

    ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=plb.cm.gist_rainbow)
    ax.contourf(x, y, z, zdir='z', offset=-3, cmap=plb.cm.gist_stern)
    ax.set_zlim(-4, 4)
    plb.pause(5)

'''

Function runners below

'''
# bar_graph()
# scatter_1()
# scatter_2()
# user_image()
# histogram_1()
# histogram_2()
# pie_chart()
# contour_plot()
# polar_plot_3d()
# surface_plot()