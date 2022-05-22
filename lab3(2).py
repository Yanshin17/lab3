#Розв'язати лінійне рівняння A · x + B = 0, задане своїми коефіцієнтами A і B (коефіцієнт A НЕ
#дорівнює 0).

def lin_eq(a, b):
    return -b / a


a = float(input("a="))
b = float(input("b="))

if abs(a) > 1.0e-15:
    print("%.4f" % lin_eq(a, b))
else:
    print("Bad a")


#Дано два ненульових числа. Знайти суму, різницю, добуток і частку їх квадратів

a = int(input("a = "))
b = int(input("b = "))
a2 = a*a
b2 = b*b
print('%d^2 + %d^2 = %d' % (a,b,a2+b2))
print('%d^2 - %d^2 = %d' % (a,b,a2-b2))
print('%d^2 * %d^2 = %d' % (a,b,a2*b2))
print('%d^2 / %d^2 = %f' % (a,b,a2/b2))
