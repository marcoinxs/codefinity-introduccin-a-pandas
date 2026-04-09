import pandas as pd
import numpy as np

# This line ensures that the results are reproducible
np.random.seed(5)

wine_data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv')

# Extraer las primeras 10 filas de este DataFrame y almacenar el resultado en la variable first_lines.
first_lines = wine_data.head(10)
# Recuperar las últimas 15 filas de este DataFrame y almacenar el resultado en la variable last_lines.
last_lines  = wine_data.tail(15)
# Seleccionar una muestra aleatoria de 12 filas de este DataFrame y almacenar el resultado en la variable random_rows.
random_rows = wine_data.sample(12)

# Testing the result
print(first_lines)
print(last_lines)
print(random_rows)