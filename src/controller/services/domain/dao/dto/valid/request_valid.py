#! -*- coding=utf-8 -*-


from utils.exception_util import CustomerException
from utils.common_util import *
import logging,sys



def valid_register_param(request_param):
    """
    desc: stone注册请求参数验证
    :param request_param:
    :return:
    """
    request_param = dict_filter_none(request_param)
    logging.info(request_param)
    if isinstance(request_param, dict)\
            and request_param.has_key('username') \
            and request_param['username'] != None \
            and request_param.has_key('agile_module_name') \
            and request_param['agile_module_name'] != None \
            and request_param.has_key('version') \
            and request_param['version'] != None \
            and request_param.has_key('stone_app_dir') \
            and request_param['stone_app_dir'] != None \
            and request_param.has_key('stone_app_name') \
            and request_param['stone_app_name'] != None:
        return True
    else:
        raise CustomerException('param is invalid! {username,'
                                'agile_module_name,version,stone_app_dirstone_app_name}'
                                ' is necessary! but ' + str(request_param))





if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', stream=sys.stderr)
    request_dict={'username':'zhouze03',
                  'agile_module_name':'baidu/kg-lx/stone-restful-app',
                  'version':'0a5bd23e12d33c39a4770e0ba3cf7f56f310997a',
                  'stone_app_dir':'/home/disk2/stone_users_application/stone-restful-app',
                  'stone_app_name':'stone-restful-app'};
    request_dict = {'username': 'zhouze03',
                    'agile_module_name': 'baidu/kg-lx/stone-restful-app',
                    'version': '0a5bd23e12d33c39a4770e0ba3cf7f56f310997a',
                    'stone_app_dir': ' ',
                    'stone_app_name': ''};
    request_dict = {
                    'agile_module_name': 'baidu/kg-lx/stone-restful-app',
                    'version': '0a5bd23e12d33c39a4770e0ba3cf7f56f310997a',
                    'stone_app_dir': ' ',
                    'stone_app_name': ''};
    # request_dict='a'

    try:
        print isinstance(request_dict, dict)
        print valid_register_param(request_dict)
    except CustomerException,e:
        print "".join(e)

