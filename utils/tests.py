from .process_string import process_string
from django.test import TestCase


class StringProcessingTest(TestCase):
    def test_process_string(self):
        self.assertEqual("Unspecified", process_string("", ["example", "example"]))
        self.assertEqual(
            "example example example",
            process_string("example", ("example", "example")),
        )
