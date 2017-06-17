#! -*- coding=utf-8 -*--

"""
    @author: zhouze03@baidu.com
    @date: 2017-06-16
    @desc: Flask Controller
"""

from flask import Flask, request
from services.domain.dao.dto.valid.utils.restful_util import *
from services.domain.dao.dto.valid.request_valid import *
from services.domain.dao.dto.valid.utils.exception_util import CustomerException



app = Flask(__name__)

@app.route('/stone/register', methods=['POST'])
def stone_register():
    request_dict = request.json
    logging.info('request_data is = ' + str(request_dict))

    try:
        valid_register_param(request_dict)
        # 调用services
        return fullResponse(R201_CREATED,"regist done", "")
    except CustomerException, e:
        logging.error("".join(e))
        return fullResponse(R400_BADREQUEST, "".join(e), None)



