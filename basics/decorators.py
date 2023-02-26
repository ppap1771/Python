def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c, kwa = int):
    print(a, b, c)
    print(kwa)

function_with_arguments(10, 20, 30, kwa = 5)
function_with_no_argument()


# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2, decorator_arg3):
#     def decorator(func):
#         def wrapper(function_arg1, function_arg2, function_arg3) :
#             "This is the wrapper function"
#             print("The wrapper can access all the variables\n"
#                   "\t- from the decorator maker: {0} {1} {2}\n"
#                   "\t- from the function call: {3} {4} {5}\n"
#                   "and pass them to the decorated function"
#                   .format(decorator_arg1, decorator_arg2,decorator_arg3,
#                           function_arg1, function_arg2,function_arg3))
#             return func(function_arg1, function_arg2,function_arg3)

#         return wrapper

#     return decorator

# pandas = "Pandas"
# @decorator_maker_with_arguments(pandas, "Numpy","Scikit-learn")
# def decorated_function_with_arguments(function_arg1, function_arg2,function_arg3):
#     print("This is the decorated function and it only knows about its arguments: {0}"
#            " {1}" " {2}".format(function_arg1, function_arg2,function_arg3))

# decorated_function_with_arguments(pandas, "Science", "Tools")

