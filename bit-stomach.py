import json
import sys
import warnings
import time
import logging
import json
import pandas as pd

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.collection import Collection
from rdflib.namespace import FOAF, RDF, RDFS, SKOS, XSD
from rdflib.serializer import Serializer
from rdfpandas.graph import to_dataframe
from SPARQLWrapper import XML, SPARQLWrapper
import bit_stomach

spek=sys.argv[1]
performance_df=pd.read_csv(sys.argv[2])
bs = bit_stomach.BitStomach(spek,performance_df)
