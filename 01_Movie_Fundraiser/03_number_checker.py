# function goes here

def int_check(question, low_num, high_num):

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))
            return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# main routine goes here
age = int_check("Age: ", 12, 130)
