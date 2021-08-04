# function goes here

def not_blank(question) -> object:
    valid = False

    while not valid:
        response = input(question)

        while response != "":
            return response
        else:
            print("This can't be be blank please enter a name")


# main routine goes here

name = not_blank("Name: ",
                 "Sorry - this can't be blank, please enter your name")
