greeting = "hello splinter"
print(greeting)

def welcome_message():
    global greeting
    greeting = "hello ninja"
    print(greeting)
    return(greeting)

welcome_message()
print(f"new greeting = {greeting}")