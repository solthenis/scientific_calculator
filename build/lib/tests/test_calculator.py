import unittest
import sys
import os

# Add the project's root directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator.calculator import CalculatorApp  # Updated import path

class TestCalculatorApp(unittest.TestCase):
    def test_initialization(self):
        app = CalculatorApp()
        self.assertIsInstance(app, CalculatorApp)

if __name__ == '__main__':
    unittest.main()
