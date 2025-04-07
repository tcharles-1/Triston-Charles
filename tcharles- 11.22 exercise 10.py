#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     11.22 exercise 10
#
# Author:      tristonc
#
# Created:     04/05/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def replace(s, old, new):
    split_string = s.split(old)
    joined_string = new.join(split_string)
    return joined_string

s = "How old are those trees? Are they as old as those old trees?"
print(replace(s, "old", "new"))
