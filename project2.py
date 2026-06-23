import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Step 1: Load dataset from local file
    df = pd.read_csv("data.csv", encoding="latin1", on_bad_lines="skip")

    # Step 2: Clean dataset
    df = df.dropna().reset_index(drop=True)

    # Step 3: Export cleaned dataset
    df.to_csv("cleaned_data.csv", index=False)
    print("✅ Cleaned sales dataset exported successfully!")

    # Step 4: Summary statistics
    print("\n📊 Summary Statistics:")
    print(df.describe())

    # Step 5: Visualizations
    plt.figure(figsize=(8,5))
    sns.histplot(df["Price"], bins=10, kde=True)
    plt.title("Distribution of Product Prices")
    plt.show()

    plt.figure(figsize=(8,5))
    sns.boxplot(x=df["Quantity"])
    plt.title("Boxplot of Quantities Sold")
    plt.show()

    plt.figure(figsize=(10,5))
    sns.scatterplot(x=df["Date"], y=df["Price"], hue=df["Category"])
    plt.title("Sales Price Trends Over Time")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()