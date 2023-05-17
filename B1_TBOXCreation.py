from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDFS, RDF, XSD

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
graph.add((LAB.Poster, RDF.type, RDFS.Class))
graph.add((LAB.Poster, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.Poster, RDFS.label, Literal("Poster")))

# 1.2) DemoPaper
graph.add((LAB.DemoPaper, RDF.type, RDFS.Class))
graph.add((LAB.DemoPaper, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.DemoPaper, RDFS.label, Literal("DemoPaper")))

# 1.3) ShortPaper
graph.add((LAB.ShortPaper, RDF.type, RDFS.Class))
graph.add((LAB.ShortPaper, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.ShortPaper, RDFS.label, Literal("ShortPaper")))

# 1.4) FullPaper
graph.add((LAB.FullPaper, RDF.type, RDFS.Class))
graph.add((LAB.FullPaper, RDFS.subClassOf, LAB.Paper))
graph.add((LAB.FullPaper, RDFS.label, Literal("FullPaper")))

graph.add((LAB.paperRelatedTo, RDF.type, RDF.Property))
graph.add((LAB.paperRelatedTo, RDFS.domain, LAB.Paper))
graph.add((LAB.paperRelatedTo, RDFS.range, LAB.SubjectDomain))
graph.add((LAB.paperRelatedTo, RDFS.label, Literal("paperRelatedTo")))

# Adding some additional attributes for Paper Concept
# 1) paperTitle
graph.add((LAB.paperTitle, RDF.type, RDF.Property))
graph.add((LAB.paperTitle, RDFS.domain, LAB.Paper))
graph.add((LAB.paperTitle, RDFS.range, XSD.string))
graph.add((LAB.paperTitle, RDFS.label, Literal("paperTitle")))

# 2) paperAbstract
graph.add((LAB.paperAbstract, RDF.type, RDF.Property))
graph.add((LAB.paperAbstract, RDFS.domain, LAB.Paper))
graph.add((LAB.paperAbstract, RDFS.range, XSD.string))
graph.add((LAB.paperAbstract, RDFS.label, Literal("paperAbstract")))

# --------------------- 2) Person Super Class --------------------------- #
graph.add((LAB.Person, RDF.type, RDFS.Class))
graph.add((LAB.Person, RDFS.label, Literal("Person")))

# Subclasses of Person
# 2.1) Author
graph.add((LAB.Author, RDF.type, RDFS.Class))
graph.add((LAB.Author, RDFS.subClassOf, LAB.Person))
graph.add((LAB.Author, RDFS.label, Literal("Author")))

# Adding some extra properties for Author Concept
graph.add((LAB.authorName, RDF.type, RDF.Property))
graph.add((LAB.authorName, RDFS.domain, LAB.Author))
graph.add((LAB.authorName, RDFS.range, XSD.string))
graph.add((LAB.authorName, RDFS.label, Literal("authorName")))

graph.add((LAB.writes, RDF.type, RDF.Property))
graph.add((LAB.writes, RDFS.domain, LAB.Author))
graph.add((LAB.writes, RDFS.range, LAB.Paper))
graph.add((LAB.writes, RDFS.label, Literal("writes")))

# 2.2) Reviewer
graph.add((LAB.Reviewer, RDF.type, RDFS.Class))
graph.add((LAB.Reviewer, RDFS.subClassOf, LAB.Person))
graph.add((LAB.Reviewer, RDFS.label, Literal("Reviewer")))

# 2.3) Handler: Editor or Chair
graph.add((LAB.Handler, RDF.type, RDFS.Class))
graph.add((LAB.Handler, RDFS.subClassOf, LAB.Person))
graph.add((LAB.Handler, RDFS.label, Literal("Handler")))

graph.add((LAB.assigns, RDF.type, RDF.Property))
graph.add((LAB.assigns, RDFS.domain, LAB.Handler))
graph.add((LAB.assigns, RDFS.range, LAB.Reviewer))
graph.add((LAB.assigns, RDFS.label, Literal("assigns")))

graph.add((LAB.Editor, RDF.type, RDFS.Class))
graph.add((LAB.Editor, RDFS.subClassOf, LAB.Handler))
graph.add((LAB.Editor, RDFS.label, Literal("Editor")))	

graph.add((LAB.Chair, RDF.type, RDFS.Class))
graph.add((LAB.Chair, RDFS.subClassOf, LAB.Handler))
graph.add((LAB.Chair, RDFS.label, Literal("Chair")))

graph.add((LAB.handleJournal, RDF.type, RDF.Property))
graph.add((LAB.handleJournal, RDFS.domain, LAB.Editor))
graph.add((LAB.handleJournal, RDFS.range, LAB.Journal))
graph.add((LAB.handleJournal, RDFS.label, Literal("handleJournal")))

graph.add((LAB.handleConference, RDF.type, RDF.Property))	
graph.add((LAB.handleConference, RDFS.domain, LAB.Chair))
graph.add((LAB.handleConference, RDFS.range, LAB.Conference))
graph.add((LAB.handleConference, RDFS.label, Literal("handleConference")))


# --------------------- 3) Venue Super Class --------------------------- #
graph.add((LAB.Venue, RDF.type, RDFS.Class))
graph.add((LAB.Venue, RDFS.label, Literal("Venue")))

# SubClasses of Venue
# 3.1) Journal
graph.add((LAB.Journal, RDF.type, RDFS.Class))
graph.add((LAB.Journal, RDFS.subClassOf, LAB.Venue))
graph.add((LAB.Journal, RDFS.label, Literal("Journal")))

# Adding properties for journal
graph.add((LAB.journalTitle, RDF.type, RDF.Property))
graph.add((LAB.journalTitle, RDFS.domain, LAB.Journal))
graph.add((LAB.journalTitle, RDFS.range, XSD.string))
graph.add((LAB.journalTitle, RDFS.label, Literal("journalTitle")))

# 3.2) Conference
graph.add((LAB.Conference, RDF.type, RDFS.Class))
graph.add((LAB.Conference, RDFS.subClassOf, LAB.Venue))
graph.add((LAB.Conference, RDFS.label, Literal("Conference")))

# Adding properties for conference
graph.add((LAB.conferenceTitle, RDF.type, RDF.Property))
graph.add((LAB.conferenceTitle, RDFS.domain, LAB.Conference))
graph.add((LAB.conferenceTitle, RDFS.range, XSD.string))
graph.add((LAB.conferenceTitle, RDFS.label, Literal("conferenceTitle")))

# SubClasses of Conference
# 3.2.1) Workshop
graph.add((LAB.Workshop, RDF.type, RDFS.Class))
graph.add((LAB.Workshop, RDFS.subClassOf, LAB.Conference))
graph.add((LAB.Workshop, RDFS.label, Literal("Workshop")))

# 3.2.2) ExpertGroup
graph.add((LAB.ExpertGroup, RDF.type, RDFS.Class))
graph.add((LAB.ExpertGroup, RDFS.subClassOf, LAB.Conference))
graph.add((LAB.ExpertGroup, RDFS.label, Literal("ExpertGroup")))

# 3.2.3) Symposium
graph.add((LAB.Symposium, RDF.type, RDFS.Class))
graph.add((LAB.Symposium, RDFS.subClassOf, LAB.Conference))
graph.add((LAB.Symposium, RDFS.label, Literal("Symposium")))

# 3.2.4) RegularConference
graph.add((LAB.RegularConference, RDF.type, RDFS.Class))
graph.add((LAB.RegularConference, RDFS.subClassOf, LAB.Conference))
graph.add((LAB.RegularConference, RDFS.label, Literal("RegularConference")))

# Since properties cannot have same name, conferences are linked to proceedings using :isIn
# while journals are linked to volume using :isOf 
graph.add((LAB.isIn, RDF.type, RDF.Property))
graph.add((LAB.isIn, RDFS.domain, LAB.Conference))
graph.add((LAB.isIn, RDFS.range, LAB.Proceedings))
graph.add((LAB.isIn, RDFS.label, Literal("isIn")))

graph.add((LAB.isOf, RDF.type, RDF.Property))
graph.add((LAB.isOf, RDFS.domain, LAB.Journal))
graph.add((LAB.isOf, RDFS.range, LAB.Volume))
graph.add((LAB.isOf, RDFS.label, Literal("isOf")))

graph.add((LAB.Proceedings, RDF.type, RDFS.Class))
graph.add((LAB.Proceedings, RDFS.label, Literal("Proceedings")))

# Adding properties for proceedings
graph.add((LAB.proceedingName, RDF.type, RDF.Property))
graph.add((LAB.proceedingName, RDFS.domain, LAB.Proceedings))
graph.add((LAB.proceedingName, RDFS.range, XSD.string))
graph.add((LAB.proceedingName, RDFS.label, Literal("proceedingName")))	

graph.add((LAB.proceedingYear, RDF.type, RDF.Property))
graph.add((LAB.proceedingYear, RDFS.domain, LAB.Proceedings))
graph.add((LAB.proceedingYear, RDFS.range, XSD.int))
graph.add((LAB.proceedingYear, RDFS.label, Literal("proceedingYear")))

graph.add((LAB.proceedingRelatedTo, RDF.type, RDF.Property))
graph.add((LAB.proceedingRelatedTo, RDFS.domain, LAB.Proceedings))
graph.add((LAB.proceedingRelatedTo, RDFS.range, LAB.SubjectDomain))
graph.add((LAB.proceedingRelatedTo, RDFS.label, Literal("proceedingRelatedTo")))

graph.add((LAB.Volume, RDF.type, RDFS.Class))
graph.add((LAB.Volume, RDFS.label, Literal("Volume")))

# Adding properties for volume
graph.add((LAB.volumeName, RDF.type, RDF.Property))
graph.add((LAB.volumeName, RDFS.domain, LAB.Volume))
graph.add((LAB.volumeName, RDFS.range, XSD.string))
graph.add((LAB.volumeName, RDFS.label, Literal("volumeName")))	

graph.add((LAB.volumeYear, RDF.type, RDF.Property))
graph.add((LAB.volumeYear, RDFS.domain, LAB.Volume))
graph.add((LAB.volumeYear, RDFS.range, XSD.int))
graph.add((LAB.volumeYear, RDFS.label, Literal("volumeYear")))

graph.add((LAB.volumeRelatedTo, RDF.type, RDF.Property))
graph.add((LAB.volumeRelatedTo, RDFS.domain, LAB.Volume))
graph.add((LAB.volumeRelatedTo, RDFS.range, LAB.SubjectDomain))
graph.add((LAB.volumeRelatedTo, RDFS.label, Literal("volumeRelatedTo")))

# --------------------- 4) SubjectDomain Super Class --------------------------- #
graph.add((LAB.SubjectDomain, RDF.type, RDFS.Class))
graph.add((LAB.SubjectDomain, RDFS.label, Literal("SubjectDomain")))

# Adding property for SubjectDomain Concept
graph.add((LAB.keywords, RDF.type, RDF.Property))
graph.add((LAB.keywords, RDFS.domain, LAB.SubjectDomain))
graph.add((LAB.keywords, RDFS.range, XSD.string))
graph.add((LAB.keywords, RDFS.label, Literal("keywords")))

# --------------------- 5) Review related Classes --------------------------- #
graph.add((LAB.ReviewText, RDF.type, RDFS.Class))
graph.add((LAB.ReviewText, RDFS.label, Literal("ReviewText")))

graph.add((LAB.reviewed, RDF.type, RDF.Property))
graph.add((LAB.reviewed, RDFS.domain, LAB.Reviewer))
graph.add((LAB.reviewed, RDFS.range, LAB.ReviewText))
graph.add((LAB.reviewed, RDFS.label, Literal("reviewed")))

graph.add((LAB.isReviewOf, RDF.type, RDF.Property))
graph.add((LAB.isReviewOf, RDFS.domain, LAB.ReviewText))
graph.add((LAB.isReviewOf, RDFS.range, LAB.SubmittedPaper))
graph.add((LAB.isReviewOf, RDFS.label, Literal("isReviewOf")))

# Adding some extra properties for Review Concept
# 1) comment
graph.add((LAB.comment, RDF.type, RDF.Property))
graph.add((LAB.comment, RDFS.domain, LAB.ReviewText))
graph.add((LAB.comment, RDFS.range, XSD.string))
graph.add((LAB.comment, RDFS.label, Literal("comment")))

# 2) decision
graph.add((LAB.decision, RDF.type, RDF.Property))
graph.add((LAB.decision, RDFS.domain, LAB.ReviewText))
graph.add((LAB.decision, RDFS.range, XSD.boolean))
graph.add((LAB.decision, RDFS.label, Literal("decision")))

# --------------------- 6) SubmittedPaper related Classes --------------------------- #	
graph.add((LAB.SubmittedPaper, RDF.type, RDFS.Class))
graph.add((LAB.SubmittedPaper, RDFS.label, Literal("SubmittedPaper")))

graph.add((LAB.submitted, RDF.type, RDF.Property))
graph.add((LAB.submitted, RDFS.domain, LAB.Paper))
graph.add((LAB.submitted, RDFS.range, LAB.SubmittedPaper))
graph.add((LAB.submitted, RDFS.label, Literal("submitted")))

graph.add((LAB.isSubmittedTo, RDF.type, RDF.Property))
graph.add((LAB.isSubmittedTo, RDFS.domain, LAB.SubmittedPaper))
graph.add((LAB.isSubmittedTo, RDFS.range, LAB.Venue))
graph.add((LAB.isSubmittedTo, RDFS.label, Literal("isSubmittedTo")))

# --------------------- 7) FinalPaper related Classes --------------------------- #	
graph.add((LAB.FinalPaper, RDF.type, RDFS.Class))
graph.add((LAB.FinalPaper, RDFS.label, Literal("FinalPaper")))

graph.add((LAB.paperAcceptanceDate, RDF.type, RDF.Property))
graph.add((LAB.paperAcceptanceDate, RDFS.domain, LAB.FinalPaper))
graph.add((LAB.paperAcceptanceDate, RDFS.range, XSD.date))
graph.add((LAB.paperAcceptanceDate, RDFS.label, Literal("paperAcceptanceDate")))

graph.add((LAB.isAs, RDF.type, RDF.Property))
graph.add((LAB.isAs, RDFS.domain, LAB.SubmittedPaper))
graph.add((LAB.isAs, RDFS.range, LAB.FinalPaper))
graph.add((LAB.isAs, RDFS.label, Literal("isAs")))

graph.add((LAB.isPublishedInConference, RDF.type, RDF.Property))
graph.add((LAB.isPublishedInConference, RDFS.domain, LAB.FinalPaper))
graph.add((LAB.isPublishedInConference, RDFS.range, LAB.Proceedings))
graph.add((LAB.isPublishedInConference, RDFS.label, Literal("isPublishedInConference")))

graph.add((LAB.isPublishedInJournal, RDF.type, RDF.Property))
graph.add((LAB.isPublishedInJournal, RDFS.domain, LAB.FinalPaper))
graph.add((LAB.isPublishedInJournal, RDFS.range, LAB.Volume))
graph.add((LAB.isPublishedInJournal, RDFS.label, Literal("isPublishedInJournal")))


# Print out the entire Graph in the RDF Turtle format
print(graph.serialize('data/tbox.ttl',format="ttl"))