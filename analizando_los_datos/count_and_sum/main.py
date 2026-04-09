import pandas as pd 

cars_data = {'model': [None, 'audi A6', 'audi A4', None, 'audi A1'],
             'year': [2017, 2016, 2017, None, 2016],
             'fueltype': [None, 'diesel', 'diesel', 'petrol', 'petrol'],
             'price': [12500, 16500, 16800, 17300, 16500]}

audi_cars = pd.DataFrame(cars_data)

# Obtener el recuento de celdas no nulas en cada columna y almacenar el resultado en la variable number_of_cells.
number_of_cells = audi_cars.count()
# Calcular el precio total (utilizando la columna 'price') de todos los autos en el DataFrame y almacenar el resultado en la variable total_price.
total_price = audi_cars['price'].sum()
# Identificar la cantidad de valores faltantes en cada columna y almacenar el resultado en la variable null_count.
null_count = audi_cars.isna().sum()

# Testing the result
print('Missing values:')
print(null_count)
print('Number of non-null cells:')
print(number_of_cells)
print(f'Total price: {total_price}')