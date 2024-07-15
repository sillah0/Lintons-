#!/usr/bin/python3

def average_purchase(customers):
    total_purchase = sum(amount for name, amount in customers)
    average_purchase = total_purchase / len(customers) if customers else 0
    return average_purchase

#sample list of customer names and their purchases
customers = [
    ('Jane', 15000),
    ('Dennis', 8000),
    ('Diana', 22000),
    ('Arnold', 11000),
    ('James', 5000)
]

print(f'Average purchase amount: {average_purchase(customers)}')
