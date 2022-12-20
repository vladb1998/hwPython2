a = int(input('Введите число: '))
list =[]
for i in range(1, a+1):
    list.append(round(((1+(1/i))**i), 3))
   
print(list)