f=open('data.txt')      #октрываем файл для чтения(режим r - является режимом по умолчанию
text= f.read()          #читаем содержимое файла одной строкой
print(text)
print(text.split())     # разбиваем содержимое файла
texts=f.readline()
print(texts)
data= open('data.txt','rb').read() #открываем файл для чтения в байтовом режиме(rb) и тут же читается
print(data)
print(data[4:8])
