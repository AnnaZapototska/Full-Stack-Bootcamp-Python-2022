# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Bonus : use some Buit-in exceptions of Python : Look here
#  solution 1
# try:
#     result = 5 /0
# except ZeroDivisionError:
#     print("Error: division by zero")

# solution 2 with function
def division_zero():
    try:
        result = 5 /0
    except ZeroDivisionError:
        print("Error: division by zero")
        
division_zero()
