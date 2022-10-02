# Maaz Sabah Uddin
# A00257491
import requests, bs4

url = "https://module1-1.maazsabahuddin.repl.co/"
res = requests.get(url + "pages/experience.html")

parseSoup = bs4.BeautifulSoup(res.text, "html.parser")

paragraphs = parseSoup.select("p")
print(paragraphs[2])

response = requests.get(url)
parserIndex = bs4.BeautifulSoup(response.text, "html.parser")
pdf_link = parserIndex.select("#pdf")
print(f"This is the pdf link {pdf_link[0].get('href')}")

with open('technology.pdf', 'wb') as f:
    f.write(requests.get(pdf_link[0].get('href')).content)
    f.close()
