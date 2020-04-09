from flask import Flask, render_template, json
import time
import requests
from bs4 import BeautifulSoup as bs


app = Flask(__name__)


@app.route('/book')
def booklist_api():
    """API for Booklist"""

    text = requests.get("https://www.gutenberg.org/browse/scores/top#books-last7")
    soup= bs(text.content, 'html.parser')
    last_30 = soup.find(id = "books-last30")
    siblings = list(last_30.findNextSiblings())
    book_list= []
    book_array=[]
    for ul in siblings:
        for li in ul.findAll('li'):
            book_list.append(li)
    # removing the ul element from the list
    book_list.pop(0)

    for li in book_list[:1]:
        book_dict={}
        book_title_auth= li.text.split("by", 1)
        book_title= book_title_auth[0]
        if len(book_title_auth)>1:
            book_auth= book_title_auth[1][:-7]
        else:
            book_auth= "No author"
        book_url=li.findAll('a')[0]['href']
        book_dict = {"title": book_title, "url":book_url, "author":book_auth}
    
        book_array.append(book_dict)
    book_array= json.dumps(book_dict)

    return book_array

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
