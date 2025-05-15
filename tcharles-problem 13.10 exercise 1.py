#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     13.10 exercise 1
#
# Author:      tristonc
#
# Created:     04/12/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def reverse_file_lines(input_filename, output_filename):
    try:
        infile = open(input_filename, 'r')
        lines = infile.readlines()
        infile.close()

        reversed_lines = []
        index = len(lines) - 1
        while index >= 0:
            reversed_lines.append(lines[index])
            index -= 1

        outfile = open(output_filename, 'w')
        for line in reversed_lines:
            outfile.write(line)
        outfile.close()

        print("Reversed lines written to '{}' successfully.".format(output_filename))

    except FileNotFoundError:
        print("Error: The file '{}' was not found.".format(input_filename))
    except Exception as e:
        print("An error occurred: {}".format(e))

input_file = 'input.txt'
output_file = 'output.txt'
reverse_file_lines(input_file, output_file)

with open(output_file, 'r') as outfile:
    print(outfile.read())

