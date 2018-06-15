"""
John Blatchford - listening@mac.com

"""


def lecture_5_exercise():
    #  Work with only these imports:
    from numpy import matrix, array, random, min, max
    import pylab as plb
    print('''\n
    only using imports:
    from numpy import matrix, array, random, min, max
    import pylab as plb\n''')

    print('Part #1: Create the Data\n')
    #  Create a list A of 600 random numbers bound between [0:10)
    a = list(random.random(600)*10)
    print('Create a list A of 600 random numbers bound between [0:10):\n{0}\n'.format(a))

    #  Create an array B with with 500 elements bound in the range [-3*pi:2*pi]
    b = plb.linspace(3*plb.pi, 2*plb.pi, 500, endpoint=True)
    print('Create an array B with with 500 elements bound in the range [-3*pi:2*pi]:\n{0}\n'.format(b))

    #  Using if, for or while, create a func4on that overwrites every element in A that falls outside of the interval [2:9)
    print('''\n
    Using if, for or while, create a func4on that overwrites every element in A that falls outside of the interval [2:9)
    overwrite that element with the average between the smallest and largest element in A
    Normalize each list element to be bound between [0:0.1]

    def replace_values(x):
        avg = (min(x) + max(x)) / 2
        for i in x:
            if i < 2 or i > 9:
                x[i] = avg
        x = [(float(y)/max(x) * 0.1) for y in x]
        return x\n''')

    def replace_values(x):
        for index, val in enumerate(x, start=0):
            if val < 2 or val > 9:
                #  overwrite that element with the average between the smallest and largest element in A
                x[index] = (min(x) + max(x)) / 2
                #  Normalize each list element to be bound between [0:0.1]
            x[index] = x[index] / 10
        return x

    #  Return the result from the function to C
    c = replace_values(a)
    print('Return the result from the function to C:\n{0}\n'.format(c))

    #  Cast C as an array
    c = array(c)
    print('Cast C as an array\n')
    print('Type of c: {0}'.format(type(c)))

    #  Add C to B (think of C as noise) and record the result in D
    d = c[0:len(b)] + b
    print('Add C to B (think of C as noise) and record the result in D:\n{0}\n'.format(d))

    print('Part #2: Plotting\n')

    #  Create a figure, give it a title and specify your own size and dpi
    fig = plb.figure(figsize=(6, 5), dpi=160)
    fig.canvas.set_window_title('Lecture 5 Class Exercise')

    #  Plot the sin of D, in the (2,1,1) location of the figure
    plb.subplot(2, 1, 1)
    plb.plot(d, plb.sin(d), color="green", linewidth=.5, linestyle='-', label='sin curve')

    #  Overlay a plot of cos using D, with different color, thickness and type of line
    plb.plot(d, plb.cos(d), color="grey", linewidth=.5, linestyle="--", label='cos line')

    #  Create some space on top and bottom of the plot (on the y axis) and show the grid
    plb.ylim(plb.sin(d).min() - 1, plb.sin(d).max() + 1)
    plb.grid()

    #  Specify the following: Title, Y-axis label and legend to fit in the best way
    plb.legend(loc='upper right')
    plb.ylabel('Fig 1', fontsize=10)
    plb.title('D sin & cos')

    #  Plot the tan of D, in location (2,1,2) with grid showing, X-axis label, Y-axis label
    # and legend on top right
    plb.subplot(2, 1, 2)
    plb.plot(d, plb.tan(d), color='cyan', linewidth=0.5, label='tan line')
    plb.grid()
    plb.xlabel('label for x axis', fontsize=8)
    plb.ylabel('Fig 2', fontsize=9, )
    plb.legend(loc='upper left')

    #  Organize your code: use each line from this HW as a comment line before coding each step
    #  Save these steps in a .py file and email it to me before next class. I will run it!
    plb.show()


lecture_5_exercise()