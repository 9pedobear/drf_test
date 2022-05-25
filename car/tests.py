from django.test import TestCase

def mathematic(a, b, c):
    if c == '+':
        return a + b
    if c == '-':
        return a - b
    if c == '*':
        return a * b
    if c == '/':
        return a / b

# def test():
#     assert mathematic(1, 2, '+') == 4
#     return 'Тест пройден'
# print(test())

# class MathematicTestCase(TestCase):
#     def test_plus(self):
#         result = mathematic(1, 2, '+')
#         self.assertEqual(3, result)
#     def test_minus(self):
#         result = mathematic(1, 2, '-')
#         self.assertEqual(-1, result)
#     def test_multiply(self):
#         result = mathematic(1, 2, '*')
#         self.assertEqual(2, result)
#     def test_division(self):
#         result = mathematic(2, 2, '/')
#         self.assertEqual(0.5, result)










