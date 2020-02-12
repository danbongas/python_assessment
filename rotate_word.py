import string

def Rotate_word(var_str,var_num ):    
    tab = str.maketrans(string.ascii_lowercase, 
                        string.ascii_lowercase[var_num:] + string.ascii_lowercase[:var_num])
    return var_str.translate(tab)

var_str =input("Enter a string: ")
var_num= int(input("Enter rotate number: "))
print(Rotate_word(var_str,var_num))