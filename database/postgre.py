#!/usr/bin/env python3
#coding: UTF-8

import psycopg2

def get_connection():
	return psycopg2.connect("host=127.0.0.1 port=5432 dbname=pi password=rspi")

def fetchExquted(query):
	with get_connection() as conn:
		with conn.cursor() as cur:
			return cur.execute(query)

# 実行
with get_connection() as conn:
	with conn.cursor() as cur:	
		cur.execute('SELECT * FROM mwlapp_status')
		
		# 列名を取得
		colnames= [col.name for col in cur.description]
		for c in colnames:
			print(repr(c))

		# レコードの取得
		print('print all rows')
		for r in cur:
			print(repr(r))
			
		# パラメータをクエリに埋め込む
		print('example using where')
		cur.execute('SELECT * FROM mwlapp_status WHERE name= %s',('1号機',))
		rows= cur.fetchall()	# これでexcute の結果がcur から消えるらしい
		for r in rows:
			print(repr(r))

		# UPDATE (レコードの更新）
		cur.execute('UPDATE mwlapp_status SET mesh=98.7 WHERE id= %s', ('1'))

