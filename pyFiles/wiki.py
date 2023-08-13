import wikipediaapi
wiki = wikipediaapi.Wikipedia('PhyXit', 'en')


def getSummary(query):
    op = open('./tmp/papers.log', 'w', encoding='utf-8')

    page = wiki.page(query)
    op.write(page.summary)
