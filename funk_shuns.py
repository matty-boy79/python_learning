def my_standard_arguments_func(arg1, arg2, arg3):
    """
    Keyword Arguments, kwargs
    You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter.
    """

    print(arg1 + arg2 + arg3)


my_standard_arguments_func("Matt ", "is ", "AWESOME!")


def my_keyword_arguments_func(kwarg1, kwarg2, kwarg3):
    """
    Keyword Arguments, kwargs
    You can also send arguments with the key = value syntax.
    This way the order of the arguments does not matter.
    """
    print(kwarg1 + kwarg2 + kwarg3)


my_keyword_arguments_func(kwarg3="AWESOME!\n", kwarg1="Matt ", kwarg2="is ")


def my_arbitrary_arguments_func(*my_args_tuple):
    """
    Arbitrary Arguments, *args
    If you do not know how many arguments that will be passed into your function,
    add a * before the parameter name in the function definition.
    This way the function will receive a tuple of arguments, and can access the items accordingly:
    """

    print(my_args_tuple[4])
    print(my_args_tuple[3])
    print(my_args_tuple[2])
    print(my_args_tuple[1])
    print(my_args_tuple[0])
    print("")


my_arbitrary_arguments_func(5, 4, 3, 2, 1)


def my_arbitrary_keyword_arguments_func(**my_args_dict):
    """
    Arbitary Keyword Arguments, **kwargs
    If you do not know how many keyword arguments that will be passed into your function,
    add two asterisk: ** before the parameter name in the function definition.
    This way the function will receive a dictionary of arguments, and can access the items accordingly:
    """
    print(my_args_dict['two'])
    print(my_args_dict['one'])
    print("")


my_arbitrary_keyword_arguments_func(one=1, two=2)
