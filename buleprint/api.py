import json
from time import time

import requests
from flask import Blueprint, jsonify, request

api_bp = Blueprint('api',__name__,url_prefix='/api')


@api_bp.route("/everyday_soup")
def soup():
    url = 'http://open.iciba.com/dsapi/'  # 词霸免费开放的jsonAPI接口
    r = requests.get(url)
    all_content = json.loads(r.text)  # 获取到json格式的内容，内容很多,json.loads: 将str转成dict
    English = all_content['content']  # 提取json中的英文鸡汤
    Chinese = all_content['note']  # 提取json中的中文鸡汤
    everyday_soup = {
        "Chinese" : Chinese + "\n",
        "English" : English,
    }
    return jsonify(everyday_soup)  # 返回结果


@api_bp.route("/upload_img", methods=["POST"])
def upload_img():
    files = dict(request.files.lists())
    print(files.items())

    filename = ""
    for img, file in files.items():
        file = file[0]
        filename = f"{int(time())}_{file.filename}"
        file.save("static/img/upload/"+filename)

    result = {
        "errno": 0,
        "data": {
            "url": "/static/img/upload/" + filename,
        }
    }
    return jsonify(result)