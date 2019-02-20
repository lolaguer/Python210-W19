#!/usr/bin/env python3

# ----------------------------------#
# Assignment: test_mailroom_4.py
# Author: Lola Guerrero
# RRoot, 02/18/2019, Created file
# ----------------------------------#

from mailroom_4 import send_thank_you, create_report, send_letters
import prettytable
import os


def test_send_thank_you():
    expected = "Dear Frank," + "\n" + "We really appreciate your support donating to us the amount of $800000." + "\n" + "Thank you!!"
    assert send_thank_you(name="Frank", amount=800000) == expected


def test_create_report():
    tb = create_report()
    assert tb.field_names == ['Donor Name', 'Total Given', 'Num Gifts', 'Average Gift']
    assert type(create_report()) is prettytable.PrettyTable


def test_send_letters():
    send_letters()
    path = "/Users/i22041/Documents/Python_Certification_UW/PYTHON210/Python210-W19/students/lolaguerrero/session06/thank_you_letters"
    assert len(os.listdir(path)) != 0
