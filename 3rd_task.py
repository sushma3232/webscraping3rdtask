import requests
import json
from bs4 import BeautifulSoup
rel=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(rel.content,"html.parser")
movies=soup.find("tbody",class_="lister-list",).find_all("tr")
list=[]
for movie in movies:
    dic={"movie":"","year":"","rating":"","position":"","link":""}
    name=movie.find('td',class_="titleColumn").a.text
    ratings=movie.find('td',class_="ratingColumn imdbRating").strong.text
    position=movie.find("td",class_='titleColumn').get_text(strip=True).split('.')[0]
    year=movie.find("td",class_="titleColumn").span.text.strip("()")
    url=movie.find("td",class_="titleColumn").a["href"]
    link="https://www.midb.com/"+url
    dic["movie"]=name
    dic["year"]=year
    dic["rating"]=ratings
    dic["position"]=position
    dic["link"]=link
    list.append(dic)
# print(list[0]["year"])
answer_dic={}
list60=[]
list70=[]
list80=[]
list2=[]
i=0
while i<len(list):
    if list[i]["year"]>="1960" and list[i]["year"]<="1969":
        list60.append(list[i])
        answer_dic["1960"]=list60
    if list[i]["year"]>="1970" and list[i]["year"]<="1979":
        list70.append(list[i])
        answer_dic["1970"]=list70
    if list[i]["year"]>="1980" and list[i]["year"]<="1989":
        list80.append(list[i])
        answer_dic["1980"]=list80
    
    if list[i]["year"]>="2000" and list[i]["year"]<="2009":
        list2.append(list[i])
        answer_dic["2000"]=list2
        
    i=i+1

with open("third_task.json","w")as f:
    json.dump(answer_dic,f,indent=8)
