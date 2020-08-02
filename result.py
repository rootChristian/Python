#coding:utf-8

import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()

print("content-type: text/html; charset=utf-8\n")

html = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <title>My page web with Python and HTML </title>
</head>
<body>
"""
print(html)

try:
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"<p>Hello, {username}!</p>")
    else:
        raise Exception("User not transmit...")
except:
    print("<p>User not transmit...</p>")
