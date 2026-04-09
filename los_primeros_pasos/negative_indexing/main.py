import pandas as pd

cars_data = {'model': ['Audi A1', 'Audi A6', 'Audi A4', 'Audi A3','Audi A1'],
             'year': [2017, 2016, 2017, 2019, 2016],
             'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
             'price': [12500, 16500, 16800, 17300, 13900]}

audi_cars = pd.DataFrame(cars_data)

# 1. Audi A1 2017 está en la posición 0
audi_A1_2017 = audi_cars.iloc[0]
# 2. Audi A1 2016 está en la posición 4
audi_A1_2016 = audi_cars.iloc[4]
# 3. Audi A3 está en la posición 3
audi_A3 = audi_cars.iloc[3]

# Testing the result
print(audi_A1_2017)
print(audi_A1_2016)
print(audi_A3)