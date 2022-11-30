from flask import Flask, render_template
from utils.extract_news_titles import *
application = Flask(__name__, static_url_path='/static')

@application.route('/')
def hello_world():
    ynet_str = get_ynet_articles()
    one_sport_str = get_one_articles()
    globs_str = get_globs_articles()
    return render_template('./screen1/lobby_screen1.html', ynet_titles_str=ynet_str, globs_titles_str=globs_str, one_titles_str=one_sport_str)

if __name__ == '__main__':
   application.run()