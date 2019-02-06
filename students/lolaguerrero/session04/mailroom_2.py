#!/usr/bin/env python3

# ----------------------------------#
# Assignment: mailroom_2.py
# Author: Lola Guerrero
# RRoot, 02/04/2019, Created file
# ----------------------------------#

import sys
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
    d_names = []
    for i in range(1,len(donors)):
        c_name = donors[i]['Name']+ ' ' + donors[i]['Last_name']
        d_names.append(c_name)
    return d_names


def donation_amount(name):
    """
    Returns a donor donation amount
    """
    donor_amount = int(input("How much money is the donor given?: "))
    name, last_name = name.split()
    name = name.strip()
    last_name = last_name.strip()
    for i in range(1, len(donors_dict)+1):
        if (name == donors_dict[i]['Name']) and (last_name == donors_dict[i]['Last_name']):
            donors_dict[i]['Donation'].append(donor_amount)
    return donor_amount


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
            name, last_name = donor_name.split()
            donor_indx = len(donors_dict) + 1
            donors_dict[donor_indx ] = {'Name': name, 'Last_name': last_name, 'Donation': []}
        return donor_name


def send_thank_you():
    """
    Writes a thank you note to the donor for his/her donation
    """

    name = select_a_donor()
    if name is None:
        return prompt
    else:
        amount = donation_amount(name)
        print("\n")
        print (f"Dear {name}," + "\n" + f"We really appreciate your support donating to us the amount of ${amount}." + "\n" + "Thank you!!")
        print ("\n")
    return prompt


def sort_amt(donor):
    """
    Converts and returns the donor amount string ($XX.00) into an integer (XX)
    """
    return int(donor[1].replace('$', '').replace('.00', ''))


def create_report():
    """
    Creates a table with all the donors, number of donations, total and average donated amounts
    """
    summary_donnors_table = []
    for i in range(1, len(donors_dict)+1):
        print('#######')
        print (donors_dict)
        print (donors_dict[i])
        donors_name = donors_dict[i]['Name']+ ' ' + donors_dict[i]['Last_name']
        total_donated = sum(donors_dict[i]['Donation'])
        number_donations = len(donors_dict[i]['Donation'])
        average_donation = total_donated / number_donations
        # Some formatting in the values
        total_donated = '$%.2f' % total_donated
        average_donation = '$%.2f' % average_donation
        donor_sum = (donors_name, total_donated, number_donations, average_donation)
        summary_donnors_table.append(donor_sum)

    sorted_table = sorted(summary_donnors_table, key=sort_amt, reverse=True)

    t = PrettyTable(["Donor Name", "Total Given", "Num Gifts", "Average Gift"])

    for row in sorted_table:
        t.add_row(list(row))

    t.align["Donor Name"] = "l"
    t.align["Total Given"] = "r"
    t.align["Num Gifts"] = "r"
    t.align["Average Gift"] = "r"

    print (t)

def send_letters():
    """
    Creates a file with the thank you note for his/her total donation
    """
    for i in range(1,len(donors_dict)+1):
        c_name = donors_dict[i]['Name']+ ' ' + donors_dict[i]['Last_name']
        total_donation = sum(donors_dict[i]['Donation'])
        date = datetime.now().strftime('%m_%d_%Y')
        file = open('./thank_you_letters/' + c_name + '_' + date + '.txt', 'w')
        text = f"Dear {c_name}," + "\n" + f"We really appreciate your support donating to us the total amount of ${total_donation}." + "\n" + "Thank you!!"
        file.write(text)
    print ('Letters saved\n')


def exit_program():
    print("Bye!")
    sys.exit()  # exit the interactive script



arg_dict = {"1": send_thank_you,
            "2": create_report,
            "3": send_letters,
            "4": exit_program}

def main():

    while True:
        response = input(prompt)
        arg_dict.get(response, 'Not a valid option!')()


# Presentation #
if __name__ == "__main__":
    main()