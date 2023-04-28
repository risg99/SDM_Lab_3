from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, RDF, XSD

def createTBOX():

	# Create a Graph
	graph = Graph()

	# Create many URIRefs in the same namespace, i.e. URIs with the same prefix
	LAB = Namespace("http://SDM_LAB3.org/")

	# Bind the lab namespace to a prefix for more readable output
	graph.bind('lab',LAB)

	# --------------------- 1) Paper Super Class --------------------------- #
	graph.add((LAB.Paper, RDF.type, RDFS.Class))
	graph.add((LAB.Paper, RDFS.label, Literal("Paper")))

	# SubClasses of Paper
	# 1.1) Poster
	graph.add((LAB.Poster, RDFS.subClassOf, LAB.Paper))
	graph.add((LAB.Poster, RDFS.label, Literal("Poster")))

	# 1.2) DemoPaper
	graph.add((LAB.DemoPaper, RDFS.subClassOf, LAB.Paper))
	graph.add((LAB.DemoPaper, RDFS.label, Literal("DemoPaper")))

	# 1.3) ShortPaper
	graph.add((LAB.ShortPaper, RDFS.subClassOf, LAB.Paper))
	graph.add((LAB.ShortPaper, RDFS.label, Literal("ShortPaper")))

	# 1.4) FullPaper
	graph.add((LAB.FullPaper, RDFS.subClassOf, LAB.Paper))
	graph.add((LAB.FullPaper, RDFS.label, Literal("FullPaper")))

	graph.add((LAB.relatedTo, RDFS.range, LAB.SubjectDomain))
	graph.add((LAB.relatedTo, RDFS.label, Literal("relatedTo")))

	graph.add((LAB.paperRelatedTo, RDF.type, RDF.Property))
	graph.add((LAB.paperRelatedTo, RDFS.domain, LAB.Paper))
	graph.add((LAB.paperRelatedTo, RDFS.range, LAB.SubjectDomain))
	graph.add((LAB.paperRelatedTo, RDFS.subPropertyOf, LAB.relatedTo))
	graph.add((LAB.paperRelatedTo, RDFS.label, Literal("paperRelatedTo")))

	# --------------------- 2) Person Super Class --------------------------- #
	graph.add((LAB.Person, RDF.type, RDFS.Class))
	graph.add((LAB.Person, RDFS.label, Literal("Person")))

	# Subclasses of Person
	# 2.1) Author
	graph.add((LAB.Author, RDFS.subClassOf, LAB.Person))
	graph.add((LAB.Author, RDFS.label, Literal("Author")))

	graph.add((LAB.writes, RDFS.domain, LAB.Author))
	graph.add((LAB.writes, RDFS.range, LAB.Paper))
	graph.add((LAB.writes, RDFS.label, Literal("writes")))

	# 2.2) Reviewer
	graph.add((LAB.Reviewer, RDFS.subClassOf, LAB.Person))
	graph.add((LAB.Reviewer, RDFS.label, Literal("Reviewer")))

	# 2.3) Handler: Editor or Chair
	graph.add((LAB.Handler, RDFS.subClassOf, LAB.Person))
	graph.add((LAB.Handler, RDFS.label, Literal("Handler")))

	graph.add((LAB.assigns, RDFS.domain, LAB.Handler))
	graph.add((LAB.assigns, RDFS.range, LAB.Reviewer))
	graph.add((LAB.assigns, RDFS.label, Literal("assigns")))

	graph.add((LAB.Editor, RDFS.subClassOf, LAB.Handler))
	graph.add((LAB.Editor, RDFS.label, Literal("Editor")))	

	graph.add((LAB.Chair, RDFS.subClassOf, LAB.Handler))
	graph.add((LAB.Chair, RDFS.label, Literal("Chair")))

	graph.add((LAB.handleJournal, RDFS.domain, LAB.Editor))
	graph.add((LAB.handleJournal, RDFS.range, LAB.Journal))
	graph.add((LAB.handleJournal, RDFS.label, Literal("handleJournal")))

	graph.add((LAB.handleConference, RDFS.domain, LAB.Chair))
	graph.add((LAB.handleConference, RDFS.range, LAB.Conference))
	graph.add((LAB.handleConference, RDFS.label, Literal("handleConference")))

	# Adding some extra properties
	graph.add((LAB.name, RDF.type, RDF.Property))
	graph.add((LAB.name, RDFS.domain, LAB.Person))
	graph.add((LAB.name, RDFS.range, XSD.string))
	graph.add((LAB.name, RDFS.label, Literal("name")))


	# --------------------- 3) Venue Super Class --------------------------- #
	graph.add((LAB.Venue, RDF.type, RDFS.Class))
	graph.add((LAB.Venue, RDFS.label, Literal("Venue")))

	graph.add((LAB.venueRelatedTo, RDF.type, RDF.Property))
	graph.add((LAB.venueRelatedTo, RDFS.domain, LAB.Venue))
	graph.add((LAB.venueRelatedTo, RDFS.range, LAB.SubjectDomain))
	graph.add((LAB.venueRelatedTo, RDFS.subPropertyOf, LAB.relatedTo))
	graph.add((LAB.venueRelatedTo, RDFS.label, Literal("venueRelatedTo")))

	# SubClasses of Venue
	# 3.1) Journal
	graph.add((LAB.Journal, RDFS.subClassOf, LAB.Venue))
	graph.add((LAB.Journal, RDFS.label, Literal("Journal")))
	
	# 3.2) Conference
	graph.add((LAB.Conference, RDFS.subClassOf, LAB.Venue))
	graph.add((LAB.Conference, RDFS.label, Literal("Conference")))

	# SubClasses of Conference
	# 3.2.1) Workshop
	graph.add((LAB.Workshop, RDFS.subClassOf, LAB.Conference))
	graph.add((LAB.Workshop, RDFS.label, Literal("Workshop")))

	# 3.2.2) ExpertGroup
	graph.add((LAB.ExpertGroup, RDFS.subClassOf, LAB.Conference))
	graph.add((LAB.ExpertGroup, RDFS.label, Literal("ExpertGroup")))

	# 3.2.3) Symposium
	graph.add((LAB.Symposium, RDFS.subClassOf, LAB.Conference))
	graph.add((LAB.Symposium, RDFS.label, Literal("Symposium")))

	# 3.2.4) RegularConference
	graph.add((LAB.RegularConference, RDFS.subClassOf, LAB.Conference))
	graph.add((LAB.RegularConference, RDFS.label, Literal("RegularConference")))

	graph.add((LAB.isIn, RDFS.domain, LAB.Conference))
	graph.add((LAB.isIn, RDFS.range, LAB.Proceedings))
	graph.add((LAB.isIn, RDFS.label, Literal("isIn")))

	graph.add((LAB.isOf, RDFS.domain, LAB.Journal))
	graph.add((LAB.isOf, RDFS.range, LAB.Volume))
	graph.add((LAB.isOf, RDFS.label, Literal("isOf")))
	
	graph.add((LAB.Proceedings, RDF.type, RDFS.Class))
	graph.add((LAB.Proceedings, RDFS.label, Literal("Proceedings")))

	graph.add((LAB.Volume, RDF.type, RDFS.Class))
	graph.add((LAB.Volume, RDFS.label, Literal("Volume")))

	# --------------------- 4) SubjectDomain Super Class --------------------------- #
	graph.add((LAB.SubjectDomain, RDF.type, RDFS.Class))
	graph.add((LAB.SubjectDomain, RDFS.label, Literal("SubjectDomain")))

	# --------------------- 5) Review related Classes --------------------------- #
	graph.add((LAB.ReviewText, RDF.type, RDFS.Class))
	graph.add((LAB.ReviewText, RDFS.label, Literal("ReviewText")))

	graph.add((LAB.reviewed, RDFS.domain, LAB.Reviewer))
	graph.add((LAB.reviewed, RDFS.range, LAB.ReviewText))
	graph.add((LAB.reviewed, RDFS.label, Literal("reviewed")))

	graph.add((LAB.isReviewOf, RDFS.domain, LAB.ReviewText))
	graph.add((LAB.isReviewOf, RDFS.range, LAB.SubmittedPaper))
	graph.add((LAB.isReviewOf, RDFS.label, Literal("isReviewOf")))

	# some other semantics
	graph.add((LAB.comment, RDFS.domain, LAB.ReviewText))
	graph.add((LAB.comment, RDFS.range, XSD.string))
	graph.add((LAB.comment, RDFS.label, Literal("comment")))

	graph.add((LAB.decision, RDFS.domain, LAB.ReviewText))
	graph.add((LAB.decision, RDFS.range, XSD.boolean))
	graph.add((LAB.decision, RDFS.label, Literal("decision")))

	# --------------------- 6) SubmittedPaper related Classes --------------------------- #	
	graph.add((LAB.SubmittedPaper, RDF.type, RDFS.Class))
	graph.add((LAB.SubmittedPaper, RDFS.label, Literal("SubmittedPaper")))

	graph.add((LAB.submitted, RDFS.domain, LAB.Paper))
	graph.add((LAB.submitted, RDFS.range, LAB.SubmittedPaper))
	graph.add((LAB.submitted, RDFS.label, Literal("submitted")))

	graph.add((LAB.isSubmittedTo, RDFS.domain, LAB.SubmittedPaper))
	graph.add((LAB.isSubmittedTo, RDFS.range, LAB.Venue))
	graph.add((LAB.isSubmittedTo, RDFS.label, Literal("isSubmittedTo")))

	graph.add((LAB.isPublishedInConference, RDFS.domain, LAB.SubmittedPaper))
	graph.add((LAB.isPublishedInConference, RDFS.range, LAB.Conference))
	graph.add((LAB.isPublishedInConference, RDFS.label, Literal("isPublishedInConference")))

	graph.add((LAB.isPublishedInJournal, RDFS.domain, LAB.SubmittedPaper))
	graph.add((LAB.isPublishedInJournal, RDFS.range, LAB.Journal))
	graph.add((LAB.isPublishedInJournal, RDFS.label, Literal("isPublishedInJournal")))


	# Some other properties
	graph.add((LAB.title, RDF.type, RDF.Property))
	graph.add((LAB.title, RDFS.label, Literal("title")))
	graph.add((LAB.title, RDFS.range, XSD.string))

	# SubProperties of title - paperTitle, conferenceTitle, journalTitle
	graph.add((LAB.paperTitle, RDF.type, RDF.Property))
	graph.add((LAB.paperTitle, RDFS.domain, LAB.Paper))
	graph.add((LAB.paperTitle, RDFS.range, XSD.string))
	graph.add((LAB.paperTitle, RDFS.subPropertyOf, LAB.title))
	graph.add((LAB.paperTitle, RDFS.label, Literal("paperTitle")))

	graph.add((LAB.conferenceTitle, RDF.type, RDF.Property))
	graph.add((LAB.conferenceTitle, RDFS.domain, LAB.Conference))
	graph.add((LAB.conferenceTitle, RDFS.range, XSD.string))
	graph.add((LAB.conferenceTitle, RDFS.subPropertyOf, LAB.title))
	graph.add((LAB.conferenceTitle, RDFS.label, Literal("conferenceTitle")))

	graph.add((LAB.journalTitle, RDF.type, RDF.Property))
	graph.add((LAB.journalTitle, RDFS.domain, LAB.Journal))
	graph.add((LAB.journalTitle, RDFS.range, XSD.string))
	graph.add((LAB.journalTitle, RDFS.subPropertyOf, LAB.title))
	graph.add((LAB.journalTitle, RDFS.label, Literal("journalTitle")))

	return graph

graph = createTBOX()

# Print out the entire Graph in the RDF Turtle format
print(graph.serialize(format="turtle"))

