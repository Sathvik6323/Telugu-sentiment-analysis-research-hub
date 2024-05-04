import pandas as pd
import random

# Load the first CSV file
df1 = pd.read_csv('book_neg.csv')

# Load the second CSV file
df2 = pd.read_csv('book_pos.csv')

# Merge the two dataframes by concatenating them
combined_df = pd.concat([df1, df2], ignore_index=True)

# Shuffle the rows of the combined dataframe
combined_df = combined_df.sample(frac=1).reset_index(drop=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('combined_book.csv', index=False)
