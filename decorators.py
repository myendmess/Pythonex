#functional programming paradigm
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello World!")

hello()  # This line should be outside the function
