from sympy import *
from colorama import init, Fore, Style


class RungeKutta:
    x = Symbol("x")
    y = Symbol("y")
    init()

    def __init__(self, x0=0, xf=0, y0=0, h=0, f=sympify(0)):
        self._x0 = x0
        self._xf = xf
        self._y0 = y0
        self._h = h
        self._n = (xf - x0)/h
        self._f = sympify(f)

    @property
    def x0(self):
        return self._x0

    @x0.setter
    def x0(self, x0):
        self._x0 = x0

    @property
    def xf(self):
        return self._xf

    @xf.setter
    def xf(self, xf):
        self._xf = xf

    @property
    def y0(self):
        return self._y0

    @y0.setter
    def y0(self, y0):
        self._x0 = y0

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, h):
        self._h = h

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, f):
        self._f = f

    def rk2(self):
        fun = lambda x0, xf: self._f.evalf(8, subs={RungeKutta.x: x0, RungeKutta.y: xf})
        x, y = self._x0, self._y0
        for i in range(int(self._n)):
            k1 = fun(x, y)
            x = x + self._h
            k2 = fun(x, y + self._h*k1)
            y = y + self._h/2 * (k1 + k2)
            print(f"n = {i + 1} x = {round(x, 4)}, y = {round(y, 8)}")
        print(Fore.RED + Style.BRIGHT + "\nR-K(2) = ", round(y, 8))
        print(Style.RESET_ALL)

    def rk3(self):
        fun = lambda x0, xf: self._f.evalf(8, subs={RungeKutta.x: x0, RungeKutta.y: xf})
        x, y = self._x0, self._y0
        for i in range(int(self._n)):
            k1 = fun(x, y)
            k2 = fun(x + self._h/2, y + self._h/2 * k1)
            x += self._h
            k3 = fun(x, y + self._h*(2*k2 - k1))
            y += self._h/6 * (k1 + 4*k2 + k3)
            print(f"n = {i + 1} x = {round(x, 4)}, y = {round(y, 8)}")
        print(Fore.RED + Style.BRIGHT + "\nR-K(3) = ", round(y, 8))
        print(Style.RESET_ALL)

    def rk4(self):
        fun = lambda x0, xf: self._f.evalf(8, subs={RungeKutta.x: x0, RungeKutta.y: xf})
        x, y = self._x0, self._y0
        for i in range(int(self._n)):
            k1 = fun(x, y)
            k2 = fun(x + self._h/2, y + self._h/2 * k1)
            k3 = fun(x + self._h/2, y + self._h/2 * k2)
            x += self._h
            k4 = fun(x, y + self._h*k3)
            y += self._h/6 * (k1 + 2*k2 + 2*k3 + k4)
            print(f"n = {i + 1} x = {round(x, 4)}, y = {round(y, 8)}")
        print(Fore.RED + Style.BRIGHT + "\nR-K(4) = ", round(y, 8))
        print(Style.RESET_ALL)
