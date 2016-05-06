#!/usr/bin/env python3
import cgi
import html
import testovoe
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())



form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text1 = html.escape(text1)
text = testovoe.main(text1)

a = """
<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset = "utf-8">
            <link type="text/css" rel="stylesheet" href="../style.css">
            <title>Тестовое задание</title>
        </head>
        <body>
        <div class="center">
        <h1>Склонятор</h1>
        <form action="/cgi-bin/form.py" method="post">
        <p>Введите слово:</p>
        <input type="text" name="TEXT_1" value="%s">
        <br>
        <br>
        
        <input type="submit" value="Просколонять">
        <p>Результат:</p>
        <textarea id="result" wrap="hard">%s</textarea>
        </form>
        </div>
        </body>
        </html>
"""%(text1,text)
print("Content-type: text/html\n")
print(a)