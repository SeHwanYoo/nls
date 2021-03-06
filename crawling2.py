# %% 

import requests 
from bs4 import BeautifulSoup
from tqdm import tqdm


# %%
# 브리콜라주 (bri_model) 

texts = '' 
# 1800
for i in tqdm(range(0, 50, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EB%B8%8C%EB%A6%AC%ED%81%B4%EB%9D%BC%EC%A3%BC&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%EB%B8%8C%EB%A6%AC%EC%BD%9C%EB%9D%BC%EC%A3%BC'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'


for i in tqdm(range(0, 10, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EB%B8%8C%EB%A6%AC%EC%BD%9C%EB%9D%BC%EC%A3%BC&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%EB%B8%8C%EB%A6%AC%EA%BC%B4%EB%9D%BC%EC%A3%BC'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'



# %%
# 사회적자본(social_funds_model)

texts = '' 
# 1800
for i in tqdm(range(0, 8560, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EA%B8%B0%EC%97%85%EA%B0%80%EC%A7%80%ED%96%A5%EC%84%B1&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EC%9E%90%EB%B3%B8'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'


# %% 
# 기업가지향성 (aim_model)

texts = '' 
# 1800
for i in tqdm(range(0, 320, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%ED%98%81%EC%8B%A0&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%EA%B8%B0%EC%97%85%EA%B0%80%EC%A7%80%ED%96%A5%EC%84%B1'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'



# %%
# 혁신 (inno_model)

texts = '' 
# 1800
for i in tqdm(range(0, 20810, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B8%B0%EC%97%85&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%ED%98%81%EC%8B%A0'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'



# %% 
# 사회적기업 (social_model)
texts = '' 
# 1800
for i in tqdm(range(0, 15620, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&query=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B8%B0%EC%97%85&queryText=&iStartCount='+ str(i) + '&iGroupView=5&icate=all&colName=bib_t&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&pageScale=10&orderBy=&fsearchMethod=&isFDetailSearch=&sflag=1&searchQuery=%EC%82%AC%ED%9A%8C%EC%A0%81+%EA%B8%B0%EC%97%85&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&resultKeyword=&pageNumber=1&p_year1=&p_year2=&dorg_storage=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&language_code=&ccl_code=&language=&inside_outside=&fric_yn=&image_yn=&regnm=&gubun=&kdc=&ttsUseYn='
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'


# %%
# 멘토링
texts = '' 
# 1800
for i in tqdm(range(0, 1800, 10)):
    url = 'http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EB%A9%98%ED%86%A0%EB%A7%81&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=' + str(i) + '&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=&resultKeyword=&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&query=%EB%A9%98%ED%86%A0%EB%A7%81'
    req = requests.get(url)
    html = req.text

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('p.title > a')

    for i in range(len(titles)):
        texts += ' ' + titles[i].get_text() + '\n'
# %%
print(texts)



# %% 
## 특수문자 처리
import re

parse_text = texts

clean_lines = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', parse_text)
p = re.compile('[^0-9]')
clean_lines = "".join(p.findall(clean_lines))
# %%

print(parse_text)
print('------------------------')
print(clean_lines)


# %% stopwords 

f = open('stopwords.txt', mode='r', encoding='utf-8')

lines = f.readlines()

stop_words = ''
for ll in lines:
    # print(ll)
    stop_words += ' ' + ll

# %%
from konlpy.tag import Okt

# okt = Okt() 
# results = okt.nouns(clean_lines)

# stopwords_results = []

# for rr in results:

#     if rr not in stop_words and len(rr) > 1:
#         stopwords_results.append(rr)

okt = Okt() 

stopwords_results = []

for ll in clean_lines.split('\n'):
    stopwords_results.append(okt.nouns(ll))

# %%
print(stopwords_results)

# for ss in stopwords_results:

#     if len(ss) < 2:
#         print(ss)

# %%
from gensim.models import FastText

ft_model = FastText(stopwords_results, size=100, window=5, min_count=5, workers=4, sg=1)

# %%

# %%
ft_model.save('bri_model')

# %%

print(ft_model.wv.most_similar('멘토링', topn=10))
# print(ft_model.wv.similarity('멘토링', '창업'))
# %%
