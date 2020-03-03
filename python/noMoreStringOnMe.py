# Accessing Values in Strings
var1 = "Hello World!"
var2 = "Python Programming"
breakLine = "\n  ============================================================================================== \n"

'''
print ("Chooseing: "+ "var[0]: ") , var1[0]
print ("Chooseing: "+ "var[1:5]': ") , var2[1:5]
print ("Adding an updated variable to the mix: "+"Updating String: -" ), var1[:6] + "Python"
'''
# Escape Characters
# \a	0x07	Bell or alert
# \b	0x08	Backspace
# \cx	 	    Control-x
# \C-x	 	    Control-x
# \e	0x1b	Escape
# \f	0x0c	Formfeed
# \M-\C-x	 	Meta-Control-x
# \n	0x0a	Newline
# \nnn	 	    Octal notation, where n is in the range 0.7
# \r	0x0d	Carriage return
# \s	0x20	Space
# \t	0x09	Tab
# \v	0x0b	Vertical tab
# \x	 	    Character x
# \xnn	 	    Hexadecimal notation, where n is in the range 0.9, a.f, or A.F

# print ("USING Escape Characters to assign values: "+"My name is %s and weight is %d kg!") % ("Cody", 100)

# String Special Operators
# +	        Concatenation - Adds values on either side of the operator	a + b will give HelloPython
# *	        Repetition - Creates new strings, concatenating multiple copies of the same string	a*2 will give -HelloHello
# []	    Slice - Gives the character from the given index	a[1] will give e
# [ : ]	    Range Slice - Gives the characters from the given range	a[1:4] will give ell
# in	    Membership - Returns true if a character exists in the given string	H in a will give 1
# not in    Membership - Returns true if a character does not exist in the given string	M not in a will give 1
# r/R	    Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark.	print r'\n' prints \n and print R'\n'prints \n
# %	        Format - Performs String formatting	See at next section


# String Formatting Operator
# %c	character
# %s	string conversion via str() prior to formatting
# %i	signed decimal integer
# %d	signed decimal integer
# %u	unsigned decimal integer
# %o	octal integer
# %x	hexadecimal integer (lowercase letters)
# %X	hexadecimal integer (UPPERcase letters)
# %e	exponential notation (with lowercase 'e')
# %E	exponential notation (with UPPERcase 'E')
# %f	floating point real number
# %g	the shorter of %f and %e
# %G	the shorter of %f and %E

# *	        argument specifies width or precision
# -	        left justification
# +	        display the sign
# <sp>	    leave a blank space before a positive number
# #	        add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
# 0	        pad from left with zeros (instead of spaces)
# %	'%%'    leaves you with a single literal '%'
# (var)	    mapping variable (dictionary arguments)
# m.n.	    m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)

'''
#Triple Quotes
print (breakLine)
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)
'''

# print (u'Hello, world!')

# raw_input("\n\nPress the enter key to exit.") #will wait for user input

# import sys; x = 'foo'; sys.stdout.write(x + '\n')

# tup = ('physics', 'chemistry', 1997, 2000)
# print (tup)
# del (tup)
# print ("After deleting tup : ")
# print (tup) #Will throw eror since the tup was deleted...


# print 'abc', -4.24e93, 18+6.6j, 'xyz';
# x, y = 1, 2;
# print "Value of x , y : ", x,y; #prints val x,y respectivly.

# Accessing a dictionary
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print "dict['Name']: ", dict['Name']
# print "dict['Age']: ", dict['Age']

# Updating a dictionary
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']
print dict
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print dict
print "dict['Age']: ", dict['Age']
print "dict['School']: ", dict['School']