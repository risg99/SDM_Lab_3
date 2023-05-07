# Semantic scholar data
import json
from semanticscholar import SemanticScholar

s2_api_key = '1WBrQVQGeo6ZZI2eJmWMk2eFnmgl8W1T7VEDvRyQ'
sch = SemanticScholar(api_key=s2_api_key)

ds_papers = sch.search_paper('data science', limit=100)
se_papers = sch.search_paper('software engineering', limit=100)
bi_papers = sch.search_paper('bioinformatics', limit=100)
graph_papers = sch.search_paper('graph theory', limit=100)
db_papers = sch.search_paper('database', limit=100)

### Dump dataset


dataset = [ds_papers, se_papers, bi_papers, graph_papers, db_papers]

result = []
for data in dataset:
    
    length = 1
    for res in data:
        if length > 500:
            break
            
        length += 1
        result.append(res)

### Dump dataset as json
with open('../data/dataset.json', 'w+') as f:
    json.dump(result, f)