#!python3
# rents.py - Command line program to tally up rent balance with 'rents.
# For credits (that they pay for on my account), enter a negative number.

import sys

# Open txt file and read in balance history.
rentsFile1 = open('C:\\Users\\Papa\\Documents\\mattPython\\rents.txt')
rentsContent1 = rentsFile1.readlines()
rentsFile1.close()

# Sum previous balance and print to user.
total1 = 0.0
for i in range(2, len(rentsContent1)):
    splitList1 = rentsContent1[i].split()
    num1 = float(splitList1[0])
    total1 += num1
print('Before today spend was $' + str(round(total1, 2)))

# If command line call passed a new value, add it and print updated total.
if len(sys.argv) > 1:
    # Update user.
    print('Writing in new item...')

    # Append current purchase and one word store to txt file from command line call.
    rentsFile2 = open('C:\\Users\\Papa\\Documents\\mattPython\\rents.txt', 'a')
    rentsFile2.write(str(sys.argv[1]) + ' ' + str(sys.argv[2]) + '\n')
    rentsFile2.close()

    # Update user.
    print('Successfully written in.')

    # Open txt file and read in updated purchase history.
    rentsFile3 = open('C:\\Users\\Papa\\Documents\\mattPython\\rents.txt')
    rentsContent3 = rentsFile3.readlines()
    rentsFile3.close()
    # log print here

    # Sum updated spend and print to user.
    total3 = 0.0
    for i in range(2, len(rentsContent3)):
        splitList3 = rentsContent3[i].split()
        num3 = float(splitList3[0])
        total3 += num3
    print('Total spent is now $' + str(round(total3, 2)))
    
