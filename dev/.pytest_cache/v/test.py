import pytest
class Test_Dome:
    def test_01(self):
        assert 1==1
    def test_02(self):
        assert 1!=2
    @pytest.mark.parametrize("user,passwd",[['张三','222'],['李四','444']])
    def test_03(self,user,passwd):
        print(user,passwd)
if __name__ == '__main__':
    pytest.main(["-sv",'test.py'])