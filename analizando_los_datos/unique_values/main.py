import pandas as pd

cars_data = {'model': ['audi A1', 'audi A6', 'audi A4', 'audi A3','audi A1'],
          'year': [2017, 2016, 2017, 2019, 2016],
          'fueltype': ['petrol', 'diesel', 'diesel', 'petrol', 'petrol'],
          'capital': ['Manila', 'Monaco', 'Bangkok', 'Stockhol', 'Valletta']}

audi_cars = pd.DataFrame(cars_data)

# Obtener todos los valores distintos de la columna 'year' y almacenarlos en la variable unique_years.
unique_years = audi_cars['year'].unique()
# Obtener todos los valores distintos de la columna 'fueltype' y almacenarlos en la variable unique_fueltype.
unique_fueltype = audi_cars['fueltype'].unique()
# Determinar el número de tipos de combustible únicos en la columna 'fueltype' utilizando el método .nunique() 
# y guardar el resultado en la variable count_unique_fueltypes.
count_unique_fueltypes = audi_cars['fueltype'].nunique()

# Testing the result
print(unique_years)
print(unique_fueltype)
print(count_unique_fueltypes)

