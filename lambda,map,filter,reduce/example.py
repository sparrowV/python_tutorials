
# example1
def power(a,b):
    return a**b
print((lambda a,b : a**b)(2,3))
power_func = lambda a,b : a**b
print(power_func(2,5))

# example2
def func(num_of_iteration,add_func):
    for i in range(num_of_iteration):
        print(i,add_func(i,i))


func(5,lambda x,y:x+y)


# example3 - filter
num_list = [12,45,2,6,90,56,13,17]
filtered_list = list(filter(lambda x : x>20,num_list))
print(filtered_list)

#example4-map
num_list = [2,6,9,11,13]
mapped_list = list(map(lambda x:x+2,num_list))
print(mapped_list)


#example5-reduce
import functools
num_list = [1,2,3,4,5]
res = functools.reduce((lambda x,y:x*y),num_list)
print(res)

#example6-reduce
import functools
num_list = [1,2,3,4,5]
res = functools.reduce((lambda x,y:x*y),num_list,10)
print(res)


#example7 map-filter
num_list = [2,5,4,7,8,3]
res = list(filter(lambda x:x<20,list(map(lambda x:x**2,num_list))))
print(res)


#example 8 map-filter-reduce
num_list = [2,5,4,7,8,3]
res = functools.reduce(lambda x,y:x+y,list(filter(lambda x:x<20,list(map(lambda x:x**2,num_list)))))
print(res)