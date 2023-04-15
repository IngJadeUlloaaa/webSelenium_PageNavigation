from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(executable_path=r'C:\DriverEdge\msedgedriver.exe')

    def test_OpenMore_Tab(self):
        driver = self.driver
        #Abrimos Ventanas
        driver.get('http://www.gmail.com/')
        time.sleep(3)
        #Abrimos Ventanas
        driver.get('https://www.google.com/')
        time.sleep(3)
        #Abrimos Ventanas
        driver.get('http://www.youtube.com/')
        time.sleep(3)
        #.Back() -> Sirve para Regresar a la Pagina Anterior
        driver.back()
        time.sleep(3)
        #.back() -> Sirve para Regresar a la Pagina Anterior
        driver.back()
        time.sleep(3)
        #.forward() -> Srive para ir a la pagina de adelante [0,1,2] = '1'
        driver.forward()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()