import urllib.request
from bs4 import BeautifulSoup

def download_file(url):
    file_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, file_name)
    print(file_name + " downloaded")
    
html_doc = urllib.request.urlopen("https://paulminors.com/resources/book-summaries/download/").read()
soup = BeautifulSoup(html_doc, 'html.parser')
pdf_urls = [link.get('href') for link in soup.find_all('a') if (link.get('href') != None and link.get('href').endswith('pdf'))]

print('About to download ' + str(len(pdf_urls))  + ' pdf files')

for pdf_url in pdf_urls:
    download_file(pdf_url)
