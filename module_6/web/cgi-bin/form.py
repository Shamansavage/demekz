import cgi
import html

form = cgi.FieldStorage()
text1 = form.getfirst("LOGIN", "UNKNOWN")
text2 = form.getfirst("PASSWORD", "UNKNOWN")
text1 = html.escape(text1)
text2 = html.escape(text2)

print("Content-type: text/html; charset=utf-8\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>OBRABOTKA</title>
        </head>
        <body>""")

print("<h1>OBRABOTKA!</h1>")
print("<p>TEXT_1: {}</p>".format(text1))
print("<p>TEXT_2: {}</p>".format(text2))

print("""</body>
        </html>""")