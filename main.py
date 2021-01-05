from tools import *
import json

if __name__ == '__main__':
    # crate info dict
    #crate_dict = {}

    # author info dict
    #author_dict = {}

    # download the crate names and some basic info
    #multi_process_download(download_crate_names, [i for i in range(1, 982)], 32)

    # extract the crate names and basic info
    #crate_dict = extract_crate_basic_info(crate_dict)
    #crate_id_list = crate_dict.keys()
    #crate_id_version_list = [[i, crate_dict[i]['newest_version']] for i in crate_dict.keys()]
    

    # download other info of crates from api
    #multi_process_download(download_crate_info, crate_id_list, 128)
    #multi_process_download(download_crate_other_info, crate_id_version_list, 128)

    # extract the specifically info of crates (dependencies and author)
    #crate_dict = extract_crate_spec_info(crate_dict)

    # analysis the crates
    #crate_dict = crate_dict_analysis(crate_dict)

    # save the crate_dict as a json file
    #with open('data/crate/crate_dict.json', 'w') as f:
    #    json.dump(crate_dict, f)

    # load the crate_dict from a json file
    with open('data/crate/crate_dict.json') as f:
        crate_dict = json.loads(f.readline())
    
    #author_list = []
    #for k,v in crate_dict.items():
    # save the crate info into csv file
    #    print(k, '*', v['created_at'], '*', v['updated_at'], '*', str(v['downloads']), '*', str(v['recent_downloads']), '*', str(v['direct_dep_num']), '*', str(v['indirect_dep_num']), '*', ','.join(v['keywords']), '*', ','.join(v['categories']), '*', v['homepage'], '*', v['documentation'], '*', v['repository'], '*', ','.join([i['crate_id'] for i in v['dependencies']]), '*', ','.join([i['login'] for i in v['owners']]), '*', str(v['authors']))
    # save the author info into csv file
    #    for i in v['owners']:
    #        if [i['login'], i['name'], i['url']] not in author_list:
    #            author_list.append([i['login'], i['name'], i['url']])
    #        else:
    #            continue
    #for i in author_list:
    #    print(i[0], ',', i[1], ',', i[2])i

    with open('data/other/contributors.txt') as f:
        author_login_list = [i.strip().split(',')[0].strip() for i in f.readlines()]

    for i in author_login_list:
    #    download_author_api(i)
        download_orgnization_api(i)

    #author_info = extract_author_csv(author_login_list)

    #with open('data/author/author_dict.json', 'w') as f:
    #    json.dump(author_info, f)
