# COFI Checkout package

## Description
Package contains an unique class named Checkout:
- Properties:
    - total_amount: final price of scanned products with applied discounts
    - products: list of products (code, name and price)
    - discounts: list of discounts (discount name)
    
- Public methods:
    - scan [(product: str) -> None]: includes new products to the Checkout object
    - total [() -> float] : apply discounts and return final price


### Discount logic
Discounts are included in the data json. The order here is important since it will affect which discount is applied in the case in which several can be applied at the same time. An attempt will be made to apply the first discount as many times as possible, once it cannot be applied, the next discount will be passed and the process will be repeated until the discounts are exhausted.

A discount is collected as a JSON object and consists of 'name' (str), 'items' (json object that indicates the amount needed for each item to apply the discount) and 'amount' (float that indicates the total discount to apply).

## Data modification (Products and Discounts)
Data is contained in
 ```
data/products_and_discounts.json
```
This file could be modified.

## Testing
Execute pytest into the folder
