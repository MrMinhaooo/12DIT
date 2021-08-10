
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

# initialise variables
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range(0, 3):

    # ask user for desire snack and put it in lowercase
    desire_snack = input("Snack: ").lower()

    for var_list in valid_snacks:

        # if the snack is in one of the list
        if  desire_snack in var_list:

            # Get full name of snack and put it
            # in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # if the chosen snack is not valid, srt snack_ok to no
        else:
            snack_ok = "no"

    # if the snack is not OK -ask question again.
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid choice")

