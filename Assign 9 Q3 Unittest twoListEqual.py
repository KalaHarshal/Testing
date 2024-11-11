import unittest

    def listEqualCheck(l1,l2):
        if l1==l2:
            return True
        else:
            return False

    class listEqCheck(unittest.TestCase):

        def test_listEqCheck(self):
            self.assertTrue(listEqualCheck([&#39;Yash&#39;,&#39;Sam&#39;],[&#39;Yash&#39;,&#39;Sam&#39;]))

if __name__ == "__main__"
unittest.main()
