class divisionby12Error(Exception):
    pass


try:
    number = int(input("enter a number: "))
    res = 10 / number
    if(number == 12):raise divisionby12Error("division by 12 not allowed in our program")
    print(number)
except ValueError as e:
    print("please enter a number!",e)
except ZeroDivisionError as e:
    print("division by 0 not allowed",e)

except     divisionby12Error as e:
    print("error",e)
except Exception as e:
    print("some error happened",e)
finally:
    print("we are in finnally ")
