def sum(a:int,b:int) -> int:
    sum = a / b
    return sum

try: #Code that might raise an exception
    a = int(input("Enter the Number : "))
    b = int(input("Enter the Number : "))
    a = sum(a,b)
    print(f"\nOutput : {round(a,2)}")

except ZeroDivisionError: #Code that handles ZeroDivisionError 
    print("A Number Can't be Divide by Zero")

except ValueError: #Code that handles ValueError
    print("Enter a Valid Number !")

except Exception as e: #Code that handle any error
    print(e)

else: #Code that runs if no exception occurred
    print("Else : Program Worked")

finally: #Code that must run no matter what
    print("Finally : I work all time ")