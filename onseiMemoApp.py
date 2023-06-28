
import PySimpleGUI as sg
import speech_recognition as sr
import json
import datetime


rec = sr.Recognizer()
mic = sr.Microphone()

TIMEOUT = 5000  # タイムアウト時間（単位：ミリ秒）
WAKE_WORD = "Ok Google"  # ウェイクワード

FONT = ("Hiragino Maru Gothic ProN", 20)
sg.theme("DarkGreen1")  #GUIのテーマ

json_file = open('memo.json', 'r')
json_dict = json.load(json_file)

#最初のレイアウト
WINDOW = sg.Window(
    "音声メモ", 
    [
        [sg.Text("お好きなタイミングで話しかけてください", size=(35, 1))],
        [sg.Text("認識結果: ", size=(40, 1), key="-RECOG_TEXT-")],
        [[sg.Checkbox(item["memo"], key=item["time"])] for item in json_dict ], #動的なチェックボックスの作成
        [sg.Button("削除",key="-delete-"),sg.Button("終了", key="-QUIT-")],
        [sg.Button("登録",key="-memo-"),sg.InputText()]
    ], 
    font=FONT
)

def submit(text):   #データの登録関数
    data={
            "memo":text,
            "time":str(datetime.datetime.now()),
            
        }   #この形式でデータを保存（json形式に準じて）
    with open('memo.json', 'r') as f:   #読み込み
        read_data = json.load(f)
    
    read_data.append(data)  #jsonデータを格納した配列に登録したい内容を追加

    with open('memo.json', 'w') as f:   #書き込み
        json.dump(read_data, f, indent=2, ensure_ascii=False)
    print("保存内容："+text)
    print("無事保存されました")

def redraw(WINDOW,text=""): #再描画関数（データ更新時リアルタイムで画面を更新するため）
    WINDOW.close()
    json_file = open('memo.json', 'r')
    json_dict = json.load(json_file)    #最新のデータを表示するためにjsonファイルを読み込み
    WINDOW = sg.Window(
        "音声メモ", 
        [
        [sg.Text("お好きなタイミングで話しかけてください", size=(35, 1))],
        [sg.Text("認識結果: "+text, size=(40, 1), key="-RECOG_TEXT-")],
        [[sg.Checkbox(item["memo"], key=item["time"])] for item in json_dict ], #上記で読み込んだデータで最新のデータを動的に表示
        [sg.Button("削除",key="-delete-"),sg.Button("終了", key="-QUIT-")],
        [sg.Button("登録",key="-memo-"),sg.InputText()]
        ],
        font=FONT
        )
    return WINDOW

disp_text=""
while True:
    print("1")  #解析用の出力（以下省略）
    event, values = WINDOW.read(timeout=TIMEOUT, timeout_key="-RECOG_TRIGGER-")
    print("2")

    if event in (sg.WIN_CLOSED, "-QUIT-"):
        print("3")
        break
    
    elif event in "-memo-":
        for value in values:
            count=0
            count_dict=0
            if value==0:
                if values[0]!="":
                    submit(values[0])   #入力ボックスに入力されたデータを登録関数に渡すことでjsonファイルに保存
                    WINDOW=redraw(WINDOW)  #データの保存後再描画
                else:
                    print("登録するデータが見つかりません")
            
    
    elif event == '-delete-':
        print("ーーーーーーーー")
        print("4")
        for value in values:
            count=0
            count_dict=0

            if values[value]==True:
                with open('memo.json') as fin:
                    data = [e for e in json.load(fin) if e["time"] != value]    #jsonデータからチェックボックスがつけられた項目以外をdata(変数)に格納し
                with open('memo.json', 'w') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)    #上記で記した様にチェックされた要素が除かれたjsonデータが格納されているdata（変数）をjsonファイルに出力（jsonファイルの更新）
                print("無事削除しました")
        print("5")
        WINDOW=redraw(WINDOW)  #データの変更後再描画
        print("6")
        print("ーーーーーーーー")
        print("7")
    
    elif event in "-RECOG_TRIGGER-":
        print("7-8")
        with mic as source:
            audio = rec.listen(source)
            print("8")

            try:
                text = rec.recognize_google(audio, language="ja-JP")
                print("9")

                if WAKE_WORD in text:   #"Ok Google"が含まれていた場合の処理
                    print("10")
                    text = text.replace(WAKE_WORD, "")  #"Ok Google"を認識結果から除く処理
                    print("11")

                    if text!="":    #認識結果がから文字じゃなかった場合
                        submit(text)    #JSONファイルに保存
                        WINDOW["-RECOG_TEXT-"].Update("認識結果: " + text)
                        WINDOW=redraw(WINDOW,text)  #データの保存後再描画
                    else:    #認識結果がから文字じゃなかった場合
                        WINDOW["-RECOG_TEXT-"].Update("聞き取れませんでした。")
                        print("聞き取れませんでした。")
                    print("12")

                else:
                    print("aaa")
                    WINDOW["-RECOG_TEXT-"].Update("認識結果: ")

            except sr.UnknownValueError:
                WINDOW["-RECOG_TEXT-"].Update("認識に失敗しました。")




WINDOW.close()

