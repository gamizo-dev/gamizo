from os import replace
import  requests
from bs4 import BeautifulSoup
def takeinput(url):

    r = requests.get(url)
    htmlContent = r.content

    soup = BeautifulSoup(htmlContent,'html.parser')

    title = soup.title
    category=soup.find("a",{"itemprop" :"genre"}).text
    # print(title.string)

    s = title.string
    # s = s.replace('- Apps on Google Play',' ')
    s=s[:-21]

    cat={'name': s,'category': category}
    return cat

# imageclass = soup.find('div', class_="xSyT2c")

# for 
# print(images)