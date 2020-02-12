def explode(var):
    new_str =""
    lst = []
    lst1 = []
  
    for i in var:     
        new_str = new_str + i  
        lst.append(new_str) 

    return ''.join([str(i) for i in lst])                   
        


var = input("Enter A Line of String:\n") 

print(explode(var))