import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

path = kagglehub.competition_download("stanford-covid-vaccine")
print("Dataset downloaded to:", path)

train_path = os.path.join(path, "train.json")
train = pd.read_json(train_path, lines=True)

print("\nFirst 5 rows:")
print(train.head())

print("\nColumns:")
print(train.columns)

print("\nDataset info:")
print(train.info())

train["seq_length"] = train["sequence"].apply(len)

train["deg_50C_mean"] = train["deg_50C"].apply(lambda x: sum(x) / len(x))
train["deg_Mg_50C_mean"] = train["deg_Mg_50C"].apply(lambda x: sum(x) / len(x))

train["A_count"] = train["sequence"].apply(lambda x: x.count("A"))
train["U_count"] = train["sequence"].apply(lambda x: x.count("U"))
train["G_count"] = train["sequence"].apply(lambda x: x.count("G"))
train["C_count"] = train["sequence"].apply(lambda x: x.count("C"))

# 5. Show engineered features
print("\nEngineered features:")
print(
    train[
        [
            "id",
            "seq_length",
            "A_count",
            "U_count",
            "G_count",
            "C_count",
            "deg_50C_mean",
            "deg_Mg_50C_mean",
        ]
    ].head()
)

plt.scatter(train["seq_length"], train["deg_50C_mean"])
plt.xlabel("RNA Sequence Length")
plt.ylabel("Average Degradation at 50C")
plt.title("RNA Sequence Length vs Average Degradation")
plt.show()

plt.scatter(train["G_count"], train["deg_50C_mean"])
plt.xlabel("G Count")
plt.ylabel("Average Degradation at 50C")
plt.title("G Count vs Average Degradation")
plt.show()

output_file = "rna_features.csv"
train[
    [
        "id",
        "sequence",
        "seq_length",
        "A_count",
        "U_count",
        "G_count",
        "C_count",
        "deg_50C_mean",
        "deg_Mg_50C_mean",
    ]
].to_csv(output_file, index=False)

print(f"\nSaved cleaned dataset to {output_file}")

plt.scatter(train["G_count"], train["deg_50C_mean"])
plt.xlabel("G Count")
plt.ylabel("Avg Degradation")
plt.title("G Count vs Degradation")
plt.show()

train["G_ratio"] = train["G_count"] / train["seq_length"]

plt.scatter(train["G_ratio"], train["deg_50C_mean"])
plt.xlabel("G Ratio")
plt.ylabel("Avg Degradation")
plt.title("G Ratio vs Degradation")
plt.show()

print(train[[
    "A_count", "U_count", "G_count", "C_count",
    "deg_50C_mean"
]].corr())