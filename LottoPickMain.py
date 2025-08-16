# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import generate lotto numbers module
from GenerateLottoNumbers import LottoNumberGenerator
import re
import unittest

def main():
    

    choice = input("Choose a lottery type (Colorado, Power Ball, Mega Millions): ")
    if re.match("Colorado", choice, re.IGNORECASE):
        print("Here are your Colorado Lottery Numbers: " + str(LottoNumberGenerator.co_generator()))
    elif re.match("Power Ball", choice, re.IGNORECASE):
        print("Here are your Power Ball Numbers: " + str(LottoNumberGenerator.pb_generator()))
    elif re.match("Mega Millions", choice, re.IGNORECASE):
        print("Here are your Mega Millions Numbers: " + str(LottoNumberGenerator.mm_generator()))
    else: print("Invalid choice. Please try again.")
    

if __name__ == '__main__':
    main()