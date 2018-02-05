import urllib.request

my_web = urllib.request.urlopen('https://www.google.com')

print(my_web.read())