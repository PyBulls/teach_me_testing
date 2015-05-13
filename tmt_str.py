import unittest
from teach_me_doctests import to_upper

class TestX(unittest.TestCase):

    def test_to_upper(self):
        self.assertEqual(to_upper("foo"),"FOO")
        
    def test_to_upper_locals(self):
        expected = "FOO"
        actual = to_upper("foo")
        self.assertEqual(actual, expected)
        
        actual = to_upper("FOO")
        self.assertEqual(actual, expected)

        actual = to_upper("FoO")
        self.assertEqual(actual, expected)


    def test_almost_eq(self):
        self.assertAlmostEqual(2.0,1.9999999,5)

    def test_d_eq(self):
        a = {"key":"val"}
        b = a
        self.assertDictEqual(a,b)

    #def test_raise(self):
    #    a = 10/0
    #    self.assertRaises('ZeroDivisionError')
    
    def test_raise_in(self):
        # Less strict matching to facilitate custom err msg
        try:
            a = 10/0
        except Exception as e:    
            self.assertIn('ZeroDivision', str(type(e)))
    

    #def test_exception_is_raised(self):
    #    with self.assertRaises(ZeroDivisionError) as e:
    #    #    division_raises()
    #        a = 10/0
    #    self.assertEqual('Foo Exception occurred', e.exception.message)
    
    def test_d_eq(self):
        a = {"a":1,"b":2}
        b = {"a":1}
        self.assertDictContainsSubset(b,a)




class TestY(unittest.TestCase):

    def test_to_upper(self):
        self.assertEqual(to_upper("foo"),"FOO")


if __name__ == "__main__":
    unittest.main()
