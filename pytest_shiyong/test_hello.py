import pytest


class Test_pytest_01():
    @pytest.mark.run(order=3)
    def test_add_1(self):
        print('这是01')
        assert 1 == 2

    @pytest.mark.run(order=1)
    def test_add_2(self):
        print('这是02')
        assert 2 == 2

    @pytest.mark.run(order=4)
    def test_add_3(self):
        print('这是03')
        assert 2 == 2

    @pytest.mark.run(order=2)
    @pytest.mark.add
    def test_add_4(self):
        print('这是04')
        assert 2 == 2
    def test_div_1(self):
        print('这是div1')
        assert 3 == 2
    def test_div_2(self):
        print('这是div1')
        assert 4 == 2
    def test_div_3(self):
        print('这是div1')
        assert 2 == 2

    @pytest.mark.div
    def test_div_4(self):
        print('这是4')
        assert 2 == 2


