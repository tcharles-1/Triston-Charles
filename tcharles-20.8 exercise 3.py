#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     20.8 exercise 3
#
# Author:      tristonc
#
# Created:     04/24/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

with open("alice.txt", "r", encoding="utf-8") as file:
    text = file.read()

start_marker = "*** START OF THIS PROJECT GUTENBERG EBOOK"
end_marker = "*** END OF THIS PROJECT GUTENBERG EBOOK"

start = text.find(start_marker)
end = text.find(end_marker)

if start != -1 and end != -1:
    text = text[start + len(start_marker):end]

text = text.lower()

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in punctuation:
    text = text.replace(char, " ")

words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.keys())

with open("alice_words.txt", "w", encoding="utf-8") as output_file:
    output_file.write("Word              Count\n")
    output_file.write("=======================\n")
    for word in sorted_words:
        count = word_counts[word]
        line = "{:<17}{}\n".format(word, count)
        output_file.write(line)

print("The word 'alice' occurs", word_counts.get("alice", 0), "times.")
