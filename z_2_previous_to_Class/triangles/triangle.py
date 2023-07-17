# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

class Triangle:
    
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c
    
    def triangle_check(self):
        a = self.a
        b = self.b
        c = self.c
        if a < b + c and b < a + c and c < a + b:
            print("Такой треугольник существует", end=" ")
            if a==b==c:
                print("и он равносторонний.")
            elif a == b or a == c or b == c:
                print("и он равнобедренный.")
            else:
                print("и он разносторонний.")
        else:
            print("Такого треугольника не существует.")