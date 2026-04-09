import pandas as pd

cars_data = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'price': [12500, 16500, 16800, 17300, 13900]}

audi_cars = pd.DataFrame(cars_data)

# Write your code below
audi_A1_2017 = audi_cars[(audi_cars['model'] == 'Audi A1') & (audi_cars['year'] == 2017)]
audi_A1_2016 = audi_cars[(audi_cars['model'] == 'Audi A1') & (audi_cars['year'] == 2016)]
audi_A3 = audi_cars[audi_cars['model'] == 'Audi A3']
                    
# Testing the result
print(audi_A1_2017)
print(audi_A1_2016)
print(audi_A3)