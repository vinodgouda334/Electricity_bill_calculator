import unittest
from electricity_bill import (
    validate_units,
    energy_charge,
    fixed_charge,
    tax_amount,
    total_bill,
)


class TestElectricityBillCalculator(unittest.TestCase):
    def test_validate_units_valid(self):
        self.assertEqual(validate_units(0), 0)
        self.assertEqual(validate_units(150), 150)
        self.assertEqual(validate_units(10000), 10000)

    def test_validate_units_invalid(self):
        with self.assertRaises(ValueError):
            validate_units(-1)
        with self.assertRaises(ValueError):
            validate_units(10001)

    def test_energy_charge_slabs(self):
        self.assertAlmostEqual(energy_charge(0), 0.0)
        self.assertAlmostEqual(energy_charge(100), 150.0)
        self.assertAlmostEqual(energy_charge(150), 275.0)
        self.assertAlmostEqual(energy_charge(250), 600.0)
        self.assertAlmostEqual(energy_charge(350), 1100.0)

    def test_fixed_charge(self):
        self.assertEqual(fixed_charge(120), 50.0)
        with self.assertRaises(ValueError):
            fixed_charge(-5)

    def test_tax_amount(self):
        # 5% of energy_charge(200) -> 5% of 400.0 = 20.0
        self.assertAlmostEqual(tax_amount(200), 20.0)

    def test_total_bill(self):
        # For 200 units: energy = 400.0, fixed = 50.0, tax = 20.0 -> total = 470.0
        self.assertAlmostEqual(total_bill(200), 470.0)


if __name__ == "__main__":
    unittest.main()
