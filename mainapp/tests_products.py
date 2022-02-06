from django.test import TestCase
from mainapp.models import Product, ProductCategory


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="футболки")
        self.product_1 = Product.objects.create(name="футболка Роналду",
                                                category=category,
                                                price=1100,
                                                quantity=200)

        self.product_2 = Product.objects.create(name="бейсболки",
                                                category=category,
                                                price=1100,
                                                quantity=130,
                                                is_active=True)

        self.product_3 = Product.objects.create(name="cумки",
                                                category=category,
                                                price=1500,
                                                quantity=125)

    def test_product_get(self):
        product_1 = Product.objects.get(name="футболки")
        product_2 = Product.objects.get(name="бейсболки")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="футболки")
        product_2 = Product.objects.get(name="бейсболки")
        self.assertEqual(str(product_1), 'Роналду (футболки)')
        self.assertEqual(str(product_2), 'сумка Роналду (сумка)')