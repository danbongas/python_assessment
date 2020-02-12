
def list_comprehension(lst):
 number_list = [ x for x in lst if x % 2 == 0]
 return number_list

lst = [12,24,35,70,88,120,155]
print(list_comprehension(lst))