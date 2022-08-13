import requests

headers = {
	'Accept':'application/json, text/plain, */*',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'en-US,en;q=0.9',
	'Connection':'keep-alive',
	'Content-Length':'123',
	'Content-Type':'application/json;charset=UTF-8',
	'Host':'1xbet.com',
	'Origin':'https://1xbet.com',
	'Referer':'https://1xbet.com/en/allgamesentrance/fortuneapple',
	'sec-ch-ua':'\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"',
	'sec-ch-ua-mobile':'?0',
	'sec-ch-ua-platform':'\"Windows\"',
	'Sec-Fetch-Dest':'empty',
	'Sec-Fetch-Mode':'cors',
	'Sec-Fetch-Site':'same-origin',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'X-Requested-With':'XMLHttpRequest'
}

session = requests.Session()
session.headers.update(headers)


cookies = """__"""

c = list(map(lambda x:x.split('='), cookies.split('; ')))

cookies = {}
for e in c:
	cookies[e[0]] = e[1]

# print(cookies)
session.cookies.update(cookies)
