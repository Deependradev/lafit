from django.test import TestCase

from .admin import some_admin_app
class YourTestCase(TestCase):
    def test_example(self):
        # Your test logic here
        some_admin_app()
        self.assertEqual(1 + 1, 2)