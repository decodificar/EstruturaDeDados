
'''
defina uma funcao maximo2 que recebe dois numeros e retorna o maior deles
'''
def maximo2(a, b):
    if a > b:
        return a
    return b

'''
defina uma funcao maximo3 que recebe três numeros e retorna o maior deles
'''
def maximo3(a, b, c):
    m = maximo2(a, b)
    if m > c:
        return m
    return c

'''
defina uma funcao maximo4 que recebe quatro numeros e retorna o maior deles
'''
def maximo4(a, b, c, d):
    m4 = maximo3(a, b, c)
    if m4 > d:
        return m4
    return d

'''
defina uma funcao maximo5 que recebe cinco numeros e retorna o maior deles
'''
def maximo5(a, b, c, d, e):
    m5 = maximo4(a, b, c, d)
    if m5 > e: 
        return m5
    return e

import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_maximo2(self):
        self.assertEqual(maximo2(1,2),2)
        self.assertEqual(maximo2(3,2),3)
        self.assertEqual(maximo2(-1,-2),-1)
        self.assertEqual(maximo2(-1,2),2)
    
    def test_maximo3(self):
        self.assertEqual(maximo3(1,2,3),3)
        self.assertEqual(maximo3(10,2,3),10)
        self.assertEqual(maximo3(1,20,3),20)
    
    def test_maximo4(self):
        self.assertEqual(maximo4(1,2,3,4),4)
        self.assertEqual(maximo4(10,2,3,4),10)
        self.assertEqual(maximo4(1,20,3,4),20)
        self.assertEqual(maximo4(1,2,30,4),30)
    
    def test_maximo5(self):
        self.assertEqual(maximo5(10,2,3,4,5),10)
        self.assertEqual(maximo5(1,20,3,4,5),20)
        self.assertEqual(maximo5(1,2,30,4,5),30)
        self.assertEqual(maximo5(1,2,3,40,5),40)
        self.assertEqual(maximo5(1,2,3,4,50),50)

    

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()

