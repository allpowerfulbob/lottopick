# Copyright (c) Bob Sheets 2025 all rights reserved
# Powerball and Megamillions propety of their respective owners
# Import generate lotto numbers module
import GenerateLottoNumbers
import re

def main():

    choice = input("Choose a lottery type (Colorado, Power Ball, Mega Millions): ")
    tickets = int(input("How many tickets would you like to generate? "))
    if re.match("Colorado", choice, re.IGNORECASE):
        for _ in range(tickets):
            print("Here are your Colorado Lottery Numbers: " +
                str(GenerateLottoNumbers.generate_lotto_numbers_colorado_lotto()))
    elif re.match("Power Ball", choice, re.IGNORECASE):
        for _ in range(tickets):
            print("Here are your Power Ball Numbers: " +
                str(GenerateLottoNumbers.generate_lotto_numbers_power_ball()))
            print("Here is your Powerball: " + 
                  str(GenerateLottoNumbers.generate_lotto_numbers_power_ball_powerball()))
    elif re.match("Mega Millions", choice, re.IGNORECASE):
        for _ in range(tickets):
            print("Here are your Mega Millions Numbers: " +
                str(GenerateLottoNumbers.generate_lotto_numbers_mega_millions()))
            print("Here is your Megaball: " + 
                  str(GenerateLottoNumbers.generate_lotto_numbers_mega_millions_megaball()))
    else: print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
