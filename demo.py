# -*- coding: utf-8 -*-
import os
import sys
from pyshacl import validate
from rdflib import Graph


idsa_code_url = "https://w3id.org/idsa/code/"

if len(sys.argv) < 2:
    print("Please provide a input data file!\nUsage: python demo.py /path/to/dataFile.ttl")
    exit(0)

data_path = os.path.abspath(sys.argv[1])

if not os.path.exists(data_path):
    print("Validtor can't find the specified file. Please check the path and try again.")
    exit(0)

data_format_mapping = {
    "ttl": "turtle",
    "xml": "xml",
    "jsonld": "json-ld",
    "nt": "nt",
    "n3": "n3"
}

file_ext = data_path.split(".")[-1]
data_format = data_format_mapping.get(file_ext, "")

if not data_format:
    print("Please provide an input file with one of the following file extentions:")
    print([key for key in data_format_mapping.keys()])
    exit(0)   

data = ""
with open(data_path, 'r') as df:
    data = df.read()

shape_dir = os.path.join(os.getcwd(), "templates")
if not os.path.exists(shape_dir):
    print("Validtor can't find the SHACL shape directory. Please check if the 'templates' directory containing the shapes is in your current working directory.")
    exit(0)


shape_files = []
for dirpath, subdirs, files in os.walk(shape_dir):
    for x in files:
        if "TemplateShape" in x:
            shape_files.append(os.path.join(dirpath, x))

shapes = Graph()

for shape_file in shape_files:
    shapes.parse(shape_file, format="turtle")


conforms, v_graph, v_text = validate(data, shacl_graph=shapes, data_graph_format=data_format, shacl_graph_format='turtle',
                                    inference='rdfs', serialize_report_graph=True, ont_graph=idsa_code_url)
print(v_text.replace("\nConstraint Violation", "\n\nConstraint Violation"))
