def my_zip(customer_name, customer_id, shopping_point, struct=True):
    length = [len(customer_name), len(customer_id), len(shopping_point)]
    
    
    if struct and len(set(length)) != 1:
        return []
    
    min_length = min(length)
    
    zipped_file = [(customer_name[i], customer_id[i], shopping_point[i]) for i in range(min_length)]
    
    return zipped_file


customer_name = ["harry", "mike", "aden"]
customer_id = [103, 152, 163]
shopping_point = [150, 122, 215]

print(my_zip(customer_name, customer_id, shopping_point, struct=True))      # Expected to work normally
#print(my_zip(customer_name, customer_id, shopping_point[:2], struct=False)) # Expected to work with different list lengths
