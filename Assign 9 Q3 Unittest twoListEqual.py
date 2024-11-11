import unittest

def listEqualCheck(l1,l2):
        if l1==l2:
            return True
        else:
            return False

class listEqCheck(unittest.TestCase):

    def test_listEqCheck(self):
        self.assertTrue(listEqualCheck(["Yash","Sam"],["Yash","Sam"]))

if __name__ == "__main__":
    unittest.main()
