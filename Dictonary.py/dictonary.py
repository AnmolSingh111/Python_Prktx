# dictonary datastructure is like object or json format

# dict1={'key':value}
dict1 = {}
dict1['ad'] = 11
# dict1['ss']=11
# dict1['ad']=11
# print(dict1)
# dict2={
#     'name':'anmol','pind':'Gholowal','province':'Changar','pincode':174101
# }
# dict1['other stuff']=dict2
print(dict1['ad'])
# how to use dictonary as list
# dict1['22']={"asddsa"}
print(dict1)
dict1['skills'] = {"python": 'js', 'gg': 'hh'}
dict1['khabar'] = {'Eyecolor': 'black', 'nationality': 'Indian'}
dict1['list'] = ['j', '322']

print(dict1['list'][1])
print(dict1['skills']['gg'])
# new_list=dict1['details']
# print(new_list[1]) ->this cant be done with object literal
# if u want to access elements from new list ->
print(dict1['khabar']['nationality'])
# to get the keys of dictonary
all_keys = dict1.keys()
print('To get all the keys of one dictonary -', all_keys)
# to get the keys of further one key

keys = dict1['khabar'].keys()
print('keys of khabar - ', keys)
# to get the values of dictonary
values = dict1.values()
print(values)

# Looping in dictonary

for k,v in dict1.items():
    print('key is ', k ,'and value is ', v)
# how to delete specific key value pair in dictonary
print(dict1)
# del dict1['khabar']
print(dict1)
dict1[32]=32
print(dict1)
del dict1[32]
print(dict1)

# how to check key exist or not 
# print(dict1.has_key(32))
# print(dict1.has_key('khabar')) depreceated

# to check the value
print(dict1.get('khabar'))




