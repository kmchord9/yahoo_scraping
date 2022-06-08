##https://atmarkit.itmedia.co.jp/ait/articles/1910/18/news015.html
##https://www.hobby-happymylife.com/%e3%83%97%e3%83%ad%e3%82%b0%e3%83%a9%e3%83%9f%e3%83%b3%e3%82%b0/python_scraping_beautifulsoup_id/
##https://naruport.com/blog/2019/12/27/bs4-href/


from urllib import request
from bs4 import BeautifulSoup
from time import sleep


def getSoupData(url):
    response = request.urlopen(url)
    soup = BeautifulSoup(response, "html.parser")
    return soup


url="https://www.yahoo.co.jp/"
soupHome = getSoupData(url)

homeDataLists = soupHome.find(id="tabpanelTopics1").find("ul").find_all("li")

for homeDataList in homeDataLists:
    print("〇"+homeDataList.find("h1").string)
    articleUrl = homeDataList.find("a").get('href')
    print(articleUrl)
    soupArticle = getSoupData(articleUrl)

    articleDataLists = soupArticle.find(id="uamods-pickup").find_all("a")

    sleep(1)

    for articleDataList in articleDataLists:
        if(articleDataList.string=="記事全文を読む"):
            print("-------------------------------------------------")
            nextPageUrl = articleDataList.get("href")
            mainArticleSoup = getSoupData(nextPageUrl)
            #print(mainArticleSoup.find(class_='article_body highLightSearchTarget').find(class_='sc-iqzUVk').text)
            try:
                print(mainArticleSoup.find(class_='article_body').text)
            except AttributeError:
                print(mainArticleSoup.find(class_='articleBody').text)

            except Exception as e:
                print(e)

            sleep(1)
