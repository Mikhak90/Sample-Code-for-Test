import unittest
from parking import Parking

parking = Parking()
class TestEcho(unittest.TestCase):
    
    def test_repeat(self):
      self.assertEqual(parking.check_availability(), True)
      self.assertEqual(parking.leave_parking(), True)

if __name__ == '__main__':
    unittest.main()