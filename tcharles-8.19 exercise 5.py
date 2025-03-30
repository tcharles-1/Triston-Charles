#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     8.19 exercise 5
#
# Author:      tristonc
#
# Created:     03/27/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string
def analyze_text(text):
	text = text.translate(str.maketrans('', '', string.punctuation))
	words = text.lower().split()
	e_count = sum(1 for word in words if 'e' in word)
	total_words = len(words)
	if total_words > 0:
		percentage = (e_count / total_words) * 100
	else:
		percentage = 0
	print(f"Your text contains {total_words} words, of which {e_count} ({percentage:.1f}%) contain an 'e'")

my_text = """The names of my favorite song right now is lightyears and it is by John Summit who I listen to a lot."""

analyze_text(my_text)

