# <center> Django安装
# 1 install pip
  pip is already installed if you are using Python 2 >=2.7.9 or Python 3 >=3.4 downloaded from python.org or if you are working in a Virtual Environment created by virtualenv or pyvenv. Just make sure to upgrade pip.

  if not then we need install pip.

   可以参考 https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py
# 2 install Django
    enter the command pip install Django at the shell prompt.
    $ pip install Django
# 3 install virtualenv
## install
    To install golbally with Pip
    $ pip install virtualenv
## guide
    创建环境ENV,默认创建依赖系统的配置虚环境
    $ virtualenv ENV
    创建指定版本虚拟环境
    $ virtualenv -p /usr/local/bin/python3  ENV
    如果不想依赖,则可使用以下命令:
    $ virtualenv --no-site-packages ENV

    启动虚拟环境
    $  cd ENV
    $  source ./bin/activate
    此时,命令行会多一个EVN(虚拟环境n名称)

    退出虚拟环境
    deactivate
# 4 install virtualenvwrapper
## install and set
### 1)安装 virtualenvwrapper
    $ pip install virtualenvwrapper
### 2) 创建目录存放虚拟环境
    $ mkdir ~/.virtualenvs
### 3) 在.bashrc中末尾添加
    在之前,可以通过whereis virtualenvwrapper.sh查看安装路径.
    export WORKON_HOME=~/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
### 4) 执行生效
    source ~/.bashrc
## Command
    workon:列出虚拟环境列表
    lsvirtualenv:同上
    mkvirtualenv [envname]:新建虚拟环境
    workon [envname]:切换虚拟环境
    rmvirtualenv  [envname]:删除虚拟环境
    deactivate: 离开虚拟环境
    cpvirtualenv [sorce] [dest]　　#复制虚拟环境
    pip freeze > requirements.txt　　导出该环境下所有依赖到requirements.txt文件
