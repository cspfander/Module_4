"""
Program: nested_if_statement.py
Author: Colten Pfander
Last date modified: 9/16/2019



The purpose of this program is to write a function that will accept the amount of the purchase,
the cash coupon, the percent coupon, and calculate and return the total order item.
"""


def calculate_order(price, cash_coupon, percent_coupon):
    tax_rate = 0.06
    if price < 10:
        shipping = 5.95
        if cash_coupon == 5:
            price = price - cash_coupon
            price = price - (price * percent_coupon)
            total_order = price + (price * tax_rate) + shipping
            return round(total_order, 2)
        if cash_coupon == 10:
            price = 0
            total_order = price + shipping
            return round(total_order, 2)


if __name__ == '__main__':
    print(calculate_order())
