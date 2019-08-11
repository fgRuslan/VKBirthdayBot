#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Author: https://vk.com/id181265169
import vk, urllib.request, urllib.error, urllib.parse, json, random, time, datetime

config = {}# Создаём массив с конфигурацией

try:
	exec(compile(open("config.py", "rb").read(), "config.py", 'exec'), config)# Загружаем туда конфигурацию из файла
except IOError:
	print("No configuration file found, to create it, run auth.py")
	quit(1)
	
url = "https://oauth.vk.com/token?grant_type=password&client_id=3697615&client_secret=AlVXZFMUqyrnABp8ncuU&username=%s&password=%s" % (config['username'], config['password'])

try:
    r = urllib.request.urlopen(url)# Переходим по ссылке(логинимся)
except urllib.error.HTTPError:
    print("Authorization failed")
    quit(1)

r = r.read()# Читаем, что нам вернул сайт
token = json.loads(r)["access_token"]# Декодируем через JSON и читаем access_token(то, зачем мы вообще логинились)

session = vk.Session(access_token = token)# Создаём сессию ВК
api = vk.API(session)

littleemoji = ["&#127873;&#127881;&#127874;", "&#127874;&#127873;&#127881;"]
bigSmiles = [3466]
zeroone = [0,1]
useBigSmiles = random.choice(zeroone)

now = datetime.datetime.now()
print("Current date: %s.%s" % (now.day, now.month))

def sendMessage():
	try:
		r = api.friends.get()
		fCount = len(r)# Получаем к-во друзей
		for i in range(0, fCount):
			time.sleep(0.5)
			r = api.friends.get(count = 1, fields = "bdate", offset = i)[0]
			if 'bdate' in r:
				r1 = r['bdate']
				birthDate = r1.split(".")
				print("Birth date: %s.%s" % (birthDate[0], birthDate[1]))
				if (int(birthDate[0]) == now.day) and (int(birthDate[1]) == now.month):
					if(useBigSmiles == 1):
						r = api.messages.send(peer_id = r['uid'], sticker_id = random.choice(bigSmiles), v = 5.38)
					else:
						r = api.messages.send(peer_id = r['uid'], message = random.choice(littleemoji), v = 5.38)
			else:
				print("Birthday is not set by user")
	except KeyboardInterrupt:
		pass
	except vk.exceptions.VkAPIError as e:
		print("==========ERROR==========")
		print(e)
		print("=========================")

sendMessage()