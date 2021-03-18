from leapyear import LeapYear
import unittest


class TestLeapYear(unittest.TestCase):
    def test_can_be_instantiated(self):
        LeapYear()

    def test_can_take_a_year_as_argument(self):
        LeapYear().is_leapyear(2020)

    def test_throws_error_on_non_integer_year(self):
        with self.assertRaises(ValueError):
            LeapYear().is_leapyear("Bodor")

        with self.assertRaises(ValueError):
            LeapYear().is_leapyear(2020.2)

        with self.assertRaises(ValueError):
            LeapYear().is_leapyear(True)

    def test_returns_value(self):
        self.assertIsNotNone(LeapYear().is_leapyear(2020))

    def test_2021_is_leapyear(self):
        self.assertFalse(LeapYear().is_leapyear(2021))

    def test_0_is_leapyear(self):
        self.assertTrue(LeapYear().is_leapyear(0))

    def test_minus_4_is_leapyear(self):
        self.assertTrue(LeapYear().is_leapyear(-4))

    def test_100_is_not_leapyear(self):
        self.assertFalse(LeapYear().is_leapyear(100))

    def test_400_is_still_a_leapyear(self):
        self.assertTrue(LeapYear().is_leapyear(400))

    def test_2020_is_leapyear(self):
        self.assertTrue(LeapYear().is_leapyear(2020))

    def test_2000_is_leapyear(self):
        self.assertTrue(LeapYear().is_leapyear(2000))

if __name__ == '__main__':
    unittest.main()  # pragma: no cover
