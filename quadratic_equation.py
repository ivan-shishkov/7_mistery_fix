from math import sqrt


def get_roots(a, b, c):
    """Solves a quadratic equation.

    This function solves a quadratic equation having the form
    a*x*x + b*x + c = 0

    Positional arguments:
    a -- the quadratic coefficient of the equation
    b -- the linear coefficient of the equation
    c -- the constant of the equation

    Function returns 2-element tuple with the roots of the equation.

    Return value depends from discriminant's value:
    (None, None) if discriminant less than 0
    (root1, None) if discriminant is equal to 0
    (root1, root2) if discriminant great than 0
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None, None

    root1 = (-b - sqrt(discriminant)) / (2 * a)
    root2 = (-b + sqrt(discriminant)) / (2 * a)

    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
