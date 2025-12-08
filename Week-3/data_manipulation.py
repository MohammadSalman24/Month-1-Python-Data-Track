# Week 3 - NumPy and Pandas Data Manipulation

import numpy as np
import pandas as pd

# -------------------------
# 1. NumPy Array Operations
# -------------------------

arr = np.array([10, 20, 30, 40, 50])
print("NumPy Array:", arr)

print("Array Mean:", np.mean(arr))
print("Array Sum:", np.sum(arr))
print("Array Max:", np.max(arr))
print("Array Min:", np.min(arr))

# Broadcasting
arr2 = arr + 10
print("Array + 10:", arr2)

# -------------------------
# 2. Pandas DataFrame
# -------------------------

data = {
    "Name": ["Asha", "Ravi", "Neha", "Kiran"],
    "Marks": [85, 72, 90, 65],
    "Age": [20, 22, 21, 23]
}

df = pd.DataFrame(data)
print("\nPandas DataFrame:")
print(df)

# Filtering
print("\nStudents with marks > 75:")
print(df[df["Marks"] > 75])

# Calculating average marks
avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)

# Handling missing values
df_with_null = df.copy()
df_with_null.loc[2, "Marks"] = None

print("\nWith Missing Value:")
print(df_with_null)

df_filled = df_with_null.fillna(df_with_null["Marks"].mean())
print("\nAfter Filling Missing Value:")
print(df_filled)
