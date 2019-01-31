#!/usr/bin/env python3

# ----------------------------------#
# Assignment: mailroom.py
# Author: Lola Guerrero
# RRoot, 01/29/2019, Created file
# ----------------------------------#


###### Not finished yet!! #########

import sys

# Data #
# Donors table
header = "Name, Donation" # Not use but helps to understand the data in our table
p1 = "Bob Smith", [25, 100, 50]
p2 = "Sue Jones", [750],
p3 = "Frankie Addams", [10, 10, 10]
p4 = "Isabel Archer", [50, 75]
p5 = "Angelica Brown", [100, 150, 75]

donors_table = [p1, p2, p3, p4, p5]



prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Exit",
          ">>> "))


# Preprocessing #
def donor_names(donors):

    """ Return the complete list of donors """

    d_names = []
    for row in donors:
        name = row[0]
        d_names.append(name)
    return d_names


def donation_amount(name):

    """ Return a donor donation amount """

    donor_amount = int(input("How much money is the donor given?: "))
    for row in donors_table:
        if name == row[0]:
            row[1].append(donor_amount)
    return donor_amount


def select_a_donor():

    """ Return a donor Full Name """

    donor_name = input("Please type the donor full name: ").title()

    if donor_name.lower() == 'list':
        print ('Here is the list of the donor names:\n')
        print (donor_names(donors_table), '\n')
    else:
        if donor_name not in donor_names(donors_table):
            new_donor = (donor_name, [])
            donors_table.append(new_donor)
            return donor_name
        else:
            return donor_name


def send_tank_you():
    name = select_a_donor()
    if name is None:
        return prompt
    else:
        amount = donation_amount(name)
        print (f"Dear {name}," + "\n" + f"We really appreciate your support donating to us the amount of ${amount}." + "\n" + "Thank you!!")
        print ("\n")
    return prompt


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)
        if response == "1":
            send_tank_you()
        elif response == "2":
            print ('For now only 1 is ready!')
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


# Presentation #
if __name__ == "__main__":
    main()