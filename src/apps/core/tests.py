from django.test import TestCase


class ExampleTestCase(TestCase):
    def test_simple(self):
        self.assertEqual(2 + 2, 4)
