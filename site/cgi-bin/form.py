# -*- coding: utf-8 -*- 
#!/usr/bin/env python3

import cgi
import html

form = cgi.FieldStorage()
text1= form.getfirst('TEXT_1', 'не задано')
text2= form.getfirst('TEXT_2', 'не задано')
text1=html.escape(text1)
text2=html.escape(text2)
print("Content-type: text/html\n")
text="""<!DOCTYPE HTML>
        <html>
        <head>
            <title>Обработка данных форм</title>
        </head>
        <body>"""

print(text)

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")
