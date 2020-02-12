def replace_x(var):
    new_str =""
    var_len = len(var)
    for i in var:
      if i != 'X' and i != 'x':  
        new_str = new_str + i
      
        
    print(new_str)    


var = input("Enter A Line of String:\n") 

replace_x(var)