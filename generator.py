import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
import config
import shutil
import logging

def generate_main_pages():
    for page in os.listdir('template/home'):
        env = Environment(loader=PackageLoader('generator', f'template/'))
        
        configs = {item: getattr(config, item) for item in dir(config) if not item.startswith("__")}
        
        index_html = index_template.render(configs)
        with open(f'output/{page}', 'w') as file:
            file.write(index_html)

def generate_static():
    try:
        shutil.rmtree('output/static')
    except Exception as e:
        logging.info('output directory created')
    shutil.copytree('template/static', 'output/static')

if __name__ == '__home__':
    if 'output' not in os.listdir('.'):
        os.mkdir('output')
    generate_main_pages()
    generate_static()