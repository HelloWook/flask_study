from flask import Flask
import random


app = Flask(__name__)

topics = [
    {"id": 1, "title": "html", "body": "html is ..."},
    {"id": 2, "title": "css", "body": "css is ..."},
    {"id": 3, "title": "javascript", "body": "javascript is ..."},
]  # 데이터베이스로 해야징 ..


def template(contents, content):  # 똑같은 본문을 작성하기 위해 생성한 함수
    return f"""<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Study</title>
</head>
<body>
    <h1><a href="/">WEB</a></h1>
    <ol>
       {contents}
    </ol>
    {content}
</body>
</html>"""


def get_contents():
    litags = ""
    for topic in topics:
        litags = litags + f'<li><a href =/read/{topic["id"]}/>{topic["title"]}</a></li>'
    return litags


@app.route("/")
def index():
    get_contents()
    return template(
        get_contents(), "<h2>welcome</h2> web is..."
    )  # "random : <strong>" + str(random.random()) + "</strong>"  # 기본적으로 return은 문자열을 받음, 플라스크를 통해서 동적인 html코드 작성이 가능함


# 라우팅 : 플라스크에서는 함수를 통해서 라우팅함 -> 라우터 -> 라우팅을 해주는 기술 플라스크에서는 @app.route("/") 함수를 사용
@app.route("/create/")
def crate():
    return "create"


@app.route("/read/<int:id>/")  # 플라스크가 정수로 컨버팅
def read(id):  # 라우트의 <값>을주면 받는 함수의 파라매터가 받는다
    litags = ""
    for topic in topics:
        litags = litags + f'<li><a href =/read/{topic["id"]}/>{topic["title"]}</a></li>'
    for topic in topics:
        if id == topic["id"]:
            title = topic["title"]
            body = topic["body"]
            break
    return template(get_contents(), f"<h2>{title}</h2>{body}")


app.run(port=5001, debug=True)
# // debug = true를 사용하면 자동으로 리로딩
