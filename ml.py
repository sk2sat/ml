#!/usr//bin/env python3
# -*- coding: utf-8 -*-

import sys
import smtplib
from email.mime.text import MIMEText
import datetime

jp = 'iso-2022-jp'

# 設定の読み込み
set_file = open('setting.cfg', 'r')

# 1行目はFromアドレス
from_addr = set_file.readline()
passwd = set_file.readline()
print('From = ' + from_addr)

# 宛先のリストファイル
addr_file = open('addrs.lst', 'r')

to_addrs = addr_file.readlines()

#print(addr_file.readline())

# 本文の読み込み
body_file = open('body.txt', 'r')
title = body_file.readline()	# タイトルの読み込み
raw_body = body_file.read()

body = MIMEText(raw_body)

body['Subject'] = title
body['From'] = from_addr
body['To'] = ','.join(to_addrs)

print(body)

# メールの送信 (Gmail)
#try:
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(from_addr, passwd)
s.send_message(body)
s.close()
print('メールの送信に成功しました。')
#except Exception:
#print("Error: can't send mail")

