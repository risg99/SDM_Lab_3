import csv
import rdflib
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDFS, RDF, XSD, FOAF
import B1_TBOXCreation
from B1_TBOXCreation import *
from B1_TBOXCreation import LAB


g = Graph()
graph.bind("foaf", FOAF)


# for row in reader:
#     subject = row['subject']
#     for predicate, object in row.items():
#         if predicate != 'subject':
#             g.add((URIRef(subject), URIRef("http://example.com/property/" + predicate), Literal(object)))
#

# -----------------------------------------------------------------------



# RDF namespaces
SCHEMA = rdflib.Namespace("http://schema.org/")
MY_ONTOLOGY = rdflib.Namespace("http://example.com/ontology#")

graph = rdflib.Graph()

# 0,pId
# 1,paperUrlId
# 2,conferenceJournalId
# 3,conferenceJournalTitle
# 4,pTitle
# 5,abstract
# 6,pType
with open('data/papers.csv') as papers:
    reader = csv.reader(papers)
    next(reader)
    for row in reader:
        id = LAB[row[0]]
        title = Literal(row[4], datatype=XSD.string)
        abstract = Literal(row[5], datatype=XSD.string)
        paperType = Literal(row[6], datatype=XSD.string)
    if id is not None:
        graph.add((id, RDF.type, B1_TBOXCreation.LAB.Poster))
    if title is not None:
        graph.add((id, B1_TBOXCreation.LAB.paperTitle, title))
    if abstract is not None:
        graph.add((id, B1_TBOXCreation.LAB.paperAbstract, abstract))

print(g.serialize())
g.serialize(destination="data/abox_tbox_connection.ttl", format="ttl")

# Process each CSV file
# csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
# for csv_file in csv_files:
#     with open(csv_file, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)
#         for row in reader:
#             id = LAB[row[0]]
#             subject = row[0]
#             predicate = row[1]
#             object = row[2]
#
#             # Map CSV columns to RDF terms
#             subject_uri = MY_ONTOLOGY[subject]
#             predicate_uri = SCHEMA[predicate]
#             object_literal = rdflib.Literal(object)
#
#             # Create RDF triple and add it to the graph
#             graph.add((subject_uri, predicate_uri, object_literal))


