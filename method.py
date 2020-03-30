from model import *
from datetime import *
from flask import json, request

# 自定义的一些方法
# 处理前端post过来的json
def get_data():
    data = json.loads(request.get_data(as_text=True))
    if not data:
        return 'empty request'
    return data


def get_grade_info(group):
    data_dict_list_dict = dict()
    us = User.query.filter_by(group=group).all()
    for u in us:
        gs = Grade.query.filter_by(openid=u.openid).all()
        if gs:
            data_list = []
            for i in gs:
                data_dict = dict()
                data_dict['name'] = i.name
                data_dict['grade'] = i.grade
                data_list.append(data_dict)
            data_dict_list_dict[u.name] = data_list
    return data_dict_list_dict


# 通过openid获取nickname
def get_nickname(openid):
    u = User.query.filter_by(openid=openid).first()
    if u:
        nick = u.name
    else:
        nick = "default"
    print("----")
    print(nick)
    return nick


# 通过openid获取group
def get_group_by_openid(openid):
    u = User.query.filter_by(openid=openid).first()
    group = u.group
    return group


# 把v提交到数据库
def submit(g):
    db.session.add(g)
    db.session.commit()


# 删除v
def delete(g):
    db.session.delete(g)
    db.session.commit()


# 判断是否管理
def is_admin(openid):
    g = Admin.query.filter_by(openid=openid)
    if g:
        return True
    else:
        return False


# 解析时间戳
def resolve_time(start, ks, data):
    c1 = time(8, 0, 0)
    c2 = time(9, 55, 0)
    c3 = time(13, 30, 0)
    c4 = time(15, 20, 0)
    c5 = time(17, 10, 0)
    c6 = time(19, 30, 0)
    c7 = time(21, 5, 0)
    for i in ks:
        index = int((i.time-start).days)
        local_time = time(i.time.hour, i.time.minute, i.time.second)
        print("-----inner")
        print(local_time)
        if c1 < local_time < c2:
            data[index][1] = data[index][1] + 1
        if c2 < local_time < c3:
            data[index][2] = data[index][2] + 1
        if c3 < local_time < c4:
            data[index][3] = data[index][3] + 1
        if c4 < local_time < c5:
            data[index][4] = data[index][4] + 1
        if c5 < local_time < c6:
            data[index][5] = data[index][5] + 1
        if c6 < local_time < c7:
            data[index][6] = data[index][6] + 1
        if c7 < local_time:
            data[index][7] = data[index][7] + 1


# 搜班级所有活动
def search_group_active(group, openid):
    data_list = []
    a = Active.query.filter_by(group=group).all()
    if a:
        for i in a:
            data_dict = dict()
            data_dict['type'] = "active"
            data_dict['title'] = i.title
            data_dict['text'] = i.text
            data_dict['time'] = i.time
            data_dict['id'] = 'class'
            print(i.time)
            data_list.append(data_dict)

    v = Vote.query.filter_by(group=group).all()
    if v:
        for i in v:
            data_dict = dict()
            text = i.text
            total = 0
            v = Vote.query.filter_by(text=text).first()

            data_detail = dict()
            if v:
                cs = Choice.query.filter_by(belong=text).all()
                for j in cs:
                    data_detail[j.text] = j.num
                    total += j.num
                data_detail["total"] = total
            data_dict['count'] = data_detail
            print("---------text")
            t = Index.query.filter_by(text=i.text, openid=openid).first()
            print("vote index")
            print(t)
            print("-----all index")
            ts = Index.query.filter_by(text=i.text).all()
            print(ts)
            if t:
                data_dict['join'] = "1"
            else:
                data_dict['join'] = "0"

            us = User.query.filter_by(group=group).all()
            t = int()
            for j in us:
                if j:
                    t = t + 1
            data_dict['class_member'] = t
            data_dict['type'] = "vote"
            data_dict['vote_type'] = i.type
            data_dict['title'] = i.text
            data_dict['time'] = i.time
            data_dict['id'] = 'class'
            cs = Choice.query.filter_by(belong=i.text).all()
            data_dict['choice'] = list()
            for j in cs:
                data_dict['choice'].append(j.text)
            print(i.time)
            data_list.append(data_dict)

    c = ClassSchedule.query.filter_by(group=group).all()
    if c:
        for i in c:
            data_dict = dict()
            data_dict['type'] = "class_schedule"
            data_dict['text'] = i.text
            data_dict['time'] = i.time
            data_dict['id'] = 'class'
            print(i.time)
            data_list.append(data_dict)

    return data_list
