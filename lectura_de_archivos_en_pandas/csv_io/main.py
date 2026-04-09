import pandas as pd

file_url = 'https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv'

# Write your code below
wine_data = pd.read_csv(file_url)

# Testing the result
print(wine_data)

