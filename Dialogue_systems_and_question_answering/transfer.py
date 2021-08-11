
import time,hashlib,random,requests,json

def translate(q,lan_from,lan_to):
    '''
    Call Baidu Translation API
    '''
    appid = "20210315000728397"
    key = "boSy8iF_COO1rM8CrWql"
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    salt = random.randint(1, 65536)
    sign = hashlib.md5((str(appid)+str(q)+str(salt)+str(key)).encode('utf-8')).hexdigest()
    params = {
        'from' :lan_from,
        'to' :lan_to,
        'salt' : salt,
        'sign' : sign,
        'appid' : appid,
        'q': q
    }
    r = requests.get(url,params=params)
    txt = r.json()
    if txt.get('trans_result', -1) == -1:
        print('ERROR Code：{}'.format(txt))
        return q
    return txt['trans_result'][0]['dst']

def transfer(str):

    en = translate(str, 'zh', 'en')
    return en

if __name__ == '__main__':
    f = open('../data/tramData.json')
    t = f.read()
    res = json.loads(t)
    for i in res['content']:
        print(i['line_name'])
        en = translate(i['line_name'], 'zh', 'en')
        time.sleep(1)
        print(en)
        i['line_name'] = en

        for stop in i['stops']:
            print(stop['name'])
            stop['name'] = translate(stop['name'], 'zh', 'en')
            time.sleep(1)
            print(stop['name'])

    print(res)