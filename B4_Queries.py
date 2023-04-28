from rdflib import Graph, URIRef
from B1_TBOXCreation import createTBOX

graph = createTBOX()

def query1(graph):

	author = URIRef("http://SDM_LAB3.org/Author")
	authorName = URIRef("http://SDM_LAB3.org/Author/name")

	sparql_query = """
		SELECT ?authorName
		WHERE
		{
		    ?author rdf:type ?o .
		    ?author ?x ?authorName
		}
	"""

	results = graph.query(sparql_query, initBindings={"o" : author, "x" : authorName})
	return [str(result[0]) for result in results]

def query2(graph):

	author = URIRef("http://SDM_LAB3.org/Author")

	sparql_query = """
		SELECT ?propertyName
		WHERE
		{
		    ?propertyName rdfs:domain ?o .
		}
	"""

	results = graph.query(sparql_query, initBindings={"o" : author})
	return [str(result[0]) for result in results]

def query3(graph):

	conference = URIRef("http://SDM_LAB3.org/Conference")
	journal = URIRef("http://SDM_LAB3.org/Journal")

	sparql_query = """
		SELECT ?propertyName
		WHERE 
		{
			{?propertyName rdfs:domain ?c}
			UNION
			{?propertyName rdfs:domain ?j}
		}
	"""

	results = graph.query(sparql_query, initBindings={"c" : conference,"j" : journal})
	return [str(result[0]) for result in results]

# TODO
def query4(graph):
	return []

print(query1(graph))
print(query2(graph))
print(query3(graph))
print(query4(graph))
