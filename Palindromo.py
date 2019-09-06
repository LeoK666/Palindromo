#Palindromo
import string

original_str = input("Input a string: ")
modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation

for char in modified_str:
    if char in bad_chars: #remueve los caracteres que no son letras
        modified_str = modified_str.replace(char,"")

if modified_str == modified_str[::-1]: #si es un palindromo
    print("The original string is: {}".format(original_str))
    print("The modified string is: {}".format(modified_str))
    print("The reversal string is: {}".format(modified_str[::-1]))
    print("String is a palindrome")

else:
    print("The original string is: {}".format(original_str))
    print("The modified string is: {}".format(modified_str))
    print("The reversal string is: {}".format(modified_str[::-1]))
    print("String is not a palindrome")
    
