#return function from another function
# def outer():
#     def inner():
#         print("in inner")
#
#     return inner
#
#
# outer()()

# assign function to a variable
# def outer():
#     def inner():
#         print("in inner")
#
#     return inner
#
#
# inner_func = outer()
# inner_func()


# def outer(param):
#     def inner():
#         print("in inner",param)
#
#     return inner
#
#
# inner_func = outer("this is outers param")
# inner_func()
# inner_func2 = outer("another param")
# inner_func2()


# def outer(param):
#     def inner(inner_param):
#         print("outer param",param)
#         print("inner param",inner_param)
#
#     return inner
#
#
# inner_func = outer("this is outers param")
# inner_func("this is inner param")
# inner_func("this is another inner param")


# def division(a,b):
#     return a/b
#
# def test(first,second,passed_func):
#     print(passed_func(first,second))
#
#
# test(10,5,division)




