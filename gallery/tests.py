from django.test import TestCase
from .models import Category,Image,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.travel= Category(name = 'Travel')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))

    # Testing Save Method
    def test_save_method(self):
        self.travel.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.travel.save_category()
        self.travel.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

    # Testing Update Method
    def test_update(self):
        category = Category.get_category_id(self.category.id)
        category.update_category('Food')
        category = Category.get_category_id(self.category.id)
        self.assertTrue(category.name == 'Food')

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.kenya= Location(name = 'Kenya')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.kenya,Location))

    # Testing Save Method
    def test_save_method(self):
        self.kenya.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.kenya.save_location()
        self.kenya.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

    # Testing Update Method
    def test_update(self):
        location = Location.get_location_id(self.location.id)
        location.update_location('Asia')
        location = Location.get_location_id(self.location.id)
        self.assertTrue(location.name == 'Asia')

class ImageTestClass(TestCase):
    # Setup Method
    def setUp(self):
        self.category = Category(name= 'Travel')
        self.category.save_category()
        
        self.location = Location(name = 'Kenya')
        self.location.save_location()

        self.image = Image()