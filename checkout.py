import json
import pkg_resources

# Products and discounts from a JSON file
with pkg_resources.resource_stream(__name__, 'data/products_and_discounts.json') as data_json:
    data = json.load(data_json)
    PRODUCTS = data['PRODUCTS']
    DISCOUNTS = data['DISCOUNTS']

AVAILABLE_CODES = [x['code'] for x in PRODUCTS]
CODE_EXCEPTION = Exception('CODE NOT VALID')


class Checkout:
    """COFI checkout class

    PROPERTIES:
    total_amount: float
    products: str[]
    discounts: str[]
    """

    def __init__(self):
        self.total_amount = None
        self.products = []
        self.discounts = []

    def _apply_discounts(self) -> float:
        discount_amount = 0
        list_products = [product['code'] for product in self.products]

        for discount in DISCOUNTS:
            # Group required codes as many times as it be required
            list_item_required = []
            for item in discount['items']:
                for i in range(discount['items'][item]):
                    list_item_required.append(item)

            # Aux variable to check codes for every discount
            list_product_temp = list_products[:]

            # While loop to check the same discount as manny as possible
            loop_running = True
            while loop_running:
                for item_required in list_item_required:
                    if item_required in list_product_temp:
                        list_product_temp.remove(item_required)
                    else:
                        loop_running = False
                        break
                else:
                    list_products = list_product_temp[:]
                    self.discounts.append(discount['name'])
                    discount_amount += discount['amount']
        return discount_amount

    def scan(self, code: str) -> None:
        """Use to add products to the checkout object
        scan(product: str) -> None"""
        if code not in AVAILABLE_CODES:
            raise CODE_EXCEPTION

        # Scanning new products, discounts should be checked again
        if self.total_amount:
            self.total_amount = 0

        product = next(x for x in PRODUCTS if x['code'] == code)
        self.products.append(product)

    def total(self) -> float:
        """Use to apply discounts and calculate final price
        total() -> final_price: float"""
        if self.total_amount:
            return self.total_amount

        # Sum of all product prices without discounts
        product_amount = sum(x['price'] for x in self.products)

        # Sum of discounts
        discount_amount = self._apply_discounts()

        self.total_amount = product_amount + discount_amount
        return self.total_amount
