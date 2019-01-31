#!/usr/bin/env python3

# ----------------------------------#
# Assignment: mailroom.py
# Author: Lola Guerrero
# RRoot, 01/29/2019, Created file
# ----------------------------------#


###### Not finished yet!! #########

import sys

# Donors table
header = "Name, Donation"
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




def send_tank_you():

    """ Return a donor Full Name"""
    donor_name = input("Please type the donor full name: ").title()

    def sort_donor_last_name(donors):
        """ Sort on the last name"""
        print ('donor', donors)
        return donors[0].split(" ")[1]

    def donor_names(donors):
        d_names = []
        for row in donors:
            name = row[1]
            d_names.append(name)
        return d_names

    if donor_name.lower() == 'list':
        print ('Here is the list of the donor names:\n')
        print (donor_names(donors_table), '\n')
        #print (sorted(donors_table, key=sort_donor_last_name))
    else:
        if donor_name.lower().split() not in donor_names(donors_table):
            new_donor = (donor_name, [])
            donors_table.append(new_donor)
            print (donors_table)
    #     else:
    #         return donor_name


def donation_amount():
    if type(send_tank_you) == str:
        donor_amount = int(input("How much money is the donor given?").title())
    for row in donors_table:
        if send_tank_you == row[1]:
            row[2].append(donor_amount)


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


def main():
    while True:
        response = input(prompt)  # continuously collect user selection
        # now redirect to feature functions based on the user selection
        if response == "1":
            send_tank_you()
        elif response == "2":
            print ('For now only 1')
        elif response == "3":
            exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()