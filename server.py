
from wsgiref.simple_server import make_server
import json

API_PORT = 2000


# 文字列のバイトサイズを計算する関数
def getStringByteSize(str):
    return len(str.encode('utf-8'))


# APIが呼ばれた時に実行される関数
def app(environ, response):
    json_file = open('memo.json', 'r')  #同一ディレクトリにあるmemo.jsonを開いて
    json_dict = json.load(json_file)    #データを変数に格納

    json_data={
    "results":json_dict
    }   #スマホでjsonデータを解析する時に解析しやすい形に変換

    #以下の形でmemo.jsonのデータを返す
    # json_data={
    # "results":[
    # {
    #     "memo": " 明日の天気",
    #     "time": "2023-01-17 23:11:22.737250"
    # },{
    #     "memo": " 明日の映画は何を見るか決める",
    #     "time": "2023-01-17 23:16:52.981580"
    # },{
    #     "memo": " 明日の道を調べる",
    #     "time": "2023-01-18 02:44:27.884784"
    # },{
    #     "memo": " 明日 シャープペンシル 買いに行く",
    #     "time": "2023-01-18 02:45:24.879361"
    # }
    # ]
    # }

# jsonのレスポンス
    content_length = getStringByteSize(json.dumps(json_data)) # Content-Lengthを計算
    status = '200 OK'
    header = [
        ('Access-Control-Allow-Origin', '*'),   # 許可するアクセス
        ('Access-Control-Allow-Methods', '*'),  # 許可するメソッド
        ('Access-Control-Allow-Headers', "X-Requested-With, Origin, X-Csrftoken, Content-Type, Accept"), # 許可するヘッダー
        ('Content-type', 'application/json; charset=utf-8'), # utf-8のjson形式
        ('Content-Length', str(content_length)) # Content-Lengthが合っていないとブラウザエラー
    ]
    response(status, header)
    return [json.dumps(json_data).encode("utf-8")]


# APIサーバを実行する関数
with make_server('', API_PORT, app) as httpd:
    print("Start API. URL is http://localhost:" + str(API_PORT) + "/ ...")
    httpd.serve_forever()
