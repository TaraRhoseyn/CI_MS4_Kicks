from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index


class TestHomeUrl(SimpleTestCase):
    """
    Tests home url is resolves to index view. 
    Credit for url unit testing: The Dumbfounds
    """
    
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)
