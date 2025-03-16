#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     7.26 exercise 9
#
# Author:      tristonc
#
# Created:     03/13/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def print_triangular_numbers(n):
	for i in range(1, n + 1):
		triangular_number = i * (i + 1) // 2
		print(triangular_number, end=" ")
	print()

print_triangular_numbers(5)
