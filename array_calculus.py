import numpy as np
import matplotlib.pyplot as plt

def gradient(x):
    """
    Computes the differential operator for a given set of points x. 
    """
    len(x)=b
    dx = x[1] - x[0]
    ax = ((np.tri(b, b, 0 , dtype=int) - np.tri(b, b, 1,dtype=int)))
    ax= ax + (np.tri(b, b, -1, dtype=int ) - np.tri(b, b, -2, dtype=int))
    ax= ax / (2*dx)
    ax[0][0]    = -1 / dx  #b=newgradient
    ax[1][0]    = 1 / dx
    ax[-1][-1]  = 1 / dx
    ax[-2][-1]  = -1 / dx
    return b

def x():
    """Plots x^2"""
    x = np.arange(7)
    fx = x**2
    fp = gradient(f)

    graph = plt.axes()

    graph.plot(x, fx, label="f(x)")
    graph.plot(x, fp, color="Red", label="f`(x)")
    title = "$x^{}2}$"
    plt.title(title.format("f(x)","f`(x)")) 
    plt.xlim()
    plt.ylim()
    plt.xlabel("x")
    plt.ylabel("y")
    a.legend()
    plt.show()
    
    
def sinx():
    """Plots sin(x)"""
    x = np.arange(8)
    s = np.sin(x)
    sp = gradient(s)

    graph1 = plt.axes()
    plt.xlabel=("x")
    plt.ylabel=("y")
    plt.title=("sin(x)")

    graph1.plot(x, s, label="s(x)")
    graph1.plot(x, sp, color="Red", label="s'(x)")

    graph1.legend()
    plt.show()

def plot(x, f, Name, gradient):
    """
    Graphs a given function    """

    ft = plt.figure(figsize=(16,9))
    axis = plt.axis()
    funcGen = np.vectorize(f)
    y = funcGen(x)
    grad = gradient(x)
    plt.xlim()
    plt.ylim()
    plt.xlabel("x")
    plt.ylabel("y")
    title = 'laber {},label {}'
    plt.title(title.format("$f(x) = $" + Name,"$Df(x)=$" +gradient)) 

    axis.legend()

    plt.show()

