# SDM_Lab_3
## Knowledge Graphs lab for the "Semantic Data Management" Course at Polytechnic University of Catalonia.
Packages needed are mentioned in the requirements.txt file.
Initial json file with data is downloaded from semanticscholar.

1. Run the B1_TBOXCreation.py file to define the schema of the graph.<br>
Result is saved to "data/tbox.ttl" in the turtle format.
2. Run the B2_ABOXCreation.ipynb to upload data in the graph.<br>
Results can be found in "data/abox.ttl".
3. Run the B3_TBOX_ABOX_Connection.ipynb to define the types of instances.<br>
Results is saved to "data/tbox_abox_connection.ttl".<br>

The graph can be explored with GraphDB. Create a new repository, choose RDF-plus (Optimized) ruleset. Import 3 .ttl files.
Explore the "Class hierarchy" and "Class relationships" tabs.
