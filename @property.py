def get_sprinkles(func):
    def wrapper(*args,**kwargs):
        print("Get your sprinkles")
        func(*args,**kwargs)
    return wrapper

def get_fudge(func):
    def wrapper(*args,**kwargs):
        print("Get yo fudge")
        func(*args,**kwargs)
    return wrapper
@get_fudge
@get_sprinkles

def get_ice_cream(flavour):
    print(f"Here's your {flavour} ice cream")

get_ice_cream(f"{input("Enter your flavoured ice cream: ")}")

