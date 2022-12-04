# list=[]
# list.append(12)
# print(list)
# #how to create list of 1000 numbers
# for num in range(1,1001):
#     list.append(num)
# print('list', list)
# # to find the length
# print("this is length",len(list),)
# #to check two list are same or not
# list1=[1,2,'eqw','qwe']
# list2=[1,2,'eqw','qwe']
# print ('list are equal or not : ',
#       list1==list2 )
# # how to print all the all elements of list
# list4=[3,4,2.3,4.2,45,.45,342]
# for num in list4:
#     print(num)
# to print list element
# print("the second numbeer is ",list4[2])
# how to print using len function
# for index in range(0,len(list4)):
#     print(list4[index])
# differrence bw append and extend
# list3 = [2, 3.4, 45.6, .342, 3, 5]
# list5 = [32, 45, 5, 6, 7, 89, 9]
# list3.append(list5)
# result = list3
# print(list3)

# Extend function
list11 = [21, 23, 4, 34, 5, 42, 4, 3, 4, 5]
list12 = [3, 234,  54.23, 2]

# list11.extend(list12)
# print(list11)

# to slice the list
# print(list11[2:8] )
# print(list11[0:] )

# now for step increment third
# print(list11[2:8:2])
# print(list11[8:1:2])
# print(list11[8:1:-2])

# print(list11[0::2])

# # /to print the last and second last element 
# print(list11[len(list11)-1])
# # or second way
# print(list11[-1])
# print(len(list11)-1)

print(list11[-1::-1])