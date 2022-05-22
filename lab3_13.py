#Дані координати двох протилежних вершин прямокутника: (x1, y1), (x2, y2). Сторони
#прямокутника паралельні до осів координат. Знайти периметр і площу даного прямокутника

var
    n2, i, n: integer;

begin
    readln(n);
    n2 := 0;
    for i := 1 to n do
    begin
        n2 := n2 + 2 * i - 1;
        writeln(i, ' ', n2);
    end;
end.


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


