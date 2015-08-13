import http
url = 'http://emspost.ru/api/rest/?method=ems.get.locations&type=cities&plain=true.html'

html = http.client.HTTPSConnection(url)
#Теперь записываешь файл
f = open('index.txt', 'w')
f.write(html)

