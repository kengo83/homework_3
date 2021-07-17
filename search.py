import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word,csv_file):
    # 検索対象取得
    df=pd.read_csv("./{}".format(csv_file))
    source=list(df["name"])
    print(source)

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("『{}』はあります".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("『{}』はありません".format(word))
        eel.view_log_js("『{}』を登録します".format(word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(csv_file),encoding="utf_8-sig")
    print(source)

kimetsu_search('むざん','sample01.csv')

