#encoding: utf-8  
  
import unittest
import myclass

class mytest(unittest.TestCase):  
    ##初始化工作  
    def setUp(self):  
        pass  
    #退出清理工作  
    def tearDown(self):  
        pass
    #具体的测试用例，一定要以test开头  
    def testsum(self):
        print(self)
        self.assertEqual(myclass.sum(1, 2), 2, 'test sum fail')  
    def testsub(self):
        print(self)
        self.assertEqual(myclass.sub(2, 1), 1, 'test sub fail')     
          
          
if __name__ =='__main__':  
    unittest.main()  
