import os
import toml
import xlwt
import time
import random
import fcntl
import json
import requests
import multiprocessing
import urllib.request
from bs4 import BeautifulSoup
import networkx as nx

def rand_select_user_agent():
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
    USER_AGENT = random.choice(USER_AGENT_LIST)
    return USER_AGENT


def request_data_from_url(referer_url, request_url):
    print('Downloading', request_url , '...')
    if referer_url != '':
        headers = {
            ':authority': 'crates.io',
            ':method': 'GET',
            ':path': '/api/v1/crates?page=1&per_page=50&sort=downloads',
            ':scheme': 'https',
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'cookie': 'cargo_session=sJIiNcfM9yvCHoGNENQaO8JrPoTF1c7xuZ6xe/LTieY=',
            'referer': referer_url,
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': rand_select_user_agent()
        }
    else:
        headers = {
            'user-agent': rand_select_user_agent()
        }
    response = requests.get(request_url, headers).text
    return response


def multi_process_download(task, map_list, process_num):
    pool = multiprocessing.Pool(process_num)
    pool.map(task, map_list)
    pool.close()
    pool.join()


def download_crate_names(page_num):
    print(page_num)
    #######This is used for downloading error.#######
    f = open('data/page_label.txt')
    data = [i.strip() for i in f.readlines()]
    if str(page_num) in data:
        return
    f.close()
    #################################################

    # download the crate list using api
    crate_name_url = 'https://crates.io/api/v1/crates?page=' + str(page_num) + '&per_page=50&sort=downloads'
 
    # using requests
    pass
    # using urlopen
    response = json.loads(urllib.request.urlopen(crate_name_url).readline())
    
    # saving the crate lists as json files
    save_path = 'data/crate/page_' + str(page_num) + '_crate_name.json'
    with open(save_path, 'w') as f:
        json.dump(response, f)

    #######This is used for downloading error.#######
    f = open('data/page_label.txt', 'a')
    f.write(str(page_num)+'\n')
    f.close()
    #################################################


def extract_crate_basic_info(crate_dict):
    for i in range(1, 982):
        # print(i) # the page num
        with open('data/crate/page_' + str(i) + '_crate_name.json') as f:
            dict_1 = json.loads(f.readline())
            for j in dict_1['crates']:
                if j['id'] not in crate_dict.keys():
                    crate_dict[j['id']] = j
    return crate_dict


def download_crate_info(crate_id):
    print(crate_id)
    #######This is used for downloading error.#######
    f = open('data/crate_label.txt')
    data = [i.strip() for i in f.readlines()]
    if crate_id in data:
        return
    f.close()
    #################################################

    # There are some apis for each crate.
    crate_url = 'https://crates.io/api/v1/crates/' + crate_id
    #version_download_url = 'https://crates.io/api/v1/crates/' + crate_name + '/downloads'
    #version_url = 'https://crates.io/api/v1/crates/' + crate_name + '/versions'
    owners_url = 'https://crates.io/api/v1/crates/' + crate_id + '/owners'
    #owner_team = 'https://crates.io/api/v1/crates/' + crate_name + '/owner_team'
    #owner_user_url = 'https://crates.io/api/v1/crates/' + crate_name + '/owner_user'
    #reverse_dependencies_url = 'https://crates.io/api/v1/crates/' + crate_name + '/reverse_dependencies'

    # using requests
    pass
    # using urlopen
    response = json.loads(urllib.request.urlopen(crate_url).readline())

    # saving the crate lists as json files
    save_path = 'data/crate/' + crate_id + '_self.json'
    with open(save_path, 'w') as f:
        json.dump(response, f)

    # using urlopen
    response = json.loads(urllib.request.urlopen(owners_url).readline())

    # saving the crate lists as json files
    save_path = 'data/crate/' + crate_id + '_owners.json'
    with open(save_path, 'w') as f:
        json.dump(response, f)

    #######This is used for downloading error.#######
    f = open('data/crate_label.txt', 'a')
    f.write(crate_id +'\n')
    f.close()
    #################################################


def download_crate_other_info(crate_id_version_list):
    [crate_id, crate_version] = [crate_id_version_list[0], crate_id_version_list[1]]
    print(crate_id, crate_version)
    #######This is used for downloading error.#######
    f = open('data/crate_label.txt')
    data = [i.strip() for i in f.readlines()]
    if crate_id in data:
        return
    f.close()
    #################################################

    # There are some apis for each crate.
    #version_download_url = 'https://crates.io/api/v1/crates/' + crate_name + '/' + 'crate_version' + '/downloads'
    author_url = 'https://crates.io/api/v1/crates/' + crate_id + '/' + crate_version + '/authors'
    dependencies_url = 'https://crates.io/api/v1/crates/' + crate_id + '/' + crate_version + '/dependencies'

    # using requests
    pass
    # using urlopen
    response = json.loads(urllib.request.urlopen(author_url).readline())

    # saving the crate lists as json files
    save_path = 'data/crate/' + crate_id + '_authors.json'
    with open(save_path, 'w') as f:
        json.dump(response, f)

    # using urlopen
    response = json.loads(urllib.request.urlopen(dependencies_url).readline())

    # saving the crate lists as json files
    save_path = 'data/crate/' + crate_id + '_dependencies.json'
    with open(save_path, 'w') as f:
        json.dump(response, f)

    #######This is used for downloading error.#######
    f = open('data/crate_label.txt', 'a')
    f.write(crate_id +'\n')
    f.close()
    #################################################


def extract_crate_spec_info(crate_dict):
    for i in crate_dict.keys():
        # print(i)
        # dependencies
        f = open('data/crate/' + i + '_dependencies.json')
        data = f.readline()
        f.close()
        try:
            json_data = json.loads(data)['dependencies']
        except:
            json_data = []
        if 'dependencies' not in crate_dict[i].keys():
            crate_dict[i]['dependencies'] = json_data
        
        # owners
        f = open('data/crate/' + i + '_owners.json')
        data = f.readline()
        f.close()
        try:
            json_data = json.loads(data)['users']
        except:
            json_data = ['None']
        if 'owners' not in crate_dict[i].keys():
            crate_dict[i]['owners'] = json_data

        # authors
        f = open('data/crate/' + i + '_authors.json')
        data = f.readline()
        f.close()
        try:
            json_data = json.loads(data)['meta']
        except:
            json_data = {}
        if 'authors' not in crate_dict[i].keys():
            crate_dict[i]['authors'] = json_data

    return crate_dict


def crate_dict_analysis(crate_dict):
    # using networkx
    dep_graph = nx.DiGraph()
    for i in crate_dict.keys():
        dep_graph.add_node(i)
        dependencies_list = crate_dict[i]['dependencies']
        if len(dependencies_list) != 0:
            for j in dependencies_list:
                if j['kind'] == 'normal' and j['optional'] == False:
                    dep_graph.add_edge(i, j['crate_id'])
    
    for i in crate_dict.keys():
        # directly depend
        direct_dep_num = len(crate_dict[i]['dependencies'])
        # indirectly depend
        indirect_dep_num = len(nx.ancestors(dep_graph, i)) 
        if 'direct_dep_num' not in crate_dict[i].keys():
            crate_dict[i]['direct_dep_num'] = direct_dep_num
        if 'indirect_dep_num' not in crate_dict[i].keys():
            crate_dict[i]['indirect_dep_num'] = indirect_dep_num
    return crate_dict


def extract_author_basic_info(crate_id_list, author_dict):
    # contribution
    for i in crate_id_list:
        #print(i)
        temp_dict = {}
        file_path = 'data/crate/' + i + '_authors.json'
        with open(file_path) as f:
            temp_dict = json.loads(f.readline())
        if 'meta' not in temp_dict.keys():
            continue
        else:
            for j in temp_dict['meta']['names']:
                if j not in author_dict.keys():
                    author_dict[j] = {}
                if 'contributions' not in author_dict[j].keys():
                    author_dict[j]['contributions'] = []
                author_dict[j]['contributions'].append(i)

    # contribution number
    for i in author_dict.keys():
        if 'contribution_num' not in author_dict[i].keys():
            author_dict[i]['contribution_num'] = len(author_dict[i]['contributions'])

    # contribution dependencies&downloads

    return author_dict
        

def extract_author_name():
    dir_path = './team/people'
    a_1 = os.listdir(dir_path)
    wb = xlwt.Workbook()
    ws = wb.add_sheet("myms")
    
    j = 0
    #for i in range(0, 255):
    for i in range(255, len(a_1)):
        print(a_1[i])
        path = os.path.join(dir_path, a_1[i])
        tmp = toml.load(path)
        j += 1
        k = 0
        for key,value in tmp.items():
            k += 1
            print(j, k,value)
            ws.write(k, j, label = key)
            k += 1
            ws.write(k, j, label = str(value))
    wb.save('excel_test2.xls')


def extract_team_name():
    print('#########################')
    dir_path = "./team/teams"
    a = os.listdir(dir_path)
    wb = xlwt.Workbook()
    #ws = wb.add_sheet("myms")
    j = 0
    print(len(a))
    for i in range(0, len(a)):
        if a[i] == 'archive':
            continue
        path = os.path.join(dir_path, a[i])
        ws = wb.add_sheet(a[i])
        tmp = toml.load(path)
        tmps = toml.dumps(tmp)
        t = tmps.split("\n")
        print(t)
        for k in range(len(t)):
            print(t[k])
            ws.write(k,j,label=t[k])

    wb.save('excel_test3.xls')
    print("over")


def download_author_api(author_login):
    print(author_login)
    #######This is used for downloading error.#######
    f = open('data/author/author_label.txt')
    data = [i.strip() for i in f.readlines()]
    f.close()
    if author_login in data:
        return
    #################################################
    
    author_url = 'https://api.github.com/users/' + author_login
    headers = {
        'user-agent': rand_select_user_agent(),
        "Authorization": "token 1777eae85a3b77e29c5854af7d2b40538b88d638"
    }
    ip_list = ['223.215.97.198:54223',
               '60.166.163.243:54286',
               '110.187.21.255:54245']
    proxies = {'http': random.choice(ip_list)}
    response = requests.get(author_url, headers=headers, proxies=proxies)
    
    # judge that if the response is valid
    if response.status_code != 200:
        return

    response_dict = json.loads(response.text)

    save_path = 'data/author/' + author_login + '_api.json'
    with open(save_path, 'w') as f:
        json.dump(response_dict, f)
    
    #######This is used for downloading error.#######
    f = open('data/author/author_label.txt', 'a')
    f.write(author_login + '\n')
    f.close()
    #################################################    

    time.sleep(random.randint(0, 5))
    

def extract_author_info_from_github(author_login, begin_year, end_year, author_dict):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    if 'contributions' not in author_dict.keys():
        author_dict['contributions'] = {}
    for i in range(begin_year, end_year+1):
        for j in range(1, 13):
            if j < 10:
                contribution_url = 'https://github.com/' + author_login + '?tab=overview&from=' + str(i) + '-0' + str(j) + '-01&to=' + str(i) + '-0' + str(j) + '-31'
            else:
                contribution_url = 'https://github.com/' + author_login + '?tab=overview&from=' + str(i) + '-' + str(j) + '-01&to=' + str(i) + '-' + str(j) + '-31'
            res = requests.get(contribution_url, headers)
            soup = BeautifulSoup(res.text, 'html.parser')
    
            # contributions
            contributions = soup.find_all('div', 'col-8 css-truncate css-truncate-target lh-condensed width-fit flex-auto min-width-0')
            result = ''
            for k in contributions:
                for l in k.children:
                    try:
                        result += l.text.strip()
                        result += ' '
                    except:
                        pass
                result += ';'
            times = str(i) + '-' + str(j)
            
            if times not in author_dict['contributions'].keys():
                author_dict['contributions'][times] = result.strip()

            print(times)
            print(result)


def extract_author_from_json(author_list):
    for i in author_list:
        with open('data/author/' + i + '_api.json') as f:
            json_data = json.loads(f.readline())
            values = [str(i) for i in list(json_data.values())]
            for j in values:
                if j == '':
                    j = 'None'
            temp = '*'.join([values[0], values[1], values[3], values[6], values[18], values[19], values[20], values[21], values[22], values[25], values[28], values[29]]) + '\n'
        with open('data/contributors_infor.txt', 'a') as f1:
            f1.write(temp)


def download_crate_commit(crate_name, crate_dict):
    crate_url = crate_dict[crate_name]['repository']
    # way 1: directly scrape the original website

    # way 2: using the github api
    url = crate_url.split('/')
    for i in range(2020, 2021):
        for j in range(1, 13):
            print(i, j)
            if i < 10:
                request_url = url[0] + '//' + 'api.' + url[2] + '/repos/' + url[3] + '/' + url[4] + '/commits?since=' + str(i) + '-0' + str(j) + '-01&until=' + str(i) + '-0' + str(j) + '-31'
            else:
                request_url = url[0] + '//' + 'api.' + url[2] + '/repos/' + url[3] + '/' + url[4] + '/commits?since=' + str(i) + '-' + str(j) + '-01&until=' + str(i) + '-' + str(j) + '-31'
            headers = {"Authorization": "token 8f6634296b6d4a1e792b25f26fd07e27a9e44b15"}
            response = json.loads(requests.get(request_url, headers=headers).text)
        
            #save_path = 'data/crate/' + crate_name + '_' + str(i) + '_' + str(j) + '_commits.json'
            #with open(save_path, 'w') as f:
            #    json.dump(response, f)
            for k in response:
                committer = i['commit']['committer']
                commit_url = i['url']
                commit_response = json.loads(requests.get(commit_url, headers=headers).text)
                commit_add_num = commit_response['stats']['additions']


def download_commit_data(crate_name):
    print(crate_name)
    #######This is used for downloading error.#######
    f = open('data/crate_label.txt')
    data = [i.strip() for i in f.readlines()]
    f.close()
    if crate_name in data:
        return
    #################################################
    try:
        request_url = crate_dict[crate_name]['repository'] + '/graphs/contributors-data'
    except:
        print('no repo url')
        return
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
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
        'Authorization': 'token 8f6634296b6d4a1e792b25f26fd07e27a9e44b15'
    }
    response = requests.get(request_url, headers=headers)
    if response.status_code != 200:
        return
    #print(response.text)
    with open('data/crate/' + crate_name + '_commits.json', 'w') as f:
        json.dump(response.text, f)
    #######This is used for downloading error.#######
    f = open('data/crate_label.txt', 'a')
    f.write(crate_name + '\n')
    f.close()
    ################################################# 

    time.sleep(1)


def extract_commit_data(crate_importance_list, time): # 2015-01-01 00:00:00 1420041600
    temp_dict = {}
    for i in crate_importance_list:
        print(i)
        crate_name = i[0]
        crate_importance = i[1]
        try:
            with open('data/crate/' + crate_name + '_commits.json') as f:
                data = f.readline()
        except:
            print('We could not find the commit file of', crate_name)
            continue

        try:
            json_data = json.loads(json.loads(data))
        except:
            print(f'the repo of {crate_name} is not a github address.')
            continue

        crate_contribution_num = 0
        for j in json_data:
            author_name = j['author']['login']
            author_contribution_num = 0
            for k in j['weeks']:
                author_add_date = k['w']
                author_contribution_add_num = k['a']
                if author_add_date < time:
                    continue
                else:
                    author_contribution_num += author_contribution_add_num
                    crate_contribution_num += author_contribution_add_num
            if author_contribution_num == 0:
                continue
            if author_name not in temp_dict.keys():
                temp_dict[author_name] = 0
            temp_dict[author_name] += author_contribution_num / crate_contribution_num * crate_importance / 4.785957350677055
        print('The commit file of', crate_name, 'processed done.')
    return temp_dict


def extract_commit_data_half_life(crate_importance_list, begin_timestamp, end_timestamp, half_life_stamp):
    temp_dict = {}
    for i in crate_importance_list: 
        crate_name = i[0]
        crate_importance = i[1]
        print(f'Looking for the committer info for crate {crate_name}.')

        try:
            with open('data/crate/' + crate_name + '_commits.json') as f:
                data = f.readline()
        except:
            print(f'We could not find the commit file of {crate_name}.')
            continue

        try:
            json_data = json.loads(json.loads(data))
        except:
            print(f'the repo of {crate_name} is not a github address.')
            continue

        crate_contribution_num = 0
        for j in json_data:
            author_name = j['author']['login']
            author_contribution_num = 0
            for k in j['weeks']:
                author_add_date = k['w']
                author_contribution_add_num = k['a']

                if author_add_date < begin_timestamp or author_add_date > end_timestamp:
                    continue
                else:
                    author_contribution_add_num_half_life = (1/2) ** ((end_timestamp - author_add_date) / half_life_stamp) * author_contribution_add_num
                    author_contribution_num += author_contribution_add_num_half_life
                    crate_contribution_num += author_contribution_add_num_half_life

            if crate_contribution_num == 0:
                continue
            if author_name not in temp_dict.keys():
                temp_dict[author_name] = 0
            temp_dict[author_name] += author_contribution_num / crate_contribution_num * crate_importance
        print('The commit file of', crate_name, 'processed done.')
    max_value = max(temp_dict.values())
    for i in temp_dict.keys():
        temp_dict[i] /= max_value
    return temp_dict

def extract_crate_categories_keywords(crate_dict):
    for i in crate_dict.keys():
        with open('data/crate/' + i + '_self.json') as f:
            data = f.readline()
        try:
            categories_data = json.loads(data)['crate']['categories']
        except:
            categories_data = []
        if 'categories' not in crate_dict[i].keys():
            crate_dict[i]['categories'] = categories_data
        crate_dict[i]['categories'] = categories_data

        try:
            keywords_data = json.loads(data)['crate']['keywords']
        except:
            keywords_data = []
        if 'keywords' not in crate_dict[i].keys():
            crate_dict[i]['categories'] = keywords_data
        crate_dict[i]['keywords'] = keywords_data
    return crate_dict


def extract_author_csv(author_login_list):
    #print('login*name*compony*blog*location*email*hireable*bio*twitter_username*public_repos*public_gists*follower*following*created_at*updated_at*id*name_id*avatar_url*url*html_url*followers_url*following_url*gists_url*starred_url*subscriptions_url*organizations_url*repos_url*events_url*received_events_url')
    temp = []
    for i in author_login_list:
        try:
            with open('data/author/' + i + '_api.json') as f:
                data = f.readline()
            author_dict = json.loads(data)
            temp.append(author_dict)
            
            #result = []
            #for k,v in author_dict.items():
            #    result.append(v)
            #    result.append('*')
            #print(result)
        except:
            pass
            #print('there is no that person')
        '''
            print(v['login'], '*',
                  v['name'], '*',
                  v['compony'], '*',
                  v['blog'], '*',
                  v['location'], '*',
                  v['email'], '*',
                  str(v['hireable']), '*',
                  v['bio'], '*',
                  str(v['twitter_username']), '*',
                  str(v['public_repos']), '*',
                  str(v['public_gists']), '*',
                  str(v['followers']), '*',
                  str(v['following']), '*',
                  v['created_at'], '*',
                  v['updated_at'], '*',
                  str(v['id']), '*',
                  v['node_id'], '*',
                  v['avatar_url'], '*',
                  v['url'], '*',
                  v['html_url'], '*',
                  v['followers_url'], '*',
                  v['following_url'], '*',
                  v['gists_url'], '*',
                  v['starred_url'], '*',
                  v['subscriptions_url'], '*',
                  v['organizations_url'], '*',
                  v['repos_url'], '*',
                  v['events_url'], '*',
                  v['received_events_url'], '*',

                 )
        '''

    return temp


def download_orgnization_api(author_login):
    print(author_login)
    #######This is used for downloading error.#######
    f = open('data/author/author_label.txt')
    data = [i.strip() for i in f.readlines()]
    f.close()
    if author_login in data:
        return
    #################################################
    
    author_url = 'https://api.github.com/users/' + author_login + '/orgs'
    headers = {
        'user-agent': rand_select_user_agent(),
        "Authorization": "token 1777eae85a3b77e29c5854af7d2b40538b88d638"
    }
    ip_list = ['180.116.168.30:4276',
               '27.157.131.102:4245',
               '61.187.243.145:4235']
    proxies = {'http': random.choice(ip_list)}
    response = requests.get(author_url, headers=headers, proxies=proxies)
    
    # judge that if the response is valid
    if response.status_code != 200:
        return

    response_dict = json.loads(response.text)

    save_path = 'data/author/' + author_login + '_orgnization_api.json'
    with open(save_path, 'w') as f:
        json.dump(response_dict, f)
    
    #######This is used for downloading error.#######
    f = open('data/author/author_label.txt', 'a')
    f.write(author_login + '\n')
    f.close()
    #################################################    

    time.sleep(random.randint(0, 5))
