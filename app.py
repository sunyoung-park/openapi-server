#flask 프레임워크를 이용한, Restful API 서버 개발

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from config import Config
from resources.naver import ChineseResource, NewsResource

# 기본 구조
app = Flask(__name__)

# 환경변수 세팅
app.config.from_object(Config)
# JWT 매니저를 초기화
jwt = JWTManager(app)


api = Api(app)

api.add_resource(ChineseResource,'/chinese')
api.add_resource(NewsResource,'/news')


if __name__=='__main__':
    app.run()
