# code to download image from web page

from urllib import request
url = "https://unsplash.com/"
web_page = request.urlopen(url).read().decode("utf-8")
img_links = []
starting_pos = 0
no_of_imgs = web_page.count("<img")
for img in range(no_of_imgs):
    img_start = web_page.find("<img", starting_pos)
    src_start = web_page.find("src=", img_start)
    src_end = web_page.find('"', src_start+5)
    src = web_page[src_start+5:src_end]
    img_links.append(src)
    starting_pos = src_end
    counter = 0
for img in img_links:
    img_data = request.urlopen(img).read()
    img_file = open(f"{counter}.jpg", "wb")
    img_file.write(img_data)
    img_file.close()
    counter += 1