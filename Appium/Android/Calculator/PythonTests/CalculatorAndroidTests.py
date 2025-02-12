import unittest
from appium import webdriver
from appium.webdriver.webdriver import AppiumOptions
from CalculatorPOM import CalculatorPOM
from CalculatorTestSetup import CalculatorTestSetup

class CalculatorAndroidTests(unittest.TestCase):

    def setUp(self):
        self.calcSetup = CalculatorTestSetup()
        desired_capabilities = {}
        desired_capabilities['appium:platformName'] = self.calcSetup.PLATFORM_NAME
        desired_capabilities['appium:platformVersion'] = self.calcSetup.PLATFORM_VERSION
        desired_capabilities['appium:automationName'] = self.calcSetup.AUTOMATION_NAME
        desired_capabilities['appium:deviceName'] = self.calcSetup.DEVICE_NAME
        desired_capabilities['appium:appPackage'] = self.calcSetup.APP_PACKAGE
        desired_capabilities['appium:appActivity'] = self.calcSetup.APP_ACTIVITY

        # Converts capabilities to AppiumOptions instance
        appium_options = AppiumOptions().load_capabilities(desired_capabilities)

        self.driver = webdriver.Remote(self.calcSetup.HOST, options=appium_options)
        self.calc = CalculatorPOM(self.driver)
        
    def tearDown(self):
        self.driver.quit()

    def test_square_root_operation_for_valid_input_returns_valid_result(self):
        self.calc.enter_square_root()
        self.calc.enter_number('9')
        self.calc.enter_equal()
        result = self.calc.get_final_result()
        self.assertIn('3', result)
            
    def test_addition_operation_for_valid_input_integers_returns_valid_integer_result(self):
        self.calc.enter_number('7')
        self.calc.enter_plus()
        formula = self.calc.get_formula()
        self.assertIn('7+', formula)
        self.calc.enter_number('3')
        formula = self.calc.get_formula()
        self.assertIn('7+3', formula)
        result = self.calc.get_result()
        self.assertIn('10', result)
        self.calc.enter_equal()
        result = self.calc.get_final_result()
        self.assertIn('10', result)

    def test_addition_operation_for_valid_input_floats_returns_valid_float_result(self):
        self.calc.enter_number('24.6')
        self.calc.enter_plus()
        formula = self.calc.get_formula()
        self.assertIn('24.6+', formula)
        self.calc.enter_number('810.5')
        formula = self.calc.get_formula()
        self.assertIn('24.6+810.5', formula)
        result =  self.calc.get_result()
        self.assertIn('835.1', result)
        self.calc.enter_equal()
        result = self.calc.get_final_result()
        self.assertIn('835.1', result)

    def test_subtraction_operation_for_valid_input_integers_returns_valid_integer_result(self):
        self.calc.enter_number('99')
        self.calc.enter_minus()
        self.calc.enter_number('3')
        result = self.calc.get_result()
        self.assertEqual('96', result)
        self.calc.enter_equal()
        result = self.calc.get_final_result()
        self.assertEqual('96', result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
