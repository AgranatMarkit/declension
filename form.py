#!/usr/bin/env python3
import cgi
import html
import testovoe

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text1 = html.escape(text1)
text = testovoe.main(str(text1))

print("Content-type: text/html\n")
print("""
        <!DOCTYPE HTML>
        <html>
        <head>
            
            <link type="text/css" rel="stylesheet" href="../style.css">
            <title>Тестовое задание</title>
        </head>
        <body>
        <div class="center">
        <h1>Склонятор</h1>
        <form action="/cgi-bin/form.py">
    	<p>Введите слово:</p>
    	""")
print('<input type="text" name="TEXT_1" value="{}">'.format(text1))
print("""
        <br>
        <br>
        
        <input type="submit" value="Просколонять">
        <p>Результат:</p>
        <textarea id="result" wrap="hard">%s</textarea>
        </form>
        </div>
        </body>
        </html>"""%text)
