def factorial(n):

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result

print(f"The functional of 4 is: {factorial(4)}")
print(f"The factorial of 5 is: {factorial(5)}")
print(f"The factorial of 0 is: {factorial(0)}")










def calculate_average(numbers):

    try:
        if not numbers:
            raise ValueError("Cannot calculate the average of an empety list")
        
        total_sum = sum(numbers)
        item_count = len(numbers)

        average = total_sum / item_count

        return average
    except ValueError as e:
        return str(e)
    
    except ZeroDivisionError:
        return "Division by zero error."
    
    my_list = [10,20,30,40,50]
    print(f"The list is: {my_list}")
    print(f"The average is {calculate_average(my_list)}\n")

    empty_list = []
    print(f"The list is {empty_list}")
    print(f"The average is: {calculate_averag(empty_list)}\n")

    another_list = [5,15,25,35]
    print(f"The list is: {another_list}")
    print(f"The average is: {calculate_average(another_list)}\n")










    def get_valid_age():

        while True:
            try:
                user_input = input("Please enter your age.")

                age = int(user_input)

                if age < 0:
                    raise ValueError("Your age cannot be an odd number.")
                
                return age
            except ValueError as e:
                print(f"Wrong {e} Please enter the true age.")

            user_age = get_valid_age()

            print(f"Thank you. You are {user_input} old.")
