import unittest
from car import Car

pilot = Car("Honda", "Pilot", 2010, 4)


class CarTest(unittest.TestCase):
    def test_wheel(self):
        self.assertEquals(pilot.wheel, 4)

    def test_model(self):
        self.assertEquals(pilot.model, "Pilot")

    def test_make(self):
        self.assertEquals(pilot.make, "Honda")


if __name__ == "__main__":
    unittest.main()
