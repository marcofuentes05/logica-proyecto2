from neo4j import GraphDatabase
uri = "neo4j://localhost:7687"
user = "neo4j"
password = "password"
def pupulate():
  driver = GraphDatabase.driver(uri, auth=(user, password ))
