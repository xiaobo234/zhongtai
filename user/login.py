import requests

class Login:
    def loginapi(self,req):
        re=requests.request(**req)
        return re #获取登录后返回数据中的token值
#         #print(re.json()['data'])