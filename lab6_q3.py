def my_max(*args):
   
    elements = list(args)
    
    
    max_value = elements[0]

    for item in elements:
        if item > max_value:
            max_value = item
    
    return max_value


list_data = [3, 5, 2, 8, 6]
print("Maximum in list:", my_max(*list_data))  


set_data = {7, 1, 9, 4}
print("Maximum in set:", my_max(*set_data)) 


tuple_data = (2, 10, 3, 6)
print("Maximum in tuple:", my_max(*tuple_data))  
