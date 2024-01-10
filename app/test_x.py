from django.test import TestCase

from .admin import some_admin_app, some_more_fun

from .models import Author


class TestAuthor(TestCase):
    def test_some(self):
        author = Author('justin')
        author.get_all_books()
        author.get_all_names()

class YourTestCase(TestCase):
    def test_example(self):
        # Your test logic here
        some_admin_app()
        some_more_fun()
        self.assertEqual(1 + 1, 2)