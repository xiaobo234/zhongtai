import pytest
import requests
import yaml
from user.register import Register
class Testregister:
    def setup(self):
        self.register=Register()#实例化注册

    # #读取yaml文件
    # def yaml_data(self):
    #     with open('../user/regidter.yaml',encoding='utf-8') as f:
    #         return yaml.safe_load(f)

    @pytest.mark.parametrize('req',yaml.safe_load(open('../user/regidter.yaml')))
    def testregister(self,req):#正常注册测试用例
        # req = {
        #     "method": "post",
        #     "url": "https://liveapi.cn/yb-user/user/login",
        #     "headers": {
        #         "content-type": "application/json;charset=UTF-8",
        #         "Remote-Host": "kk.100live.cn"
        #     },
        #     "json": {
        #         "username": "15801409675",
        #         "password": "e10adc3949ba59abbe56e057f20f883e"
        #     }
        # }
        assert self.register.userregister(req).status_code==200

