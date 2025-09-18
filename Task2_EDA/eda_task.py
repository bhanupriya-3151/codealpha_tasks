import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("train.csv")
print("✅ Dataset Loaded Successfully!")
print()

# Step 2: Display first 5 rows
print("🔍 First 5 Rows:")
print(df.head())
print()

# Step 3: Dataset Info
print("📊 Dataset Info:")
print(df.info())
print()

# Step 4: Check Missing Values
print("❓ Missing Values Count:")
print(df.isnull().sum())
print()

# Step 5: Basic Statistics
print("📈 Basic Statistics:")
print(df.describe())
print()

# Step 6: Count how many survived
print("❤️ Survival Count:")
print(df['Survived'].value_counts())
import matplotlib.pyplot as plt
import seaborn as sns

# 1️⃣ Survival Count
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

# 2️⃣ Survival by Gender
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()

# 3️⃣ Survival by Passenger Class
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Passenger Class")
plt.show()
