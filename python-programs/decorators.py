def decorate(*args):

    def wrapper(func):

        def inner(x, y):

            # def add(x, y): return x + y
            # def sub(x, y): return x - y
            # def mul(x, y): return x * y
            # def div(x, y): return x / y

            func(x, y)
            output = {} 
            for operator in args:
                output[f"{x} {operator} {y}"] = eval(f"{x} {operator} {y}")
        
            return output

        return inner

    return wrapper


@decorate("+", "-", "/")
def add_sub(x, y):
    print(f"X and Y are {x}, {y}")


print(add_sub(5, 3))


# def add(x, y):
    
#     def inner(x, y):
#         x += 1
#         return x
    
#     return inner(x, y)


# print(add(3,2))



# def decorate(func):

#     def wrapper(*args, **kwargs):
#         print("ARGS: ", args)
#         print("KWARGS: ", kwargs)
#         return func(*args, **kwargs)

#     return wrapper

# @decorate
# def add(x, y):
#     return x + y

# sum = add(x=5, y=3)
# print(sum)




"""
Q. Is this possible to make a decorator which can reverse the functionality
of in-built function str.upper to str.lower

def lower(func):
    print(func)

    def wrapper(s):
        print("arg: ", s)
        return s.lower()

    return wrapper

s= 'Hello AMIT'
supper = lower(s.upper)
print(supper(s))

"""



    





def lower_it(func):

    def wrapper():
        res = func()
        return res.lower()
    
    return wrapper

def split_string(func):

    def wrapper():
        s = func()
        return s.split()
    return wrapper

# @split_string
# @lower_it
# def hello():
#     return "hEllo AmiT"

# print(hello())



"""
def greet(func):

    def inner():
        print("Hello, ", end=' ')
        func()

    return inner

upper = greet(str.upper)

print(upper("amit"))
"""