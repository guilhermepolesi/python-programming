# The Caesar Cipher: encrypting a message
#
# We will show you four simple programs to introduce some aspects of string processing in Python.
# They are purposefully simple.
#
# The first problem we want to show is called Caesar cipher
# more details here: https://en.wikipedia.org/wiki/Caesar_cipher.

# This cipher was (probably) invented and used by Gaius Julius Caesar and his troops during
# the Gallic Wars. The idea is quite simple - each letter in the message is replaced by
# its closest consequent (A becomes B, B becomes C, and so on). The only exception is Z, which becomes A.
#
# The program is a very simple (but functional) implementation of the algorithm.

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# We write it using the following assumptions:
#
#     accepts only Latin letters (note: the Romans did not use whitespace or digits)
#     all letters in the message are in capital letters (note: the Romans only knew capital letters)
#
# Let's trace the code:
#
#     line 16: ask the user to insert the open (non-encrypted) one-line message;
#     line 17: prepare a string for an encrypted message (empty for now)
#     line 18: start iteration through the message;
#     line 19: if the current character is not alphabetic...
#     line 20: ...ignore it;
#     line 21: convert the letter to uppercase (it is preferable to do it blindly, rather than checking
#     whether it is necessary or not)
#     line 22: get the letter code and increment it by one;
#     line 23: if the resulting code has “left” the Latin alphabet (if it is greater than the Z code)...
#     line 24: ...change it to code A;
#     line 25: append the received character to the end of the encrypted message;
#     line 27: print the cipher.
#
# The input with this message:
# AVE CAESAR
#
# has the following output:
# BWFDBFTBS


# The inverse transformation should now be clear to you - we'll just present you with the code as is
# without any explanations.
# Use the cryptogram from the previous program.

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# The Number Crunch
#
# The third program shows a simple method that allows you to enter a line full of numbers, and process
# them easily. Note: the input() routine function, combined with the int() or float() functions
# is unsuitable for this purpose.
#
# Processing will be extremely easy - we want the numbers to add up.
#
# See the code, let's analyze it.

# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")

# Let's present our version:
#
#     line 86: ask the user to enter a line filled with any number of numbers (numbers can be floats)
#     line 87: split the line receiving a list of substrings;
#     line 88: start the total sum at zero;
#     line 89: as the string-float conversion can raise an exception, it is best to continue with
#     the protection of the try-except block;
#     line 90: iterate through the list...
#     line 91: ...and try to convert all its elements into float numbers; if it works, increase the sum;
#     line 92: everything is fine so far, so print the sum;
#     line 93: the program ends here in case of an error;
#     line 94: print a diagnostic message showing the user the reason for the failure.
#
# The code has an important weakness - it presents a false result when the user enters an empty line.


# The IBAN validator
#
# The fourth program implements (in a slightly simplified form) an algorithm used by European banks
# to specify account numbers. The standard called IBAN (International Bank Account Number) provides
# a simple and very reliable method of validating account numbers against simple typing errors that
# may occur when rewriting the number, for example, on paper documents such as invoices or bills, for computers.
#
# You can find more details here: https://en.wikipedia.org/wiki/International_Bank_Account_Number.
#
# An IBAN-compliant account number consists of:
#
#     a two-letter country code taken from ISO 3166-1 (for example, FR for France, GB for Great Britain
#     DE for Germany, and so on)
#     two check digits used to perform validity checks - quick and simple but not entirely reliable tests
#     showing whether a number is invalid (distorted by a typo) or whether it appears to be valid;
#     the actual account number (up to 30 alphanumeric characters - the length of this part depends on the country)
#
# The standard says that validation requires the following steps (according to Wikipedia):
#
#     (step 1) Check that the total length of the IBAN is correct according to the country (this program will
#     not do this, but you can modify the code to meet this requirement if you wish; note: you must teach the code
#     all the lengths used in Europe)
#     (step 2) Move the initial four characters to the end of the string (i.e. the country code and check digits)
#     (step 3) Replace each letter in the string with two digits, thus expanding the string
#     where A = 10, B = 11... Z = 35;
#     (step 4) Interpret the string as a decimal integer and calculate the remainder of that number when divided by 97;
#     If the remainder is 1, the digit verification test is passed and the IBAN may be valid.
#
# See the code, let's analyze it:

# IBAN Validator.
iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


# line 143: ask the user to enter the IBAN (the number may contain spaces, as they significantly improve the
# legibility of the number...
#     line 144: ...but remove them immediately)
#     line 146: the IBAN entered must consist of digits and letters only - if it does not...
#     line 147:... output the message;
#     line 148: the IBAN must not be shorter than 15 characters (this is the shorter variant, used in Norway)
#     line 149: if it is shorter, the user is informed;
#     line 150: in addition, the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
#     line 151: if it is longer, make a warning;
#     line 152: start the processing itself;
#     line 153: move the initial four characters to the end of the number and convert all letters to uppercase
#     (step 02 of the algorithm)
#     line 154: this is the variable used to complete the number, created by replacing letters with digits
#     (according to step 03 of the algorithm)
#     line 155: iterate through the IBAN;
#     line 156: if the character is a digit...
#     line 157: just copy it;
#     line 158: otherwise...
#     line 159: ...convert it to two digits (note how this is done here)
#     line 160: the converted form of the IBAN is ready - make an integer of it;
#     line 161: is the remainder of dividing iban2 by 97 equal to 1?
#     line 162: If yes, then success;
#     line 163: Otherwise...
#     line 164: ...the number is invalid.
#
# Let's add some test data (all these numbers are valid - you can invalidate them by changing any character).
#
#     British: GB72 HBZU 7006 7212 1253 00
#     French: FR76 30003 03620 00020216907 50
#     German: DE02100100100152517108

