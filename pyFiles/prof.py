from scholarly import scholarly
import urllib.request

def knowProf(query):
    search_query = scholarly.search_author(query)
    author = next(search_query)
    data = scholarly.fill(author, sections=[])
    fields = ['url_picture', 'name', 'affiliation', 'interests', 'homepage']

    urllib.request.urlretrieve(data[fields[0]], "prof.jpg")

    with open("prof.log", "w") as output:
        for i in range(1, len(fields)):
            if fields[i] in data.keys():
                line = f"{fields[i]}: {data[fields[i]]}\n"
            

            output.writelines(line)

def researchField(keyword):
    search_query = scholarly.search_keyword(keyword)

    # for i in range(10):
    data = scholarly.pprint(next(search_query))
    print(data)
        # print()
        

researchField("Quantum Cosmology")

