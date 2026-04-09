import pandas as pd

cars_data = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'capital': ['Manila', 'Monaco', 'Bangkok', 'Stockhol', 'Valletta']}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
audi_cars = audi_cars.drop(columns = ['capital'])

# Testing the result
print(audi_cars)