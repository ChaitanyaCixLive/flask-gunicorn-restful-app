#! -*- coding=utf-8 -*-

from flask import jsonify

# define statu_dics here
R200_OK = {'code': 200, 'desc': 'OK all right.'}
R201_CREATED = {'code': 201, 'desc': 'All created.'}
R204_NOCONTENT = {'code': 204, 'desc': 'All deleted.'}
R400_BADREQUEST = {'code': 400, 'desc': 'Bad request.'}
R403_FORBIDDEN = {'code': 403, 'desc': 'You can not do this.'}
R404_NOTFOUND = {'code': 404, 'desc': 'No result matched.'}


def fullResponse(statu_dic, msg , data):
    statu_dic['msg'] = msg
    statu_dic['data'] = data
    return jsonify(statu_dic)


def statusResponse(statu_dic):
    return jsonify({'status': statu_dic})




