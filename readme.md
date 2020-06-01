Tracer是一个基于Django的轻量级bug&任务追踪管理平台，目的是让bug追踪更简单、高效、便捷，提供安全、稳定的数据保障，将项目管理与团队协作完美地结合在一起。。。

**Overview**

Tracer使用了Django自带的数据库SQLite储存了用户过程中的产生的基本信息，诸如注册信息、项目信息等，文件上传利用了腾讯云的cos对象存储，对于某些必要的缓存，则利用redis进行缓存处理，如短信注册、session缓存。

安全方面：规避了XSS、CSRF、SQL注入等漏洞风险，及一些逻辑漏洞~


**Installation**

请先装好redis，Tracer使用pipenv管理虚拟环境，所以使用前请确保安装一个Python3.6环境（比如我这里环境路在/Users/0xff/anaconda3/envs/python36/bin/python3.6），然后安装好pipenv,redis装好后，进入项目目录，依照步骤执行：

```
# 下载代码

git clone https://github.com/oxff644/tracer
cd tracer
方案一：
pip install pipenv
# 请先提前创建好Python3.6环境
pipenv install --python /Users/0xff/anaconda3/envs/python36/bin/python3.6 --skip-lock
# 进入虚拟环境
pipenv shell
# 先配置好相关数据库配置
# 运行：
cd tracer
pipenv run python manage.py

方案二:
cd tracer
pip install -r requirements.txt
python manage.py makemigrations web
python manage.py migrate
python manage.py runserver 8080
```
**Featu****re****s**

* 注册
* 登录
  * 短信登录
  * 验证码登录
* 项目管理
  * 创建项目
  * 星标项目
  * 参与项目展示
* wiki
  * 添加/删除/修改wiki
  * Markdown文件预览
  * 文件上传/下载
* 问题
  * 更新问题
  * 评论与回复
  * 操作记录
  * 邀请链接
* 概览
  * 问题统计
  * 新增问题趋势
  * 人员任务配比
  * 项目参与者
  * 动态
* 日历
* 设置
  * 个人信息设置
  * 修改项目
  * 系统设置
* 统计
  * 人员工作统计
  * 优先级统计
* 支付
* 工作台

公众号：阿茯和面包，有兴趣的话可以关注下~

