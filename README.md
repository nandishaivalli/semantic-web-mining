# simantic-web-mining
## Meaning based web mining and scraping.

*A new type of search engine*.

Many seacrh engine like google,bing etc offer a better , robust way of searching any data from the internet.In this project we prupose a model that search or ranks pages based on the  simantic simlarity between the search query and the data in the website(for instance all the headers and paragraps in the page)

Using the concept of web scraping and NLP combined to produce the final results.
### 1. Web Scraping
[Scrapy](https://docs.scrapy.org/en/latest/intro/install.html ) + [Beautifulsoup](https://pypi.org/project/beautifulsoup4/ "")

### 2. Data Comparision (NLP)
[Universal sentence encoder](https://tfhub.dev/google/universal-sentence-encoder/4 " ") + [cosine similarity](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html ) 

---

To Run

``` scrapy crawl getData -o data.json``` a data.json file is created with the scraped items.

open the `jupyter notebook` to run the remaining code

---
