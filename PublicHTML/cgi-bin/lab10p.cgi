#!/usr/bin/python -W

import cgi
import os
import cgitb

form = cgi.FieldStorage()
city = form["usercity"].value
prov = form["userprovince"].value
country = form["usercountry"].value
pict = form["picture"].value

print "Content-type:text/html\n\n"
print "<html lang=en>"
print "<head>"
print "<title>City Display</title>"
print "</head>"
print "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'>"
print "<h1> This is ", city.upper(), ", ", prov.upper(), ", in ", country.upper(), ".</h1>" 
print "<img src=", pict, " alt='city background' style='background-color:#b7e0ff;border: solid 6px #b7e0ff; border-radius:10px; max-width:80%; height:auto;'>"
print "</body>"
print "</html>"


