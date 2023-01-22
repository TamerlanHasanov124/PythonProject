import functools

def my_map(func, iterable):
     res = list()

     for i in iterable:
         res.append(func(i))
     return iter(res)


def my_filter(function, iterable):
     res = list()
     for i in iterable:
         if function(i):
             res.append(i)
     return iter(res)


def longest(longest, currentWord):
    if len(currentWord) > len(longest):
       return currentWord
    else:
       return longest


def my_reduce(function, iterable):
     it = iter(iterable)
     value = next(it)
     for element in it:
         value = function(value, element)
     return value


names = ["John", "Jane", "Jake","Jeremy","John","Jill","Jeremiah"]

lengths = my_map(lambda x: len(x), names)
print(f"MAP STEP: {list(lengths)}")

filter = my_filter(lambda x: len(x) > 5, names)
print(f"REDUCE STEP: {list(filter)}")

reduce = my_reduce(longest, names)
print(str(reduce))