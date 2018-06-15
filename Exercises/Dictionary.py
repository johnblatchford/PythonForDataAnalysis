import pylab as plb

a = {'key1': None, 'key2': None, 'key3': None, 'key4': None, 'key5': None}


def random_values(x):
    for key, value in x.items():
        num = plb.randint(0, 10)
        x[key] = num
    return x


b = random_values(a)


def swap_values(x):
    s = plb.normal(2, 3, 256)
    for key, value in x.items():
        if x[key] < 5:
            x[key] = s
    return x


c = swap_values(b)


def plot_dict(x):
    for key, array in x.items():
        plb.figure(1)
        plb.hist(array, bins=12, histtype='stepfilled', normed=True, color='cyan', label='Uniform')
        plb.title('Lecture 6 Exercise - histogram')
        plb.xlabel('x label')
        plb.ylabel('y label')
        plb.legend(loc='best')
        plb.grid(True)
        plb.pause(1)


plot_dict(c)