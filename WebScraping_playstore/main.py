import  requests
from bs4 import BeautifulSoup
url ="https://play.google.com/store/apps/details?id=com.google.android.keep"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent,'html.parser')

title = soup.title
print(title.string)
