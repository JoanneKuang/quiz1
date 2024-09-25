#!/usr/bin/env python3

# Author: Joanne Kuang
# Student ID: 165994187
# Date: 09-25-2024

# convert inches to cm
def inchtocm(inch):
	return inch * 2.54

# convert cm to inches
def cmtoinch(cm):
	return cm / 2.54

def main():
	while True:
		# this will ask the user what selection they want to pick
		print("1. Convert inches -> cm")
		print("2. Convert cm -> inches")
		selection = input("Make your selection (1, 2): ")

		# if 1 is picked then enter the inch and convert
	  if selection == '1':
		inches = int(input("Enter inches: "))
		cm = inchtocm(inch)
		print("Number of cm: " + str(cm))
	  	# if 2 is picked then enter the cm and convert
	  elif selection == '2':
		cm = int(input("Enter cm: "))
		inch = cmtoinch(cm)
		print("Number of inches: " + str(inch))
		# when user enter number that arent 1 or 2 
	  else:
		print("Invalid please try again")


if __name__ == "__main__":
	main()
