import os
import markdown2 as markdown

def convert_to_html():
    PATH = 'templates/news/content/'
    dirs = os.listdir(PATH)
    news = []
    for arq in dirs:
        news.append(markdown.markdown_path(PATH+arq))
    return news