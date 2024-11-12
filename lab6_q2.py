def my_zip(customer_name, customer_id, shopping_points, strct=True):
  
    lengths = [len(customer_name), len(customer_id), len(shopping_points)]
    
   
    if strct and len(set(lengths)) != 1:
        return []  
    
    
    min_length = min(lengths)
    
   
    zipped_list = [(customer_name[i], customer_id[i], shopping_points[i]) for i in range(min_length)]
    
    return zipped_list

def my_sort(data, key=0):
    n = len(data)
    
   
    for i in range(n):
        for j in range(0, n - i - 1):
            
            if data[j][key] > data[j + 1][key]:
                
                data[j], data[j + 1] = data[j + 1], data[j]
    
    return data


customer_name = ["Alice", "Charlie", "Bob"]
customer_id = [101, 103, 102]
shopping_points = [500, 200, 300]


zipped_data = my_zip(customer_name, customer_id, shopping_points)


print("Sorted by customer name:", my_sort(zipped_data, key=0))


print("Sorted by customer ID:", my_sort(zipped_data, key=1))


print("Sorted by shopping points:", my_sort(zipped_data, key=2))
