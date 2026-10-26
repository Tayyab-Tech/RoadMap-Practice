import pandas as pd

data = {
    "OrderID": [101, 102, 103, 102, 104, 105, 105],
    "Customer": [
        "Ali", "Sara", "Ahmed", "Sara",
        "Zain", "Ayesha", "Ayesha"
    ],
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Mouse",
        "Monitor", "Phone", "Phone"
    ],
    "Amount": [100000, 2000, 4000, 2000, 25000, 80000, 80000]
}

df = pd.DataFrame(data)

print(df)




print("\nCount duplicates : \n")
print(df.duplicated().sum())


print("\n Display duplicate rows : \n")

duplicates = df[df.duplicated()]
print(duplicates)


print("\n Display all copies of duplicate records : \n")

all_duplicates = df[df.duplicated(keep=False)]

# print(all_duplicates)


# Mark later occurrences as duplicates
print(df[df.duplicated(keep="first")])

# Mark earlier occurrences as duplicates
print(df[df.duplicated(keep="last")])



print("\n Remove exact duplicates : \n")
clean_df = df.drop_duplicates()
print(clean_df)

print("Rows before:", len(df))
print("Rows after:", len(clean_df))
print("Rows removed:", len(df) - len(clean_df))