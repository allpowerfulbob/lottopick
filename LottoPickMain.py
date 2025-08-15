# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import generate lotto numbers module
import GenerateLottoNumbers
import re

def main():
    class LottoNumberGenerator:
        def __init__ (self, co_generator, pb_generator, mm_generator):
            self.co_generator = GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto
            self.pb_generator = GenerateLottoNumbers.generate_lotto_numbers_power_ball
            self.mm_generator = GenerateLottoNumbers.generate_lotto_numbers_mega_millions

    choice = input("Choose a lottery type (Colorado Lotto, Power Ball, Mega Millions): ")
    if re.match("Colorado Lotto", choice, re.IGNORECASE):
        print("Here are your Colorado Lotto Numbers: " + str(co_generator()))
    elif re.match("Power Ball", choice, re.IGNORECASE):
        print("Here are your Power Ball Numbers: " + str(pb_generator()))
    elif re.match("Mega Millions", choice, re.IGNORECASE):
        print("Here are your Mega Millions Numbers: " + str(mm_generator()))
    else: print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()