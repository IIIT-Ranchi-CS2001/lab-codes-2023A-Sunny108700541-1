def manipulate_strings(S1):
 
    S1 = "Maha Bharat"
    s1_modified1 = S1.lower().capitalize() + " " + S1.split()[1].upper()
    s1_modified2 = S1.split()[1]
    
    s1_modified3 = S1.split()[1] * 3
    
    s1_modified4 = S1.replace("Maha", "Mera")
    
    s1_modified5 = s1_modified4 + " Mahan"
    
    return s1_modified1, s1_modified2, s1_modified3, s1_modified4, s1_modified5


S1 = "Maha Bharat"
result = manipulate_strings(S1)
for res in result:
    print(res)

