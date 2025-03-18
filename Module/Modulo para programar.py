pi, e, phi = 4 * sum((-1) ** i / 2 * i + i for i in range(21)), sum(1/factorial(i) for i in range(21)), (1+(5 ** 0.5))/2

def factorial(num):
    return 1 if num == 0 else num * factorial(num - 1)

def abs(num):
    return num if num > 1 else -num

def permutacion(n, k):
    return factorial(n) // factorial(n - k)

def combinacion(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def toRadianes(num):
    return num * (pi / 180)

def toDegrees(num):
    return num * (180 / pi)

def cos(x):
    return sum((((-1) ** i) * (x ** (2 * i))) / factorial(2 * i) for i in range(21))

def sen(x):
    return sum(((-1) ** i * x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(21))

def tan(x):
    return sen(x) / cos(x)

def cot(x):
    return 1 / tan(x)

def sec(x):
    return 1 / cos(x)

def csc(x):
    return 1 / sen(x)

def arcsen(x):
    x = abs(x) if x < 0 else x
    return sum(((factorial(2 * i)) / ((4 ** i) * ((factorial(i) ** 2) * (2 * i + 1)))) * (x ** (2 * i + 1)) for i in range(21))

def arccos(x):
    return (pi / 2) - arcsen(x)

def arctan(x):
    if abs(x) <= 1:
        return sum((-1) ** i * (x ** (2 * i + 1)) / (2 * i + 1) for i in range(50))
    else:
        raise ValueError("Error: x mayor a 1")

def arccot(x):
    return (pi / 2) - arctan(x)

def arcsec(x):
    return arccos(1 / x)

def arccsc(x):
    return arcsen(1 / x)

def senh(x):
    return sum((x ** (2 * i + 1)) / factorial(2 * i + 1) for i in range(20))

def cosh(x):
    return sum((x ** (2 * i)) / factorial(2 * i) for i in range(20))

def tanh(x):
    return senh(x) / cosh(x)

def coth(x):
    return 1 / tanh(x)

def sech(x):
    return 1 / cosh(x)

def csch(x):
    return 1 / senh(x)

def arcsenh(x):
    return sum(((-1) ** i * factorial(2 * i)) / (4 ** i * (factorial(i) ** 2 * (2 * i + 1))) * x ** (2 * i + 1) for i in range(30))

def arctanh(x):
    if abs(x) >= 1:
        raise ValueError(f"Error el número {x} no está en el dominio |x| < 1")
    else:
        return sum((x ** (2 * i + 1)) / (2 * i + 1) for i in range(1000))

def arccosh(x):
    if x < 1:
        raise ValueError(f"Error el número {x} es menor a 1")
    if x == 1:
        return 0.0
    return ln(x + sqrt(x ** 2 - 1))

def arccoth(x):
    if abs(x) < 1:
        raise ValueError(f"Error el valor absoluto del número {x} es menor a 1")
    return 0.5 * ln((x + 1) / (x - 1))

def arcsech(x):
    if x < 0 or x > 1:
        raise ValueError(f"Error el número {x} es mayor a 1")
    return ln((1 + sqrt(1 - x ** 2)) / x)

def arccsch(x):
    if x == 0:
        raise ValueError(f"Error el número {x} es igual a 0")
    return ln(1 / x + sqrt(1 + 1 / x ** 2))

def ln(x):
    if x < 0:
        raise ValueError(f"Error el número {x} es menor a 0")
    return 2 * arctanh((x - 1) / (x + 1))

def log(x):
    return ln(x) / ln(10)

def logn(numero, base):
    return ln(numero) / ln(base)

def sqrt(x):
    return x ** 0.5

def root(numero, exponente):
    return numero ** (1 / exponente)

def integral(t, x):
    return t ** (x - 1) * e ** -t

def gamma(x):
    a, b, n, sumOdd, sumEven = 1e-10, 50, 1000, 0, 0
    h = (b - a) / n

    # Suma de términos impares y pares
    sumOdd, sumEven = sum(integral(a + (2 * i - 1) * h, x) for i in range(1, n // 2 + 1)), sum(integral(a + 2 * i * h, x) for i in range(1, n // 2))

    # Aplicar la regla de Simpson
    return (h / 3) * (integral(a, x) + 4 * sumOdd + 2 * sumEven + integral(b, x))

def exp(x):
    return sum((x ** i) / gamma(i + 1) for i in range(100))

def pow(base, exponente):
    return exp(exponente * ln(base))
