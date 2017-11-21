#!python3
# spgMin.py - Command line program to tally up SPG spending via txt file.
# If called prints total to date, if passed a new purchase adds it to doc and sums a new total.

import sys

# Open txt file and read in purchase history.
spgFile1 = open('C:\\Users\\Papa\\Documents\\mattPython\\spgMin.txt')
spgContent1 = spgFile1.readlines()
# enter log print here

# Sum previous spend and print to user.
total1 = 0.0
for i in range(2, len(spgContent1)):
    strLen = len(spgContent1[i])
    total1 += float(spgContent1[i][0:(strLen-1)])
print('Before today spend was $' + str(round(total1, 2)))
spgFile1.close()

# If the command line call passed a purchase value, add it and print the new total.
if len(sys.argv) > 1:
    # Update user.
    print('Writing in new purchase...')

    # Append current purchase to txt file from command line call.
    spgFile2 = open('C:\\Users\\Papa\\Documents\\mattPython\\spgMin.txt', 'a')
    spgFile2.write(str(sys.argv[1]) + '\n')
    spgFile2.close()
    # how to verify that this worked?

    # Update user.
    print('Successfully written in.')

    # Open txt file and read in updated purchase history.
    spgFile3 = open('C:\\Users\\Papa\\Documents\\mattPython\\spgMin.txt')
    spgContent3 = spgFile3.readlines()
    # log print here

    # Sum updated spend and print to user.
    total3 = 0.0
    for i in range(2, len(spgContent3)):
        strLen3 = len(spgContent3[i])
        total3 += float(spgContent3[i][0:(strLen3-1)])
    print('Total spent is now $' + str(round(total3, 2)))
    spgFile3.close()
    
