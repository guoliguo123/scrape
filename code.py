import time
import random
import json
import requests
import multiprocessing
import urllib.request
import random

TOKEN = 'YOUR_TOKEN'
FROM = 0
TO = 10000

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
]

headers = {
    'Referer': 'https://github.com/rust-lang/team/graphs/contributors',
    'Cookie': '_octo=GH1.1.619591892.1603265695; _ga=GA1.2.93098847.1603265768; _device_id=ac78fa16de70480db92c69a1449d37c9; user_session=prM3MrKaRK-fret7VllqZpbeW50XLnBiEQkUQet9qWlXnrm_; __Host-user_session_same_site=prM3MrKaRK-fret7VllqZpbeW50XLnBiEQkUQet9qWlXnrm_; logged_in=yes; dotcom_user=chargerKong; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=wPV6%2F9v15dk0A1eqwScTET98zEZk6G%2BjLdlvf%2FuxiQjr6fSXAgYaVuFO0esNLwDEIV4BsdreniWNO6kJT%2BY%2BX9JYsIzYn%2BBzNKxysmG31HZSVE6RRk%2B4SxQ42mvK90m7bFWZaBek2dE%2BJEAHztSlmbsnCUd4%2B%2FceTDw5yRPUuscjlP%2F%2FOOrzd6t5k9Wkag5A--knXCKDcW5cabS%2F6m--D9GunWquaHRW%2Fc8Gyuawqg%3D%3D',
    'accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,eo;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'github.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'X-Requested-With': 'XMLHttpRequest',
    'Authorization': 'token ' + TOKEN
}

def multi_process_download(task, map_list, process_num):
    pool = multiprocessing.Pool(process_num)
    pool.map(task, map_list)
    pool.close()
    pool.join()

def download_commit_data(crate_name):
    print(f'Downloading the committers of {crate_name}')
    #######This is used for downloading error.#######
    with open('data/crate_label.txt') as f:
        data = [i.strip() for i in f.readlines()]
    if crate_name in data:
        print('The committer info of', crate_name, 'has been downloaded.')
        return
    #################################################
    if crate_name not in crate_dict or 'repository' not in crate_dict[crate_name]:
        raise Exception(f'There is no repository url for {crate_name}')

    repo_url = crate_dict[crate_name]['repository']
    headers['user-agent'] = random.choice(USER_AGENT_LIST)
    request_url = repo_url + '/graphs/contributors-data'
    response = requests.get(request_url, headers=headers)

    if response.status_code < 200 or response.status_code >= 300:
        raise Exception(f'Response error {response.status_code}')

    with open('data/crate/' + crate_name + '_commits.json', 'w') as f:
        json.dump(response.text, f)
    with open('data/crate_label.txt', 'a') as f:
        f.write(crate_name + '\n')
    ################################################# 

    time.sleep(random.randint(0, 9))

with open('data/crate/crate_dict.json') as f:
    crate_dict = json.loads(f.readline())

with open('data/only_crate.txt') as f:
    crate_list = [i.strip() for i in f.readlines()]

#multi_process_download(download_commit_data, crate_list[12000:14000], 4)
failed = []
for crate in crate_list[FROM:TO]:
    try:
        download_commit_data(crate)
    except Exception as e:
        print(f'failed to download {crate}, reason:{e}')
        failed.append(crate)

with open('./fails', 'w') as f:
    f.write('\n'.join(failed))
