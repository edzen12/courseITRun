# циклы for  и  while

# print(" hello world "*10)
# print(" hello world ")
# print(" hello world ")
# print(" hello world ")
nList = []
for i in range(1, 11):
    print(i,'hello world') 
    nList.append(i)
print(nList)
# итерация
# j = 'Никита'
# n = ['Нурбек', "Никита", "Жи","Матай", 'Milena']
# for i in n:
#     if i == j:
#         print(i)
allFruits = ['Банан', "киви", "Мандарин", "апельсин","яблоко", "манго","виноград"]
myFavoriteFruits = ['Мандарин', "Банан"]
for i in allFruits:
    if i in myFavoriteFruits:
        print(i, 'люблю')
    else:
        print(i, 'не люблю')
        
 

# i = 1
# while i <= 10:
#     print('Hello Misha') 
#     i+=1 # i = i + 1