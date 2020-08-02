#coding:utf-8

import cgi
import http.cookies
import datetime
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")
my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True

print(my_cookie.output())

print("content-type: text/html; charset=utf-8\n")

#print(my_cookie.output())

html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>My page web with Python and HTML </title>
</head>
<body>
    <h1><center>WELCOME IN MY STORE</h1>
    <h2>Cookies in Python</p2>
    <hr>
</body>
</html>
"""

print(html)

#=====================================================================
'''
html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>My page web with Python and HTML </title>
</head>
<body>
    <h1><center>WELCOME IN MY STORE</h1>
    <h2>Cookies in Python</p2>
    <hr>

    <form method="post" action="result.py">
        <p><input type="text" name="username" placeholder="USERNAME">
        <input type="submit" value="Send"></p>
    </form>
</body>
</html>
"""

print(html)
'''
