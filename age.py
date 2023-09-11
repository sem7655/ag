age = int(input())#запрашиваем возраст
if age % 5 and age % 6:
    print('года')
elif age == 1:
    print('год')
else:
    print('лет')
