# importing necessary libraries
import arxiv

def getList(query):
  output = open("papers.log", "w")

  search = arxiv.Search(query = query,max_results = 10,sort_by = arxiv.SortCriterion.SubmittedDate)
  count = 1

  for result in search.results():

    line = f"{count}. **{result.title}** : {result}\n"
    count += 1
    output.writelines(line)

def fetchPaper(ID):
  output = open("papers.log", "w")

  search = arxiv.Search(id_list=[ID])
  paper = next(search.results())
  
  authors = ""

  for author in paper.authors:
    authors += str(author) + ", "


  line = f"**Link**: {paper} \n**Title**: {paper.title} \n**Publishing Date**: {paper.published} \n**Author(s)**: {authors} \n**Abstract**: {paper.summary} \n**DOI**: {paper.doi} \n**Primary arxiv Category**: {paper.primary_category}\n**All arxiv Categories**: {paper.categories}\n**URL's associated with this paper**: {paper.links}"
  output.writelines(line)
