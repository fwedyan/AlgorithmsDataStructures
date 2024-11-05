inventory = {"apples": 430, "bananas": 312, 
             "oranges": 525, "pears": 217}
#A new shipment of bananas arriving 
inventory["bananas"] += 200
print(inventory)

for k in inventory.keys():   # The order of the k's is not defined
   print("Got key", k, "which maps to value", inventory[k])

ks = list(inventory.keys()) #deep copy, using list construcotr
l2 =inventory.keys() #shallow copy
print(ks)

inventory["strawburries"] = 500
print(inventory)
print(ks)
print(l2)

