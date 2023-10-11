"""
A context manager is an object that defines the methods __enter__() and __exit__(). 
Mainly it is used to set up resources before a block of code is executed and to 
clean up resources after the block of code is executed.
"""

class MyContextManager:

    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Exiting the context" )
        if exc_type is not None:
            print(f"Exception: {exc_type} - {exc_value}")
        return True  # Suppressing exceptions


# Using the context manager
with MyContextManager() as cm:
    print("Inside the context")

