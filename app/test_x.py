from django.test import TestCase

from .admin import some_admin_app, some_more_fun
class YourTestCase(TestCase):
    def test_example(self):
        # Your test logic here
        some_admin_app()
        some_more_fun()
        self.assertEqual(1 + 1, 2)