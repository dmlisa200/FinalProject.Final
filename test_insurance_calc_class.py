import unittest
from insurance_calc_class import LifeInsuranceCalculator


class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = self.calculator.Calculator()

    def tearDown(self):
        del self.calculator

    def test_income_value(self):
        self.assertTrue(self.calculator.income_value, 150000)

    def test_income_value_invalid(self):
        self.assertTrue(self.calculator.income_value, 'wer')

    def test_other_inc_value(self):
        self.assertTrue(self.calculator.other_inc_value, 50000)

    def test_other_inc_value_invalid(self):
        self.assertTrue(self.calculator.other_inc_value, 'wer')

    def test_answer(self):
        self.assertEqual(self.calculator.answer, 'Y')

    def test_answer_no(self):
        self.assertEqual(self.calculator.answer, 'n')

    def test_debt(self):
        self.assertTrue(self.calculator.debt, 350000)

    def test_debt_invalid(self):
        self.assertTrue(self.calculator.debt, 'wer')

    def test_savings(self):
        self.assertTrue(self.calculator.savings, 50000)

    def test_savings_invalid(self):
        self.assertTrue(self.calculator.savings, 'wer')

    def test_retirement(self):
        self.assertTrue(self.calculator.retirement, 400000)

    def test_retirement_invalid(self):
        self.assertTrue(self.calculator.retirement, 'wer')

    def test_present_amount(self):
        self.assertTrue(self.calculator.present_amount, 100000)

    def test_present_amount_invalid(self):
        self.assertTrue(self.calculator.present_amount, 'wer')



if __name__ == '__main__':
    unittest.main()
