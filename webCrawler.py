from urllib import request

URL = "http://olympus.realpython.org/profiles/poseidon"
webConnection = request.urlopen(URL)
savePathAndFile = "web.html"
webPageAsHTML = webConnection.read().decode("cp1252")
webPageAsHTML = webPageAsHTML.replace("/static/poseidon.jpg", "http://olympus.realpython.org/static/poseidon.jpg")
print(webPageAsHTML)
fileObj = open(savePathAndFile, "w")
fileObj.write(webPageAsHTML)
fileObj.close()