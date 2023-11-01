# Filter function--------------------
# def isprime(num):
#     for i in range(2,num):
#         if num%i == 0:
#             return False
#         return True

# nums = [1,2,4,5,6,7,8,9]
# primes = list(filter(isprime,nums))
# print(primes)
# ------------------------------------

# dictionary-methods

dict = {"name":"aditya"}

# a = dict.fromkeys(["a1"],0)
# a = dict.get('age')
# a = dict.items()
# for key,value in a:
#     print(key,value)  

# a = list(dict.keys())

# a= dict.pop('age')
# print(dict)

a = dict.setdefault('age',21)
print(dict)

dict.update({'name':"acchint"})
dict.update({'color':"white"})

b = list(dict.values())
print(b)

print(dict)

