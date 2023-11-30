from unittest import TestCase

from sensor_monitoring.services.main import is_valid_value
from sensor_monitoring.validators import TemperatureValidator
from sensor_monitoring.models import Range


class TestValidation(TestCase):
    validator = TemperatureValidator(
        valid_range=Range(min=5, max=10)
    )

    def test_within_range(self):
        self.assertTrue(is_valid_value(self.validator, 7))

    def test_leftmost_inclusive(self):
        self.assertTrue(is_valid_value(self.validator, 5))

    def test_rightmost_inclusive(self):
        self.assertTrue(is_valid_value(self.validator, 10))

    def test_leftmost_out_of_range(self):
        self.assertFalse(is_valid_value(self.validator, 3))

    def test_rightmost_out_of_range(self):
        self.assertFalse(is_valid_value(self.validator, 12))
