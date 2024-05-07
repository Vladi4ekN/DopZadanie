def treug_(a, b, c):
    if a == b == c:
        return("Равносторонний")
    if a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return("Разносторонний")
a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))
treug_type = treug_(a, b, c)
print("Треугольник является", treug_type)