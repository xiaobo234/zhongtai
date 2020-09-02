import yaml

def testyamldata():
    #要转换的数据
    req = {
        "method": "post",
        "url": "https://liveapi.cn/yb-user/user/login",
        "headers": {
            "content-type": "application/json;charset=UTF-8",
            "Remote-Host": "kk.100live.cn"
        },
        "json": {
            "username": "15801409675",
            "password": "e10adc3949ba59abbe56e057f20f883e"
        }
    }
    kk=[[req,200],[req,201]]
    print(yaml.dump(kk))
    #打开一个yaml文件，名字为gettoken.yaml，并且将转换的数据保存到此yaml文件中
    with open("login1.yaml","w") as f:
        yaml.safe_dump(data=kk,stream=f) #将python字典转换成yaml文件的方法