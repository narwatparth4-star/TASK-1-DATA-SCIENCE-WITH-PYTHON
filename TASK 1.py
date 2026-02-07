import pandas as pd

# Load data
df = pd.read_csv("customers-100.csv")


# Basic cleanup


# Drop unnecessary index column
df = df.drop(columns=["Index"], errors="ignore")

# Strip whitespace from all string columns
df = df.apply(
    lambda col: col.str.strip() if col.dtype == "object" else col
)

# Standardize email
df["Email"] = df["Email"].str.lower()

# Parse subscription date
df["Subscription Date"] = pd.to_datetime(
    df["Subscription Date"], errors="coerce"
)

# Phone number cleanup

phone_cols = ["Phone 1", "Phone 2"]
for col in phone_cols:
    df[col] = (
        df[col]
        .str.replace(r"[^\d+]", "", regex=True)  # keep digits and +
        .replace("", pd.NA)
    )

# Remove duplicates

df = df.drop_duplicates(subset=["Customer Id"])


# Sort data

df = df.sort_values(
    by=["Last Name", "First Name"],
    ascending=True
).reset_index(drop=True)


# Final result

print(df.head())

df.to_csv("customers_cleaned_sorted.csv", index=False)
