from urllib import request

def crawler (url):
    list =[]
    file = request.urlopen(url)
    content = file.read()
    try:
        html = content.decode('cp1252')
    except:
        html = content.decode()
    
    html = html.replace('"','"')
    a = html.find('<a')
    while (a!=-1):
        s = html.find('href=',a)+len('href=')+1
        e = html.find('"',s)
        link = html[s:e]
        a = html.find ('<a',e)

        if (not link.startswith('https')):
            link = url + link
        list.append(link)
    return list

links = crawler('https://www.w3schools.com/html/html_links.asp')

for link in links:
    print (link)
    print ('---------------------------------')