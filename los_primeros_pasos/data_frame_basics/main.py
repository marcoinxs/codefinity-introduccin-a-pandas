import pandas as pd 

# Creating a dictionary
animals_data = {'animal': ['Cat', 'Dog', 'Parrot', 'Cat', 'Parrot', 'Cat'],
           'name': ['Dolly', 'Abbey', 'Erin', 'Kelly', 'Taffy', 'Odie']}

# Write your code below
animals = pd.DataFrame(animals_data)

# Testing the result
print(animals)