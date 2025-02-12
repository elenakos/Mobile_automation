import re
from selenium.webdriver.common.by import By
'''
Calculator Page Object class
'''

class CalculatorPOM:
    # all elements from the page as defined in the  code
    DIGIT_0 = 'com.google.android.calculator:id/digit_0'
    DIGIT_1 = 'com.google.android.calculator:id/digit_1'
    DIGIT_2 = 'com.google.android.calculator:id/digit_2'
    DIGIT_3 = 'com.google.android.calculator:id/digit_3'
    DIGIT_4 = 'com.google.android.calculator:id/digit_4'
    DIGIT_5 = 'com.google.android.calculator:id/digit_5'
    DIGIT_6 = 'com.google.android.calculator:id/digit_6'
    DIGIT_7 = 'com.google.android.calculator:id/digit_7'
    DIGIT_8 = 'com.google.android.calculator:id/digit_8'
    DIGIT_9 = 'com.google.android.calculator:id/digit_9'
    DECIMAL_POINT = 'com.google.android.calculator:id/dec_point'
    OPERATION_PLUS = 'com.google.android.calculator:id/op_add'
    OPERATION_MINUS = 'com.google.android.calculator:id/op_sub'
    OPERATION_DIVIDE = 'com.google.android.calculator:id/op_div'
    OPERATION_MULTIPLY = 'com.google.android.calculator:id/op_mul'
    OPERATION_DEL = 'com.google.android.calculator:id/del'
    OPERATION_EQUAL = 'com.google.android.calculator:id/eq'
    ARROW = 'com.google.android.calculator:id/collapse_expand'
    FORMULA = 'com.google.android.calculator:id/formula'
    RESULT = 'com.google.android.calculator:id/result_preview'
    FINAL_RESULT = 'com.google.android.calculator:id/result_final'
    SYMBOLIC = 'com.google.android.calculator:id/symbolic'
    SQUARE_ROOT = 'com.google.android.calculator:id/op_sqrt'

    def __init__(self, driver):
         self.driver = driver
         # all elements from the Page
         self.button_0 = driver.find_element(By.ID, self.DIGIT_0)
         self.button_1 = driver.find_element(By.ID, self.DIGIT_1)
         self.button_2 = driver.find_element(By.ID, self.DIGIT_2)
         self.button_3 = driver.find_element(By.ID, self.DIGIT_3)
         self.button_4 = driver.find_element(By.ID, self.DIGIT_4)
         self.button_5 = driver.find_element(By.ID, self.DIGIT_5)
         self.button_6 = driver.find_element(By.ID, self.DIGIT_6)
         self.button_7 = driver.find_element(By.ID, self.DIGIT_7)
         self.button_8 = driver.find_element(By.ID, self.DIGIT_8)
         self.button_9 = driver.find_element(By.ID, self.DIGIT_9)
         self.button_decimal_point = driver.find_element(By.ID, self.DECIMAL_POINT)
         self.button_plus = driver.find_element(By.ID, self.OPERATION_PLUS)
         self.button_minus = driver.find_element(By.ID, self.OPERATION_MINUS)
         self.button_divide = driver.find_element(By.ID, self.OPERATION_DIVIDE)
         self.button_multiply = driver.find_element(By.ID, self.OPERATION_MULTIPLY)
         self.button_del = driver.find_element(By.ID, self.OPERATION_DEL)
         self.button_equal = driver.find_element(By.ID, self.OPERATION_EQUAL)
         self.button_arrow = driver.find_element(By.ID, self.ARROW)
         self.area_formula = driver.find_element(By.ID, self.FORMULA)
         self.area_result = driver.find_element(By.ID, self.RESULT)


    def enter_number(self, number):
        # Verify if a number is valid
        num_format = re.compile(r'^\-?[1-9][0-9]*\.?[0-9]*')
        assert re.match(num_format,number), "Please provide a valid number to enter"

        numbers = [self.button_0, self.button_1, self.button_2, self.button_3, self.button_4,  
                   self.button_5, self.button_6, self.button_7, self.button_8, self.button_9]
        for i in range(len(number)):
            if number[i].isdigit():
                numbers[int(number[i])].click()
            elif number[i] == '-':
                self.button_minus.click()
            else:    
                self.button_decimal_point.click() 
                     
    
    def enter_plus(self):
        self.button_plus.click()

    def enter_minus(self):
            self.button_minus.click()
    
    def enter_divide(self):
            self.button_divide.click()
    
    def enter_multiply(self):
            self.button_multiply.click()
 
    def enter_equal(self):
        self.button_equal.click()
 
    def enter_square_root(self):   
        self.open_advanced_operations_window() 
        SQUARE_ROOT = self.driver.find_element(By.ID, self.SQUARE_ROOT)
        SQUARE_ROOT.click()
        self.close_advanced_operations_window()
        
    def open_advanced_operations_window(self):
        self.button_arrow.click()

    def close_advanced_operations_window(self):
        self.button_arrow.click()

    def get_result(self):
        return self.area_result.text
    
    def get_formula(self):
        return self.area_formula.text

    def get_final_result(self):
        return self.driver.find_element(By.ID, self.FINAL_RESULT).text

    def get_result_symbolic(self):
        return self.driver.find_element(By.ID, self.SYMBOLIC).text
