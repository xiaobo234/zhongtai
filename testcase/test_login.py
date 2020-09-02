import pytest
import requests
import yaml

from user.login import Login

class Testlogin:
    def setup(self):
        self.logintest=Login()#实例化注册

    @pytest.mark.parametrize('req,expect', yaml.safe_load(open('../user/login1.yaml')))
    def testlogin(self, req,expect):  # 正常注册测试用例
        assert self.logintest.loginapi(req).json()['code']== expect