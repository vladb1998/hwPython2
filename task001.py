a =int(input('Введите число: '))
sum = 0
while a > 0 :
    sum += a % 10
    a //= 10
print(f' Сумма цифр = {sum}')

    

