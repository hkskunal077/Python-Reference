##Beautiful Soup Web Scraping
##For avoiding redundancy we have Tags instead of Instruction Text, Tags
##allow us to have multiple instance of same type of Tags.
##Markup Language is used for marking up the text, to identify what part
##is what part. Modern markup systems use component name to later process
##those names to apply formatting or other processing, like XML, HTML.
##Conventional markups like Troff, TeX, LaTeX have typesetting instruction.
##
##We can structurize the data/information by scraping and it will be easily
##available for read/write data. We extract feeds, data from websites to
##collect and analyze the data. 

from bs4 import BeautifulSoup as bs
import requests


url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
#Gets the web page
if req != False:
    print("True", req)


soup = bs(req.text, "lxml")
#gets all of the textual part
if soup != False:
    print("Got the complete text")
print(soup.title)
#printing only the title text.


count = 0
for link in soup.find_all('a'):
    print(link.get('href'))
    count = count + 1
print(count)
#'a' assings the hyperlink and href is just one of the attribtues of
#it and it contains the actual destination of hyperlink.
