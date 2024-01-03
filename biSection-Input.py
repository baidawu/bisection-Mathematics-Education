import numpy as np 
def equation(x):
#      return x - 3 + np.log(x)
# #     return x**3 + 1.1 * x**2 + 0.9 * x - 0.4
     return x+np.log(x)-3

def bisection_method_infinite(func, a, b, tolerance=1e-6):
    """
    Parameters:
    - func: 待求解的方程
    - a, b: 初始区间 [a, b]，确保在该区间内存在一个根
    - tolerance: 允许的误差范围，当区间长度小于 tolerance 时停止迭代

    Returns:
    - root: 方程的近似解
    - iterations: 实际迭代次数
    """
    if func(a) * func(b) > 0:
        raise ValueError("区间端点函数值必须异号，确保存在根")

    root = None
    iterations = 0

    print(f"Iteration\t   a\t\t  c\t\t  b\t\t  f(a)\t\t f(c)\t\t  f(b)")
    print("-" * 100)

    while (b - a) > tolerance:
        mid_point = (a + b) / 2
        fa = func(a)
        fb =func(b)
        fx = func(mid_point)

        print(f"{iterations + 1}\t\t {a:.6f}\t {mid_point:.6f}\t {b:.6f}\t {fa:.6f}\t {fx:.6f}\t {fb:.6f}")

        if fx == 0:
            root = mid_point
            break
        elif fx * func(a) < 0:
            b = mid_point
        else:
            a = mid_point

        iterations += 1
        
        user_input = input("Press Enter to continue...")

    root = (a + b) / 2

    print("-" * 100)
    print(f"方程的近似解: {root}")
    print(f"实际迭代次数: {iterations}")


bisection_method_infinite(equation, 2, 3, tolerance=0.0001)
