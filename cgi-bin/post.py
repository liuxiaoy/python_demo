#!/usr/bin/env python
# Written by Vamei
import cgi

form = cgi.FieldStorage()

# Output to stdout, CGIHttpServer will take this as response to the client
print "Content-Type: text/html"  # HTML is following
print  # blank line, end of headers
print "<p>Hello world!</p>"  # Start of content
print "<p>" + repr(form['firstname']) + "</p>"
