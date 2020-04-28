# -*- Coding: utf-8 -*-

import sys
import sqlite3
import datetime

from HTTPClient import HTTPClient
from SQLiteClient import SQLiteClient
from MusicParser import MusicParser


MAX = 10

httpClient = HTTPClient()
sqliteClient = SQLiteClient("lovelive.db")

musicParser = MusicParser()
songs = musicParser.get_songs()

print(songs)

sys.exit()


for si in range(1, MAX + 1):

    # soup_song、soup_eventで区別する
    soup = httpClient.connect(URL_SONGS + str(si))

    #### タイトルを取得
    span = soup.select(".card-title")[0]

    title = span.get_text()
    print(title)

    #### 発売日の日付を取得
    # 後述のtableと区別する
    table = soup.select("div.s12")[0]

    # TODO: 複数公演ある場合に目的の日付が取れてるか確認
    tr = table.select("tr")[3]
    td = tr.select("td")[0]

    date_release = datetime.datetime.strptime(td.get_text(), "%Y/%m/%d")
    print(date_release)

    #### 初披露日の日付を取得

    trs = soup.select("tr")
    tr = trs[6]
    td = tr.select("td")[0]
    
    soup_event = httpClient.connect(URL_TOP + td.a.get("href"))

    table = soup_event.select("table")[0]
    tr = table.select("tr")[0]
    
    tds = tr.select("td")
    len_tds = len(tds)
    td = tds[len_tds - 1]

    date_perform = datetime.datetime.strptime(td.get_text(),  "%Y/%m/%d %H:%M")
    print(date_perform)
    print()

    # query = "INSERT INTO song VALUES("
    # query += str(si) + ", '" + title + "', '" + str(date_release) + "', '" + str(date_perform) + "')"
    # print(query)
    # sqliteClient.insert(query)