def multi(n):
    if n == 1:
        return 1
    else:
        return n * multi(n - 1) 

a = int(input('Введите число: '))
list =[]
for i in range(1, a+1):
    list.append(multi(i))
   
print(list)
    