import sys
import warnings
import time
import logging
import json
import re

from load_bitstomach import read


#from asyncore import read

import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper
import pandas as pd
from rdflib import Graph, Literal, Namespace, URIRef ,BNode
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD 
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper
import numpy as np 

class BitStomach():
    def __init__(self, spek: str = "{}",performance_data: pd.DataFrame=()):
        self.spek = spek
        self.performance_data = performance_data
        self.graph_read=read(self.spek)
        b_node =URIRef("http://example.com/app#display-lab")
        p = URIRef("http://example.com/slowmo#IsAboutPerformer")
        o =URIRef("p1")
        self.graph_read.add((b_node, p, o,))
        s1=o
        p1=RDF.type
        o1=Literal("http://purl.obolibrary.org/obo/psdo_0000085")
        self.graph_read.add((s1, p1, o1))
        s2=URIRef("p1")
        
        print(self.graph_read.serialize(format='json-ld', indent=4))

        #df = to_dataframe(self.graph_read) 
        #df.to_csv("input_csv.csv")
