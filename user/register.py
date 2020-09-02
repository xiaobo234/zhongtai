import requests

class Register:
    def userregister(self,req):
        r = requests.request(**req)
        return r
# if __name__=='__main__':
#     req = {
#         "method": 'post',
#         "url": "https://liveapi.cn/yb-user/user/login",
#         "headers": {
#             "content-type": "application/json;charset=UTF-8",
#             "Remote-Host": "kk.100live.cn"
#         },
#         "json": {
#             "username": "15801409675",
#             "password": "e10adc3949ba59abbe56e057f20f883e"
#         }}
#
#     kk=Register()
#     kk.userregister(req)