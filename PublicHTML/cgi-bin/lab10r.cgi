#!/usr/local/bin/ruby -w
puts "Content-type: text/html\n\n"
require 'cgi'
cgi = CGI.new
city = cgi['usercity']
prov = cgi['userprovince']
country = cgi['usercountry']
pict = cgi['picture']


puts "<html lang=en>"
puts "<head>"
puts "<title>City Display</title>"
puts "</head>"
puts "<body style='background-color:#000214; color:#b7e0ff; text-align:center; font-family:Verdana, sans-serif;'>"
puts "<h1> " + city.to_s.capitalize + ", " + prov.to_s.capitalize + ", in " + country.to_s.capitalize + ".</h1>" 
puts "<img src='" + pict.to_s + "' alt='city background' style='background-color:#b7e0ff;border: solid 6px #b7e0ff; border-radius:10px; max-width:100%; height:auto;'>"
puts "</body>"
puts "</html>" 