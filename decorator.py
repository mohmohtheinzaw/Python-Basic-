def greet(fun):

    def wrapper(name):
        #before
        print('Hello')
        fun(name)
        #after
        print('Good Bye')
    return wrapper

@greet
def sayName(name):
    print(name)

sayName('mgmg')
