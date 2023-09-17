import random

 # Generate a list of ten dictionaries with unique id and random age
def simple_list():   
    result = []
    for i in range(1,11):
        result.append({"id":i,"age": random.randint(1,100)})
        return result
    
 
def sort_list():
    pass
    
    
