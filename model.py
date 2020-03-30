from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@127.0.0.1:3306/db_info'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
db.create_all()


# 实体
# 用户类
# name用户名 openid用户识别码 group用户组 name用户名 birthday生日
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    group = db.Column(db.Text)
    name = db.Column(db.Text)


# 用户信息类,用户拥有某一条信息
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    name = db.Column(db.Text)
    text = db.Column(db.Text)


# openid用户识别码 name课程名 grade成绩
class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    name = db.Column(db.Text)
    grade = db.Column(db.Integer)


# 班级类
# name班级名 creator创建者
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    creator = db.Column(db.Text)


# 日程类
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    time = db.Column(db.DateTime)
    text = db.Column(db.Text)
    group = db.Column(db.Text)


# 班级日程
class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    group = db.Column(db.Text)
    time = db.Column(db.DateTime)
    text = db.Column(db.Text)


# 投票类
# text问卷描述 time截止时间 group用户组 creator索引到创建者
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    time = db.Column(db.DateTime)
    group = db.Column(db.Text)
    creator = db.Column(db.Text)
    type = db.Column(db.Text)


# 问题结果类
# text内容描述 num表示选择的人数 belong索引到问卷
class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    num = db.Column(db.Integer, default=0)
    belong = db.Column(db.Text)


# 填表问卷描述类
# text内容描述 creator索引到用户 group用户组
class Blank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    creator = db.Column(db.Text)
    group = db.Column(db.Text)


# 填空问卷回答类
# text回答的内容 creator填这条的人 belong索引到填表描述
class BlankContext(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    belong = db.Column(db.Text)
    creator = db.Column(db.Text)


# 事件通知类
# text事件描述 time时间 group用户组 creator创建者
class Active(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    time = db.Column(db.DateTime)
    group = db.Column(db.Text)
    creator = db.Column(db.Text)


# 关系类
# 标志类,openid的用户参加了事件text type参与事件的类型 choose选择了什么
class Index(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    type = db.Column(db.Text)
    text = db.Column(db.Text)
    choose = db.Column(db.Text)
    time = db.Column(db.DateTime)


# 标志类,标志着创建者权限
class Creator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    name = db.Column(db.Text)
    text = db.Column(db.Text)
    type = db.Column(db.Text)
    time = db.Column(db.DateTime)


# 标志类,标志着管理员权限
# 用户openid是group的管理员
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    openid = db.Column(db.Text)
    group = db.Column(db.Text)
