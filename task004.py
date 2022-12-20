a = int(input('введите число : '))
list1 = []
for i in range(-a, a+1):
    list1.append(i)

position1 = int (input ('Введите первую позицию: '))
position2 = int (input ('Введите вторую позицию: '))
list2= [position1 , position2]
print(list1)
print(list2)
print (f'Сумма элементов на указанных позициях = {list1[position1] * list1[position2]}')