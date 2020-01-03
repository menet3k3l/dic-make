# dic-make
Password dictionary generator

# How to use?
python3 dic-make.py [options]

# Options:
-h  ... ... ... help

-n (#)  ... ... add numbers after keywords (default range 0 - 9)
(#) ->  modifies the range like so: -n 999 ->  000-999

-c (#)  ... ... combinations of lower and upper case letters, 
(#) = 1 -> only first letter in a keyword is being changed
(#) = 2 -> all possible combinations of lower and upper case letters in a keyword

# File?
When you run the program, it asks you to enter a filename.
It's a name for a file that the generated combinations will be put in after the program ends.

# FYI
There's a bunch of predefined "keynumbers" that are very common (like "123456").
Every time you run the program it will automatially combine keywords and keynumbers.
