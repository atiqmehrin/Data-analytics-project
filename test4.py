# Sample DataFrames
import pandas as pd
import numpy as np
df_1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df_2 = pd.DataFrame({'ID': [2, 3, 4], 'Department': ['HR', 'IT', 'Finance']})

# Outer Join
df_outer = pd.merge(df_1, df_2, on='ID', how='outer'
                    )
print(df_outer)