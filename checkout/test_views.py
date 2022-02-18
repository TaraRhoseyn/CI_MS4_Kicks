# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Third party
from django.test import TestCase
from django.contrib.auth.models import User

# Internal
from checkout.models import Order
from profiles.models import UserProfile

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class TestCheckoutViews(TestCase):
    """
    Tests checkout view
    """
    def setUp(self):
        """
        Create test users and a test order
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')
        test_user_superuser = User.objects.create_superuser(
            username='test_user_superuser', password='test_password')

        test_user.save()
        test_user_superuser.save()
        test_user = UserProfile.objects.get(user=test_user)

        Order.objects.create(
            full_name='Test User',
            email='test_email@gmail.com',
            phone_number='123456789',
            country='IE',
            town_or_city='Test City',
            street_address1='Test Address 1',
            street_address2='Test Address 2',
            user_profile=test_user
        )

    def tearDown(self):
        """
        Delete test orders
        """
        Order.objects.all().delete()
