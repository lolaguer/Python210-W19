#!/usr/bin/env python3

# ----------------------------------#
# Assignment: mailroom_4.py
# Author: Lola Guerrero
# RRoot, 02/18/2019, Created file
# ----------------------------------#

import sys
import os
from datetime import datetime
from prettytable import PrettyTable

# Data #
# Donors table
header = "Name, Donation" # Not use but it helps to understand what the data means in our table
p1 = "Bob Smith", [25, 100, 50]
p2 = "Sue Jones", [750],
p3 = "Frankie Addams", [10, 10, 10]
p4 = "Isabel Archer", [50, 75]
p5 = "Angelica Brown", [100, 150, 75]

donors_table = [p1, p2, p3, p4, p5]


## Donors list to dict:
donors_dict = {}
donor_indx = 1
for i in range(len(donors_table)):
    name, last_name = donors_table[i][0].split()
    donation = donors_table[i][1]
    donors_dict[donor_indx] = {'Name': name, 'Last_name': last_name, 'Donation': donation}
    donor_indx += 1

# Delete the previous donors table
del donors_table

prompt = "\n".join(("Please choose from below options:",
          "1 - Send a Thank You",
          "2 - Create a Report",
          "3 - Send letters to all donors",
          "4 - Exit",
          ">>> "))


# Preprocessing #
def donor_names(donors):
    """
    Returns the complete list of donors
    """
    # Changing to comprehension list
    return [v['Name'] + ' ' + v['Last_name'] for k, v in donors.items()]


def donation_amount(name):
    """
    Returns a donor donation amount
    """
    try:
        donor_amount = int(input("How much money is the donor given?: "))

        if donor_amount < 0:
            print("You can't donate negative quantities")
            donation_amount(name)
        else:
            name, last_name = name.split()
            name = name.strip()
            last_name = last_name.strip()
            # Changing to comprehension list
            [v['Donation'].append(donor_amount) for v in donors_dict.values() if (name == v['Name']) and (last_name == v['Last_name'])]
            print('Donation amount', donor_amount)
            return donor_amount
    except ValueError:
        print ("That wasn't a correct amount. Try again.")
        donation_amount(name)


def select_a_donor():
    """
    Returns a donor Full Name
    """
    donor_name = input("Please type the donor full name: ").title()

    if donor_name.lower() == 'list':
        print ('** Here is the list of the donor names:')
        print (donor_names(donors_dict))
        print('\n')
    else:
        if donor_name not in donor_names(donors_dict):
            try:
                name, last_name = donor_name.split()
                if name.isalpha() and last_name.isalpha():
                    donor_indx = len(donors_dict) + 1
                    donors_dict[donor_indx ] = {'Name': name, 'Last_name': last_name, 'Donation': []}
                else:
                    print('One of the names is not a correct string. Please, provide a correct name.')
                    select_a_donor()
            except ValueError:
                print ('Please, provide a complete name')
                select_a_donor()
        return donor_name


def send_thank_you(name, amount):
    """
    Writes a thank you note to the donor for his/her donation
    """

    # if name is None:
    #     return prompt

    if name:
        if amount is None:
            amount = donation_amount(name)
    else:
        name = select_a_donor()
        if amount is None:
            amount = donation_amount(name)

        print ('Amount in  the tank you note', amount)
        print("\n")
        print (f"Dear {name}," + "\n" + f"We really appreciate your support donating to us the amount of ${amount}." + "\n" + "Thank you!!")
        print ("\n")
    return f"Dear {name}," + "\n" + f"We really appreciate your support donating to us the amount of ${amount}." + "\n" + "Thank you!!"


def sort_amt(donor):
    """
    Converts and returns the donor amount string ($XX.00) into an integer (XX)
    """
    return int(donor[1].replace('$', '').replace('.00', ''))


def create_report():
    """
    Creates a table with all the donors, number of donations, total and average donated amounts
    """
    # Changing to comprehension list
    donors_name = [v['Name'] + ' ' + v['Last_name'] for v in donors_dict.values()]
    total_donated = [sum(v['Donation']) for v in donors_dict.values()]
    number_donations = [len(v['Donation']) for v in donors_dict.values()]
    average_donation = [x / y for x, y in zip(total_donated, number_donations)]
    total_donated = ['$%.2f' % t for t in total_donated]
    average_donation = ['$%.2f' % n for n in average_donation]
    summary_donnors_table = [(name, total, num, avg) for name, total, num, avg in zip(donors_name, total_donated, number_donations, average_donation)]

    sorted_table = sorted(summary_donnors_table, key=sort_amt, reverse=True)

    t = PrettyTable(["Donor Name", "Total Given", "Num Gifts", "Average Gift"])

    for row in sorted_table:
        t.add_row(list(row))

    t.align["Donor Name"] = "l"
    t.align["Total Given"] = "r"
    t.align["Num Gifts"] = "r"
    t.align["Average Gift"] = "r"

    return t


def send_letters():
    """
    Creates a file with the thank you note for his/her total donation
    """
    for i in range(1,len(donors_dict)+1):
        c_name = donors_dict[i]['Name']+ ' ' + donors_dict[i]['Last_name']
        total_donation = sum(donors_dict[i]['Donation'])
        date = datetime.now().strftime('%m_%d_%Y')
        try:
            file = open('./thank_you_letters/' + c_name + '_' + date + '.txt', 'w')
            text = f"Dear {c_name}," + "\n" + f"We really appreciate your support donating to us the total amount of ${total_donation}." + "\n" + "Thank you!!"
            file.write(text)
        except FileNotFoundError:
            os.mkdir('./thank_you_letters/')
            send_letters()
    print ('Letters saved!!\n')


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script


arg_dict = {"1": send_thank_you,
            "2": create_report,
            "3": send_letters,
            "4": exit_program}

def main():

    while True:
        try:
            response = input(prompt)
            arg_dict.get(response, 'Not a valid option!')()
        except TypeError:
            response = input(prompt)
            arg_dict.get(response, 'Not a valid option!')()
        except FileNotFoundError:
            response = input(prompt)
            arg_dict.get(response, 'Not a valid option!')()
        except EOFError:
            response = input(prompt)
            arg_dict.get(response, 'Not a valid option!')()
        except KeyboardInterrupt:
            response = input(prompt)
            arg_dict.get(response, 'Not a valid option!')()

# Presentation #
if __name__ == "__main__":
    main()