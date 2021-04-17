import unittest

from .. import Checkout


class MyTest(unittest.TestCase):

    def setUp(self):
        self.new_checkout = Checkout()

    def test_empty_scan(self):
        # Case 1 - Empty scan
        with self.assertRaises(Exception):
            self.new_checkout.scan('')

    def test_invalid_code_scan(self):
        # Case 2 - Invalid code
        with self.assertRaises(Exception):
            self.new_checkout.scan('INVALID_CODE')

    def test_several_products_and_discounts(self):
        data_set = [
            # items | expected_amount | msg
            {'items': ['VOUCHER', 'TSHIRT'], 'expected_amount': 25.0, 'msg': 'Case 3 - Scan without discounts'},
            {'items': ['VOUCHER', 'VOUCHER'], 'expected_amount': 5.0, 'msg': 'Case 4 - 2x1 VOUCHER discount'},
            {'items': ['TSHIRT', 'TSHIRT', 'TSHIRT'], 'expected_amount': 57.0, 'msg': 'Case 5 - bulk TSHIRT discount'},
            {'items': ['VOUCHER', 'TSHIRT', 'MUG'], 'expected_amount': 25.0, 'msg': 'Case 6 - SWAG discount'},
            {'items': ['VOUCHER', 'VOUCHER', 'VOUCHER', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'MUG'],
             'expected_amount': 87.0, 'msg': 'Case 7 - All discounts'},
            {'items': ['VOUCHER', 'VOUCHER', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'MUG'],
             'expected_amount': 70.0, 'msg': 'Case 8 - One discount with more products'},
            {'items': ['VOUCHER', 'VOUCHER', 'VOUCHER', 'VOUCHER', 'VOUCHER', 'VOUCHER'],
             'expected_amount': 15.0, 'msg': 'Case 9 - 2x1 VOUCHER discount x3'},
        ]

        for data_row in data_set:
            with self.subTest():
                self.setUp()
                [self.new_checkout.scan(item) for item in data_row['items']]
                self.assertEqual(data_row['expected_amount'], self.new_checkout.total(), msg=data_row['msg'])

    def test_total_before_scan(self):
        # Case 10 - scan, total, scan and total
        self.new_checkout.scan('VOUCHER')
        self.assertEqual(5, self.new_checkout.total())
        self.new_checkout.scan('VOUCHER')
        self.assertEqual(5, self.new_checkout.total())
        self.new_checkout.scan('VOUCHER')
        self.assertEqual(10, self.new_checkout.total())
