from flask import request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource
import requests
from mysql_connection import get_connection
from mysql.connector import Error


class ChineseResource(Resource) :

    def post(self) :
        
        data = request.get_json()
        
        # 클라이언트가 입력한 body의 json 가져오기
        # 네이버의 파파고 API를 호출하여
        # 결과를 가져온다.

        # 파파고 API의 문서를 보고,
        # 어떤 데이터를 보내야 하는지 파악하여
        # requests의 get, post, put, delete 등의
        # 함수를 이용하여 호출하면 된다.

        req_data = {
                        "source":"ko",
                        "target":"zh-CN",
                        "text":data['sentence']
                    }
        
        req_header ={
                        "X-Naver-Client-Id":"7V89Lh5rHWswlUoe6D6B",
                        "X-Naver-Client-Secret":"9l22vo6_9b"

                   }

        response = requests.post('https://openapi.naver.com/v1/papago/n2mt',
                     req_data,
                     headers=req_header)
        
        # 뒤에 s 붙은 것으로 위에 request는 flask 라이브러리랑 다른 라이브러리
        
        # 데이터를 파파고 서버로 부터 받아왔으니, 
        # 우리가 필요한 데이터만 뽑아내면 된다.

        print(response)
        
        # 원하는 데이터를 뽑기 위해서는
        # 받아온 데이터를 다시 json으로 저장 ★★★★★

        response = response.json()

        print()
        print(response)

        chinese = response['message']['result']['translatedText']

        return {"result" : "success",
                "chinese": chinese}, 200


class NewsResource(Resource) :

    def get(self) :

        keyword = request.args.get('query')

        #네이버 뉴스 검색 API를 호출
        

        

        query_string = {                      
                        "query":keyword,
                        "display":30,
                        "sort":"date"}
        
        
        
        naver_header ={
                        "X-Naver-Client-Id":"7V89Lh5rHWswlUoe6D6B",
                        "X-Naver-Client-Secret":"9l22vo6_9b"

                   }

        response = requests.get('https://openapi.naver.com/v1/search/news.json',
                     query_string,
                     headers=naver_header)
        
        

        response = response.json()



        print()
        print(response)

        return {"result" : "success",                
                "items": response['items'],
                "count" : len(response['items'])}, 200