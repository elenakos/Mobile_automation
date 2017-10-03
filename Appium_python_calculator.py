import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class CalculatorAndroidTests(unittest.TestCase):
    
    def setUp(self):
        dc = {}
        dc['platformName'] = 'Android'
        dc['platformVersion'] = '7.0'
        dc['deviceName'] = 'Moto_G__5__Plus'
        dc['appPackage'] = 'com.google.android.calculator'
        dc['appActivity'] = 'com.android.calculator2.Calculator'
        self.d = webdriver.Remote('http://localhost:4723/wd/hub', dc)    
        sleep(2)

    def tearDown(self):
        self.d.quit()

    def test_square_root_operation_for_valid_input_returns_valid_result(self):
        d9 = self.d.find_element_by_id('digit_9')
        eq = self.d.find_element_by_id('eq')
        arrow = self.d.find_element_by_id('arrow')
        arrow.click()
        sqr_root = self.d.find_element_by_id('op_sqrt')
        sqr_root.click()
        
        swipe = TouchAction(self.d)
        swipe.press(x=275, y=1280).move_to(x=689, y=10).release().perform()
        
        d9.click()
        eq.click()
        res = self.d.find_element_by_id('result')
        self.assertIn('3', res.text)
            
        
    def test_addition_opearation_for_valid_input_integers_returns_valid_integer_result(self):
        d0 = self.d.find_element_by_id('digit_0')
        d1 = self.d.find_element_by_id('digit_1')
        d2 = self.d.find_element_by_id('digit_2')
        d3 = self.d.find_element_by_id('digit_3')
        d4 = self.d.find_element_by_id('digit_4')
        d5 = self.d.find_element_by_id('digit_5')
        d6 = self.d.find_element_by_id('digit_6')
        d7 = self.d.find_element_by_id('digit_7')
        d8 = self.d.find_element_by_id('digit_8')
        d9 = self.d.find_element_by_id('digit_9')

        plus = self.d.find_element_by_id('op_add')
        minus = self.d.find_element_by_id('op_sub')
        divide = self.d.find_element_by_id('op_div')
        multiply = self.d.find_element_by_id('op_mul')
        
        eq = self.d.find_element_by_id('eq')
        point = self.d.find_element_by_id('dec_point') 
     
        delete = self.d.find_element_by_id('del')
        
        formula = self.d.find_element_by_id('formula')
        res = self.d.find_element_by_id('result')

        d7.click()
        plus.click()
        f = formula.text
        self.assertIn('7+', f)
        d3.click()
        f = formula.text
        self.assertIn('7+3', f)
        self.assertIn('10', res.text)
        eq.click()
        r = res.text
        self.assertIn('10', r)
        

    def test_addition_opearation_for_valid_input_floats_returns_valid_float_result(self):
        d0 = self.d.find_element_by_id('digit_0')
        d1 = self.d.find_element_by_id('digit_1')
        d2 = self.d.find_element_by_id('digit_2')
        d3 = self.d.find_element_by_id('digit_3')
        d4 = self.d.find_element_by_id('digit_4')
        d5 = self.d.find_element_by_id('digit_5')
        d6 = self.d.find_element_by_id('digit_6')
        d7 = self.d.find_element_by_id('digit_7')
        d8 = self.d.find_element_by_id('digit_8')
        d9 = self.d.find_element_by_id('digit_9')

        plus = self.d.find_element_by_id('op_add')
        minus = self.d.find_element_by_id('op_sub')
        divide = self.d.find_element_by_id('op_div')
        multiply = self.d.find_element_by_id('op_mul')
        
        eq = self.d.find_element_by_id('eq')
        point = self.d.find_element_by_id('dec_point') 
     
        delete = self.d.find_element_by_id('del')
        
        formula = self.d.find_element_by_id('formula')
        res = self.d.find_element_by_id('result')
        
        d2.click()
        d4.click()
        point.click()
        d6.click()
        plus.click()
        f = formula.text
        self.assertIn('24.6+', f)
        d8.click()
        d1.click()
        d0.click()
        point.click()
        d5.click()
        f = formula.text
        self.assertIn('24.6+810.5', f)
        r = res.text
        self.assertIn('835.1', r)
        eq.click()
        r = res.text
        self.assertIn('835.1', r)


    def test_subtraction_opearation_for_valid_input_integers_returns_valid_integer_result(self):
        d0 = self.d.find_element_by_id('digit_0')
        d1 = self.d.find_element_by_id('digit_1')
        d2 = self.d.find_element_by_id('digit_2')
        d3 = self.d.find_element_by_id('digit_3')
        d4 = self.d.find_element_by_id('digit_4')
        d5 = self.d.find_element_by_id('digit_5')
        d6 = self.d.find_element_by_id('digit_6')
        d7 = self.d.find_element_by_id('digit_7')
        d8 = self.d.find_element_by_id('digit_8')
        d9 = self.d.find_element_by_id('digit_9')

        plus = self.d.find_element_by_id('op_add')
        minus = self.d.find_element_by_id('op_sub')
        divide = self.d.find_element_by_id('op_div')
        multiply = self.d.find_element_by_id('op_mul')
        
        eq = self.d.find_element_by_id('eq')
        point = self.d.find_element_by_id('dec_point') 
     
        delete = self.d.find_element_by_id('del')
        
        formula = self.d.find_element_by_id('formula')
        res = self.d.find_element_by_id('result')

        d9.click()
        d9.click()
        minus.click()
        d3.click()
        self.assertEqual('96', res.text)
        eq.click()
        self.assertEqual('96', res.text)
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


