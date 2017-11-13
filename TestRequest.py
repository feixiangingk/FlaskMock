#-*-coding=utf-8-*-
# project:     workspace
# createtime:  2017/11/13  11:17
# IDE:         PyCharm
# anthor:      ZT@gufan
import requests
class TestRequest():

    def __init__(self):
        self.s=requests.session()

    def test_HF1010(self):
        URL='http://127.0.0.1:5000/HF1010.do'
        data={"format":"XML","channel":"WAP","certType":"A","certNo":"123456789123456789","bank":"shanghaiyinhang"}
        # data1={"format":"XML","channel":"WAP","certType":"A","certNo":"123456789123456789"}
        self.s.post(URL,params=data)
        self.s.close()

if __name__=="__main__":
    test=TestRequest()
    test.test_HF1010()