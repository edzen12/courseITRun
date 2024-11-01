# import index10
# from index10 import calc 

# # print(index10.calc(10, 5, '-'))
# print(calc(10, 8, '-'))

my_list = [1, 2, 3, 4, 5,6,7,8,9]
print(my_list[::-1])
# start end step 

my_list1 = ['cde', 'fgh', 'abc', 'klm', 'opq']
my_list1.sort()
print(my_list1)


# dict - словарь
contacts = {
    'gena': 7717774444,
    'katya': 4557774444,
} 
# set - множество, удаляет повторяющиеся элементы, нет индексов
contact1 = {'gena', 'masha', 'dasha', 'dasha', 'sasha'}
print(contact1)
print(contacts)


# for while - цикл - итерация - прохождение по объекту
for i in contact1:
    print(i)


print(max(my_list))


def calc():
    n1 = int(input())
    n1 = int(input())
    sim1 = input()

# calc()


n = [1,2,3,4,5,6,7,8,9]
new_n = []
for i in n: 
    if i < 5:
        new_n.append('0')
    elif i >= 5:
        new_n.append('1')
print(new_n)


lst = [14, 7, 2]
str1 = 'то что надо или надо будет {2}{1}{2}{0}'.format(lst[0], lst[1], lst[2])
print(str1)

x = [1,2,3]
print(x in x)

lst = []
lst.append(5)
print(lst)


for i in range(0,16, 4):
    print(i)

f = 'AnyText'
print(f[-1::])

r = 1
for i in range(4):
    r*=i
print(r)

a = [2,1,2,4]
a[1:].remove(2)
print(sum(a))

asi= 'hello'
asi = asi.upper()
print(asi)

g = [1,2,3,2]
j = {1,2,3,2}
print(set(g) == j)
print(g == list(j))

nums = ['one', 'two', 'three', 'four']
numdict = {x[0]: x for x in nums}
print(numdict)