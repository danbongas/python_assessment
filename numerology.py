from string import ascii_lowercase


LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()

    temp_str =''
    new_str = ''
    int_str = 0
    sum_res = 0
    output = []

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    temp_str = '+'.join(numbers)
    new_str = eval(temp_str)    
    int_str = int(new_str)
    
    print("Integer? :",int_str)

    if int_str == 11 and int_str == 13:
       final_res = int_str
    else:   
     while int_str>0 :
        rem = int_str % 10
        int_str = int(int_str / 10) 
        output.append(rem) 
        final_res = sum(output)
    print("Magic Number :", final_res)      
        
          






text = input("Enter String: \n")    


alphabet_position(text)