


def decorator(method_to_decorator):
    def wrapper(*args, **kwargs):
        print('**********')
        print(args)
        print(kwargs)
        args = args
        method_to_decorator(*args,**kwargs)
    return wrapper()

@decorator
def add(a = 2,b=4):
    print(a+b)

func = lambda x,y:9+x

print(func)



























