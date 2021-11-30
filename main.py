from sympy import sympify
from RungeKutta import RungeKutta
from colorama import init, Fore, Style


def titulo():
    init()
    print(Fore.YELLOW + Style.BRIGHT + """
______                              _   __      _   _        
| ___ \                            | | / /     | | | |       
| |_/ /   _ _ __   __ _  ___ ______| |/ / _   _| |_| |_ __ _ 
|    / | | | '_ \ / _` |/ _ \______|    \| | | | __| __/ _` |
| |\ \ |_| | | | | (_| |  __/      | |\  \ |_| | |_| || (_| |
\_| \_\__,_|_| |_|\__, |\___|      \_| \_/\__,_|\__|\__\__,_|
                   __/ |                                     
                  |___/                                      
                                            By: Jossefrp
""")
    print(Style.RESET_ALL)


def main():
    x0 = sympify(input("Ingrese el x0: "))
    xf = sympify(input("Ingrese el xf: "))
    y0 = sympify(input("Ingrese el y0: "))
    h = sympify(input("Ingrese el paso: "))
    f = sympify(input("Ingrese la función: "))
    solucion = RungeKutta(x0, xf, y0, h, f)
    print("\nIngresar la forma de aproximar:\n1. Runge-Kutta(2)\n2. Runge-Kutta(3)\n3. Runge-Kutta(4)")
    opc = int(input("--> "))
    if opc == 1:
        solucion.rk2()
    elif opc == 2:
        solucion.rk3()
    elif opc == 3:
        solucion.rk4()
    else:
        print("Elija una opción correcta")
        raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        titulo()
        main()
    except KeyboardInterrupt:
        print("Salida forzosa")
    finally:
        input("\nEnter para salir")
