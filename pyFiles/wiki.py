import wikipediaapi
wiki = wikipediaapi.Wikipedia('PhyXit', 'en')
op = open('./tmp/papers.log', 'w', encoding='utf-8')


def getSummary(query):
    page = wiki.page(query)
    op.write(page.summary)
