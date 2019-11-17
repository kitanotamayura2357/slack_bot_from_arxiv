import pprint
import arxiv
import pandas as pd
import time
import argparse
import os

parser = argparse.ArgumentParser(description='input author')
parser.add_argument('author', help='input author')
args = parser.parse_args()
paper_list = arxiv.query(query=f'au:"{args.author}"')

if paper_list:
    author_name = args.author.replace(" ","_")
    print(author_name)
    new_dir_path = f'test_arXiv_download/{author_name}'
    if not os.path.isdir(new_dir_path):
        os.mkdir(new_dir_path)

def get_paper_name(paper):

    authors_name = ','.join(paper['authors']).replace(' ', '.')
    paper_id = paper.get('id').split('/')[-1]
    paper_title = paper.get('title').replace('\n','').replace('  ',' ').replace(' ', '_').replace('/','-').replace(':','-').replace('"','~').replace(",","_")
    return  paper_id + "." + paper_title + "(" +authors_name +")"

for paper in paper_list:
    print(paper.get('title'))
    print(paper.get('id').split('/')[-1])
    print(paper.get('authors'))
    #print("len",len(get_paper_name(paper)))
    #arxiv.download(obj=paper, dirpath=f'test_arXiv_download/{author_name}', slugify=get_paper_name)
    arxiv.download(obj=paper, dirpath=f'test_arXiv_download/{author_name}')
