# import statement

# function goes here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        while response != "":
           return response
        else:
            print("This can't be be blank please enter a name")

# check for an integer between two values

# ******* Main Routine *******

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before & show

# Loop to get ticket details
# Start of the loop

# checks for an integer more than 0
def int_check(question):
    error = "Please enter a whole number between 12 and 130"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))
            return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

while name != "xxx" and ticket_count <= MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("You have {} seats "
              "left.".format(MAX_TICKETS - ticket_count))
    # Warns  user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    # Get  details...

    # Get name (can't be blank)
    name = not_blank("Name: ")

    # end the loop if the exit code is entered
    if name == "xxx":
        break

    # Get age (between 12 and 130)
    age = int_check("Age: ")

    # check that age is valid...
    if age < 12:
       print("Sorry you are too young for this movie")
       continue
    elif age > 130:
       print("This is very old - it look like a mistake.")
       continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

# End of tickets loop

# Calculate profit etc...
ticket_profit = ticket_sales -(5 * ticket_count)
print("Profit from Tickets:${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.   \n"
          "There are {} places still available."
          .format(ticket_count, MAX_TICKETS - ticket_count))
