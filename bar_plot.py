import pylab as plb

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