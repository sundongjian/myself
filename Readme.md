TodoList：
优先级1
1 需要是用消息队列，来改动，让收益随着用户账户走动。(陈鼎)
2 回收站删除需要有回滚操作，如果连不上masterapi，需要能回滚，不然数据被删除，而服务器没有卸载。
3 需要监控中心，saltapi是否正常工作，爬虫获取消息是否成功。(sunjian)
4 编写远程维护数据库脚本。（陈鼎，完成）
5 数据库配置，热备份，故障自动切换，读写分离。（陈鼎）
6 回收站添加全部清空
7 添加错误捕获。
9 添加验证钱包，防止作弊。

8 clelry添加2个任务队列，一个响应即时任务，一个响应后台任务


优先级2
2 加密需要添加验证签名。
3 需要设置提现功能。
4 注册邮箱验证。（sunjian）
5 找回密码，重置密码。（sunjian）
6 解决ubuntu，发送邮件，无法读取import包的问题。
10 做用户中心，要求有修改密码，修改自己的图片，提现功能。（ ）


-------------安全性防护-------------
7 登陆界面，添加验证码。(sunjian)
8 登录界面设置登录保护，1天内只允许同一个账号5次密码输入错误。（防止暴力破解）
9 服务器需要记录ip在固定时间内访问次数，超出访问次数，则抛异常。
11 任何输入过程，需要做safe过滤，防止跨站脚本攻击。
12 重定向修复。（sunjian）


优先级3
1 修改挖矿种类，使用celery还是有问题，需要搞定。（这个使用频率不高，目前是秒切。所以，可以放到后面优化）
2 控制中心，在删除时，反应速度明显比添加慢，需要检查原因在哪里。

程序说明：
程序有2部分组成
a salt_api_flask 服务器 部署在salt——master同一台主机上
b web服务器 部署在web主机上

--------------------------------------------------------------------
a salt_master 所在服务器配置
1 建立一个新用户fp，创建文件夹/srv/salt/user_config，为fp用户分配user_config的读写权限。并且设置ssh只允许fp用户使用公钥登陆
2 进入到 saltapi_flask 目录 输入
    pip3 install -r requirements.txt
    等待环境配置完毕输入
    nohup python3 app.py &

--------------------------------------------------------------------
b web服务器配置说明：
1 进入config/settings.py
1.1 修改
    SALT_API = {
    "url": "http://192.168.0.41:5001",(修改 IP 为salt_master所在 IP 地址，端口不变)
    "auth_code":'yyUHHefsFHS@Khwewe&*$639!227&HJbe'
    }

1.2 修改 root@192.168.0.41 为刚在salt——master 所在主机创建的用户
    master_user = {
        'user':'root@192.168.0.41'
    }

2 终端输入
    ssh-copy-id root@192.168.0.41
    添加公钥到salt——master主机，建立信任关系。

3 配置数据库，详情见下方数据库配置

4 配置完数据库后启动数据库，
    输入pip3 install pymongo
    进入configs内执行setting_db.py,初始化数据库。

5 进入到 flask 目录 输入
    pip3 install -r requirements.txt
    等待环境配置完毕输入
    nohup sh run.sh &

6 初始化管理员配置 -》 部署配置。
    执行configs内的init_setup_deploy.py

启动celery
celery worker -A app.celery_gg --loglevel=info -B

apt-get install dos2unix
--------------------------------------------------------------------
c web服务器数据库配置
1 在／database 内找到 mongo_install，运行sh mongo_install.sh
2 终端1（如果报错，找不到文件夹，则去创建相关文件夹）
    mongod --port 27018 --dbpath /home/caturbhuja/mongodb/data/db
  终端2
  mongo --port 27018
    use admin
    db.createUser(
      {
        user: "myUserAdmin",
        pwd: "Hb123456",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
      }
    )
    exit

  终端1 结束之前任务，输入
    # 生产环境
    mongod --auth --port 27018 --bind_ip 0.0.0.0 --dbpath /home/caturbhuja/mongodb/data/db
    # 测试版本
    mongod --auth --port 27018 --bind_ip 127.0.0.1 --dbpath /home/caturbhuja/mongodb/data/db
    # mac
    mongod --auth --port 27018 --dbpath /Users/caturbhuja/mongodb/data/db



  终端2
  mongo --port 27018 -u "myUserAdmin" -p "Hb123456" --authenticationDatabase "admin"

    use OptimusPrime

    db.createUser(
      {
        user: "caturbhuja",
        pwd: "hb123456",
        roles: [ { role: "readWrite", db: "OptimusPrime" }]
      }
    )

    db.createUser(
      {
        user: "caturbhujadas",
        pwd: "hb123456",
        roles: [ { role: "dbAdmin", db: "OptimusPrime" }]
      }
    )

    exit

终端1 结束之前任务，输入
    nohup /usr/bin/mongod --auth --port 27018 --bind_ip 127.0.0.1,180.166.158.138 --dbpath /home/caturbhuja/mongodb/data/db >/opt/mongo.log 2>&1 &


--------------------------------------------------------------------
d redis配置
运行database内 redis_install.sh

--------------------------------------------------------------------
最后，使用pycharm

记得手动保存，记得手动保存，记得手动保存！不然会经常出现版本回退。


#############################################################################################
                                 salt-master 安装与配置

1．添加saltstack源
    #sudo wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | sudo apt-key add -
    新建saltstack master 源文件,并向其添加一下内容
    #sudo echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main" >/etc/apt/sources.list.d/saltstack.list
    #sudo apt-get update

2. 安装saltstack 包
    #sudo apt-get -y install salt-master salt-api

3.配置salt-api
    3.1安装pyOpenSSL
        pip install pyOpenSSL==18.0.0  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com --trusted-host pypi.douban.com
    3.2 添加salt-api 用户saltapi,为了安全，不允许login
        useradd –M –s /usr/sbin/nologin saltapi 并设置密码
    3.3 创建自签名证书
        salt-call --local tls.create_self_signed_cert
    3.4 安装cherrypy(修复TLS bug)
        pip install cherrypy==3.2.3

4．配置salt-master
    在/etc/salt/master 文件最后添加如下内容：（perl格式，注意缩进与空格，否则极容易出错）
interface: 0.0.0.0

external_auth:
  pam:
    saltapi:
      - .*
      - '@wheel'
      - '@runner'
      - '@jobs'

rest_cherrypy:
  port: 8000
  ssl_crt: /etc/pki/tls/certs/localhost.crt
  ssl_key: /etc/pki/tls/certs/localhost.key

file_recv: True
auto_accept: True

    重启服务
        service salt-master restart
        service salt-api restart
    测试Salt-API 工作是否正常
       curl -sSk https://localhost:8000/login -H 'Accept: application/x-yaml' -d username=saltapi -d password=salt2018 -d eauth=pam
 
       如下输出说明salt-api 配置正常，可以与salt-master通讯
       root@ubuntu:/home/ubuntu# curl -sSk https://localhost:8000/login -H 'Accept: application/x-yaml' -d username=saltapi -d password=salt2018 -d eauth=pam
       return:
       - eauth: pam
          expire: 1531580085.250718
       perms:
         - .*
         - '@wheel'
         - '@runner'
         - '@jobs'
      start: 1531536885.250717
      token: 42f23495b01c1d9e2b80154352a254e2bf0c338c
      user: saltapi

异常处理：
报错 PID check failed. RNG must be re-initialized after fork(). Hint: Try Random.atfork()
需要更改pycrypto,将这个判断注释掉。
"/usr/local/lib/python3.5/dist-packages/Crypto/Random/_UserFriendlyRNG.py", line 137, check_pid()

'''
