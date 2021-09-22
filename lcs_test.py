import unittest
from lcs_dp_mine import lcs,print_lcs

class LcsTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(0,lcs("A","B"))        

    def test_1(self):
        self.assertEqual(1,lcs("A","A"))
    
    def test_2(self):
        self.assertEqual(2,lcs("AAF","BAA"))
    
    def test_3(self):
        self.assertEqual(3,lcs("AFAOREK","REKAF"))

    def test_6(self):
        self.assertEqual(6,lcs("AFAOREKA","LAFAREK"))
    
    def test_print_lcs_1(self):
        self.assertEqual("",print_lcs("A","B"))
        
    def test_print_lcs_2(self):
        self.assertEqual("A",print_lcs("AB","A"))
        
    def test_print_lcs(self):
        self.assertEqual("CTTA",print_lcs("AGCTTAGCTG","CTTA"))
        
    def test_print_lcs(self):
        self.assertTrue(print_lcs("AGCTTAGC","TCGGATG") == "TGG" or print_lcs("AGCTTAGC","TCGGATG") =="ATG")
        
if __name__ == "__main__":
    unittest.main()