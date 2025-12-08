# Week 4 - Data Visualization (Matplotlib + Seaborn)

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample dataset
data = {
    "Age": [20, 22, 24, 21, 23, 22, 24, 25],
    "Marks": [85, 72, 90, 65, 88, 76, 92, 70],
    "Hours_Studied": [5, 3, 7, 2, 6, 4, 8, 3]
}

df = pd.DataFrame(data)

# 1. Histogram
plt.figure(figsize=(6,4))
plt.title("Marks Distribution")
sns.histplot(df["Marks"], kde=True)
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(6,4))
plt.title("Marks vs Hours Studied")
sns.scatterplot(x=df["Hours_Studied"], y=df["Marks"])
plt.show()

# 3. Line Plot
plt.figure(figsize=(6,4))
plt.title("Marks Trend")
plt.plot(df["Marks"], marker="o")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.show()

# 4. Heatmap
plt.figure(figsize=(6,4))
plt.title("Correlation Heatmap")
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()

# 5. Pairplot
sns.pairplot(df)
plt.show()
