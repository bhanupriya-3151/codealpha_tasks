import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("train.csv")

# 1️⃣ Count of passengers by class
sns.countplot(x="Pclass", data=df)
plt.title("Passengers by Class")
plt.show()

# 2️⃣ Survival by Gender
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()

# 3️⃣ Age distribution
sns.histplot(df["Age"].dropna(), bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

# 4️⃣ Fare distribution
sns.histplot(df["Fare"], bins=20, kde=True)
plt.title("Fare Distribution")
plt.show()

# 5️⃣ Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
