import pandas as pd
import re


def cheque(price_list, purchases):
    cheque_data = []

    for index, row in purchases.iterrows():
        product = row["product"]
        number = row["number"]
        price = price_list.get(product, 0)
        cost = price * number
        cheque_data.append([product, price, number, cost])

    cheque_df = pd.DataFrame(cheque_data, columns=["product", "price", "number", "cost"])
    cheque_df = cheque_df.sort_values(by="product")

    return cheque_df


def discount(cheque_df):
    discounted_cheque_df = cheque_df.copy()
    mask = discounted_cheque_df["number"] > 2
    discounted_cheque_df.loc[mask, "cost"] = discounted_cheque_df.loc[mask, "cost"] * 0.5

    return discounted_cheque_df


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words.sort()

    return words


def length_stats(cheque_df):
    words_lengths = []

    for index, row in cheque_df.iterrows():
        product = row["product"]
        words = preprocess_text(product)
        for word in words:
            words_lengths.append((word, len(word)))

    words_lengths_series = pd.Series(dict(words_lengths))

    return words_lengths_series


def get_long(cheque_df, max_length=None, min_quantity=None, min_price=None):
    filtered_cheque_df = cheque_df.copy()

    if max_length is not None:
        filtered_cheque_df = filtered_cheque_df[filtered_cheque_df["product"].str.len() <= max_length]

    if min_quantity is not None:
        filtered_cheque_df = filtered_cheque_df[filtered_cheque_df["number"] >= min_quantity]

    if min_price is not None:
        filtered_cheque_df = filtered_cheque_df[filtered_cheque_df["price"] >= min_price]

    return filtered_cheque_df


price_list = pd.read_csv("price_list.csv")
price_list = pd.Series(price_list["price"].values, index=price_list["product"])
purchases = pd.read_csv("purchases.csv")
cheque_df = cheque(price_list, purchases)

print("Исходный чек:")
print(cheque_df)

discounted_cheque_df = discount(cheque_df)
print("\nЧек со скидкой:")
print(discounted_cheque_df)

stats = length_stats(cheque_df)
print("\nСтатистика по длинам слов:")
print(stats)

filtered_cheque1 = get_long(cheque_df, max_length=6)
filtered_cheque2 = get_long(cheque_df, min_quantity=5)
filtered_cheque3 = get_long(cheque_df, min_price=4.0)

print("\nФильтрованный чек по максимальной длине названия товара (6 символов):")
print(filtered_cheque1)

print("\nФильтрованный чек по минимальному количеству купленных товаров (5 шт.):")
print(filtered_cheque2)

print("\nФильтрованный чек по минимальной цене товара (4.0 у.е.):")
print(filtered_cheque3)
