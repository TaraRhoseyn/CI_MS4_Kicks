# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase

# Internal
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestBagViews(TestCase):
    """
    Testing bag views
    """
    def setUp(self):
        """
        Create a test product
        """
        Product.objects.create(
            name='testproduct',
            price='1.99',
            default_rating='3'
        )

    def tearDown(self):
        """
        Delete test product
        """
        Product.objects.all().delete()

    def test_get_bag(self):
        """
        Checks that the bag page is displayed
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
    
    def test_add_to_bag(self):
        """
        Checks that items have been added to bag
        """
        testproduct = Product.objects.get(name='testproduct')
        response = self.client.post(f'/bag/add/{testproduct.id}/',
                                    {"quantity": 1, 
                                    "redirect_url": "view_shopping_bag"})
        bag = self.client.session['bag']
        self.assertEqual(bag[str(testproduct.id)], 1)
    
    def test_remove_from_bag(self):
        """
        Checks that items have been removed from bag
        """
        testproduct = Product.objects.get(name='testproduct')
        self.client.post(f'/bag/add/{testproduct.id}/', {
            'quantity': 1,
            "redirect_url": "view_shopping_bag",
            "product_size": 1
        })
        response = self.client.post(f'/bag/remove/{testproduct.id}/',
                                    {"product_size": 1})
        bag = self.client.session['bag']
        self.assertEqual(bag, {})
