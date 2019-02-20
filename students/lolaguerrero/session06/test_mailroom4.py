#!/usr/bin/env python3

# ----------------------------------#
# Assignment: test_mailroom_4.py
# Author: Lola Guerrero
# RRoot, 02/18/2019, Created file
# ----------------------------------#

import pytest
from mailroom_4 import send_thank_you, create_report, send_letters


print (send_thank_you("Frank", 80000))

def test_send_thank_you():
    expected = "Dear Frank," + "\n" + "We really appreciate your support donating to us the amount of $800000." + "\n" + "Thank you!!"
    assert send_thank_you("Frank", 800000) == expected

#
# #def test_create_report():
#     assert 1 == 1
#
#
# #def test_send_letters():
#     assert 1 == 1
