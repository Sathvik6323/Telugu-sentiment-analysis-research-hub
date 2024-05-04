
import pandas as pd

# Read each CSV file into a pandas DataFrame
df1 = pd.read_csv('combined_book.csv')
df2 = pd.read_csv('combined_movie.csv')
df3 = pd.read_csv('combined_product.csv')

# Concatenate the DataFrames
merged_df = pd.concat([df1, df2, df3], ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv('merged_file.csv', index=False)
