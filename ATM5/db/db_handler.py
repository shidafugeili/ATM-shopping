from conf import settings
import json
import os
db_path=settings.DB_PATH
# '%s/%s.json'%(db_path,name)
def select(name):
    if not os.path.exists('%s/%s.json'%(db_path,name)):
        return
    else:
        with open('%s/%s.json'%(db_path,name),'r',encoding='utf-8') as f:
            user_dic=json.load(f)
            return user_dic
def save(user_dic):
    with open('%s/%s.json'%(db_path,user_dic['name']),'w',encoding='utf-8') as w:
        res=json.dumps(user_dic)
        w.write(res)
        w.flush()

