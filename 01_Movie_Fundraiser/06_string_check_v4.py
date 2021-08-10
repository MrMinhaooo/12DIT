

# Function goes here
def string_check(choice, options):
    for var_list in options:

        #if the snack is in one of the lists, return the full function
        if choice in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted

            chosen = var_list[0].title()
            is_valid = "yes"
            break

       # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

# Valid snacks hold list of all snacks
# Each item im valid snacks in a list with
# valid options for each snacks  is a list with
# valid options for each snack <full name, letter code  (a, -e)
# , and possible abbreviations etc>
valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "o"],
    ["water", "w", "d"]
]

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# hold snack order for a single user.
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# If they say yes, ask what snacks they want (and add to our snack)
if check_snack == "=Yes":

    desire_snack = ""
    while desire_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desire_snack = input("Snack: ").lower()

        if desire_snack == "xxx":
            break

        # check if snack is valid
        snack_choice = string_check(desire_snack, valid_snacks)
        print("Snack Choice: ", snack_choice)

        # add snack to list...

        # check that snack is not the exit code become adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# Show snack orders
print()
if len(snack_order) == 0:
    print("Snack Ordered: None")

else:
    print("Snacks ordered:")

    for item in snack_order:
        print(item)