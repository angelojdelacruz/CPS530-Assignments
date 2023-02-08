#!/usr/bin/perl -wT 
use CGI ':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 

use strict;
print "Content-type: text/html\n\n";

print "<!DOCTYPE html>";
print "<html><head>";
print qq(<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">);
print "<title>First Perl Program</title></head>";

print "<body>";
print qq(<div style="color:green; font-size:5em; text-align:center; font-family:pacifico">); 
print "My first perl program\n<br>";


print "</div></body></html>";