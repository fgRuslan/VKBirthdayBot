#!/usr/bin/python
#-*- coding utf8 -*-
# Author: https://vk.com/id181265169
import vk, urllib2, json, random

config = {}# Создаём массив с конфигурацией

try:
	execfile("config.py", config)# Загружаем туда конфигурацию из файла
except IOError:
	print u"Нету файла конфигурации, чтобы его создать, запустите файл auth.py"
	quit(1)
	
url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])

try:
    r = urllib2.urlopen(url)# Переходим по ссылке(логинимся)
except urllib2.HTTPError:
    print u"Не получилось авторизоваться (возможно неправильно указаны логин или пароль)"
    quit(1)

r = r.read()# Читаем, что нам вернул сайт
token = json.loads(r)["access_token"]# Декодируем через JSON и читаем access_token(то, зачем мы вообще логинились)

session = vk.Session(access_token = token)# Создаём сессию ВК
api = vk.API(session)

phrases = [u"Message 1", u"Message 2", u"Message 3", u"Message 4"]

def sendMessage():
	try:
		r = api.friends.get()
		fCount = len(r)# Получаем к-во друзей
		for i in range(1, fCount):
			r = api.friends.get(count = 1, fields = "bdate", offset = i)
			print r
	except:
		print u"Произошла ошибка при отправке сообщения"
		return

sendMessage()