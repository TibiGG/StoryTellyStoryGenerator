# Python program to demonstrate
# Conversion of JSON data to
# dictionary# importing the module
import json  # Opening JSON file

with open('data.json') as json_file:
    data = json.load(json_file)  # for reading nested data [0] represents
    # the index value of the list
    print(data['dictionary'][0])  # for printing the key-value pair of
    # nested dictionary for loop can be used
    print("\nPrinting nested dictionary as a key-value pair\n")
    for i in data['dictionary']:
        print("tags:", i['tags'])
        print("story:", i['story'])
        print()
