import random

 # Generate a list of ten dictionaries with unique id and random age
def simple_list():   
    result = []
    for i in range(0,10):
        result.append({"id":i,"age": random.randint(1,100)})
    return result
    
 #Sort the list of dictionaries by age in ascending order
def sort_list(dicts):
    sorted_dicts = sorted(dicts, key=lambda x: x["age"])
    return sorted_dicts
    
    
