from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys

#Your  Key
key = "Your Key"
#Your secret
secret = "Your Secret"
wait_time = 1

# コマンドラインの引数の1番目の値を取得。以下の場合は[cat]を取得
# python download.py cat 

### Write here the word you want to search about## Like "Spoon" and you will get the pictures of 'Spoon'
animalname = 'humanbeing'
savedir = "./"+'People'


# format:受け取るデータ(jsonで受け取る）
flickr = FlickrAPI(key, secret, format='parsed-json')

"""
text : 検索キーワード
per_page : 取得したいデータの件数
media : 検索するデータの種類
sort : データの並び
safe_seach :　UIコンテンツの表示有無
extras : 取得したいオプションの値(url_q 画像のアドレス情報)
"""
result  = flickr.photos.search(
    text = animalname,
    per_page = 5000,
    media = 'photos',
    sort = 'relevance',
    safe_seach = 1,
    extras = 'url_q, licence'
)

# 結果
photos = result['photos']
pprint(photos)


for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'

   # 重複したファイルが存在する場合スキップする。
    if os.path.exists(filepath):continue
   # 画像データをダウンロードする
    urlretrieve(url_q, filepath)
   # サーバーに負荷がかからないよう、1秒待機する
    time.sleep(wait_time)