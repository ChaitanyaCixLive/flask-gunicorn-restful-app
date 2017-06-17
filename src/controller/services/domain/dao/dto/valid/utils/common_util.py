#! -*- coding=utf-8 -*-

"""
    Author:zhouze03@baidu.com
    Date:2017-06-17
    Desc: 通用的工具模块
"""




def dict_filter_none(dict):
    """
    desc: 过滤掉None语义的iterm
    :param dict:
    :return: 过滤后的dict
    """
    result_dict = {}
    for (k,v) in dict.items():
        if v != None and v != "":
            if isinstance(v, str):
                if v.strip() != "":
                    result_dict[k] = v
            else:
                result_dict[k] = v

    return result_dict



def dict_change_none(dict, sinbol):
    """
    desc: 将dict中选项值为None, " ", "" 统一转换为sinbol
          这方便对上述三种值统一处理
    :param dict:
    :return: 转换后的dict
    """
    for (k,v) in dict.items():
        if v == None or v == "" or (isinstance(v, str) and v.strip() == ""):
            dict[k]=sinbol
    return dict





if __name__ == '__main__':
    request_dict = {'username': 'zhouze03',
                    'agile_module_name': 'baidu/kg-lx/stone-restful-app',
                    'version': '0a5bd23e12d33c39a4770e0ba3cf7f56f310997a',
                    'stone_app_dir': ' ',
                    'stone_app_name': '',
                    'id':12345,
                    'None':None};
    print dict_filter_none(request_dict)
    print dict_change_none(request_dict, None)