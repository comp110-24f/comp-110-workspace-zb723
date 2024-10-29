#Limits of Lists for collections data
#   Whats wrong with the list on the slide??? 
#   Storing PID as an index, have a lot of empty items and takes up a lot of memory 

# Slide 2 
# how do you algorithmically find their assigned seat? 
#   Think of 2 tables as a group and chose a specific index (treat as directly related to one another)
#   Loook through all of the onyens, then go through all of the seats 

# Dictionaries 
#   Have the ability to decide how and what to idx data by unlike lists
#   Dictionaries are indexed by keys associated with values 
#       Unlike lists that are aleays zero-based, sequential, and integre indicies 

# Exploring dictionary syntax tgt

""" Examples of dictionary syntax with Ice CreamShop order tallies."""
ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# "" in dict_name  returns a bool to see if key is already in dict
# mutate dict = dict_name["new_key"] = value 
#   ex: 
#       ice_cream["pbj"] = 1
#       ice_cream["pbj"] +=10
#   ice_cream["pbj"] = returns value 

# len of dict = number ot key-value entries 

#Acess Values by subscription
#   mint_orders: int = ice_cream["mint"]
#    print(mint_orders)

#remove items by using pop method 
#   ice_cream/pop("strawberry")

#test if a key in the dictionary 
#   print("strawberry" in ice_cream)
#   print("vanilla" in ice_cream)

#Loop through items using for-in loops
#   for flavor in ice_cream:
#   tally: int = ice_cream[flavor]
#   print(f"{flavor} : {tally}"") -> prints each key and value 
#  (flavor = variable that has the same type as the key variable)

# Can't have same keys duplicated in dict 