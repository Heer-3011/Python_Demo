import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result 
    return wrapper

#decoraters enables us to run specific code before running the function
#it can be use to see wheter user is loged in or not  
@timer
def example(n):
    time.sleep(n)

example(2)