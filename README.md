# Information Model - Contract Validation Demo
A short demonstration of how to validate RDF contracts according to the Information Model of the International Data Spaces Association using Python and SHACL.

## What it does
This tool demonstrates the validation of contracts and usage policies in Python 3. To do so, it heavily relies on the Python modules `pySHACL` and `rdflib`. For a given RDF input serialized in turtle, xml, json-ld, nt or n3 the validation checks, if the input conforms to the SHACL shapes defined by the `International Data Space Association - InformationModel`.

## How to use
### Installation:
- Download this repository.
- Install the required python packages with PIP installer. (`pip install -r requirements.txt`)
- Download the [IDSA Information Model](https://github.com/International-Data-Spaces-Association/InformationModel "Github: International-Data-Spaces-Association / InformationModel") repository. 
- Copy the folder `examples/contracts-and-usage-policy/templates` into this directory, to provide the validator the necessary shape information. ([Link to folder online](https://github.com/International-Data-Spaces-Association/InformationModel/tree/develop/examples/contracts-and-usage-policy/templates))
The resulting folder structure should look like this:
```
IM-ContractValidatorDemo
│───.gitignore
│───demo.py 
│───README.md
│
└───examples
│   │───valid_agreement.ttl
│   │───invalid_agreement.ttl
|   |───...
│   
└───templates
    │───<Classname>Templates
    |   |───<Classname>_TEMPLATE.jsonld
    |   |───<Classname>_TEMPLATE.ttl
    |   |───<Classname>TemplateShape.ttl
    │───...
```

### Command Line Usage
```python demo.py /path/to/dataFile.ttl```

As output the `result_text` return value of pySHACLs validate function is printed to the console. This is the textual representation of the SHACL [Validation Report](https://www.w3.org/TR/shacl/#validation-report).

Example:

```
$ python demo.py examples/invalid_offer.jsonld
Validation Report
Conforms: False
Results (3):

Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
        Severity: sh:Violation
        Source Shape: shapes:ConstraintTemplate-rightOperandPropertyShape
        Focus Node: [ <http://www.w3.org/ns/odrl/2/leftOperand> idsc:POLICY_EVALUATION_TIME ; <http://www.w3.org/ns/odrl/2/operator> idsc:AFTER ; ids:leftOperand idsc:POLICY_EVALUATION_TIME ; ids:operator idsc:AFTER ; rdf:type <http://www.w3.org/ns/odrl/2/Constraint>, ids:AbstractConstraint, ids:Constraint, rdfs:Resource ]
        Result Path: [ sh:alternativePath ( ids:rightOperand ids:rightOperandReference ) ]
        Message: <https://raw.githubusercontent.com/International-Data-Spaces-Association/InformationModel/master/examples/contract-and-usage-policy/templates/ConstraintTemplates/ConstraintTemplateShape.ttl> (ConstraintTemplate-rightOperandPropertyShape): In a _:Constraint one of the properties a) ids:rightOperand or b) ids:rightOperandReference must point to an adequate value according to the ids:LeftOperand used in this constraint.

Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
        Severity: sh:Violation
        Source Shape: shapes1:ObligationTemplate-assigneePropertyShape
        Focus Node: [ <http://www.w3.org/ns/odrl/2/action> idsc:LOG ; <http://www.w3.org/ns/odrl/2/assigner> <https://iais.fraunhofer.de/> ; ids:action idsc:LOG ; ids:assigner <https://iais.fraunhofer.de/> ; rdf:type <http://www.w3.org/ns/odrl/2/Duty>, <http://www.w3.org/ns/odrl/2/Rule>, ids:Described, ids:Duty, ids:Rule, ids:UsageControlObject, rdfs:Resource ]
        Result Path: ids:assignee
        Message: <https://raw.githubusercontent.com/International-Data-Spaces-Association/InformationModel/master/examples/contract-and-usage-policy/templates/ObligationTemplates/ObligationTemplateShapes.ttl> (ObligationTemplate-assigneePropertyShape): In a _:Duty for a _:ContractAgreement the ids:assignee property must point to exactly one participant. This can be a) an IRI or b) an ids:Participant. In a _:Duty for a _:ContractOffer or _:ContractRequest the ids:assignee property may still be missing.

Constraint Violation in NodeConstraintComponent (http://www.w3.org/ns/shacl#NodeConstraintComponent):
        Severity: sh:Violation
        Source Shape: shapes:OfferTemplateShape
        Focus Node: <https://mdmconnector.ids.isst.fraunhofer.de/ResourceCatalog/e75d21a7/offer1/>
        Value Node: <https://mdmconnector.ids.isst.fraunhofer.de/ResourceCatalog/e75d21a7/offer1/>
        Message: <https://raw.githubusercontent.com/International-Data-Spaces-Association/InformationModel/master/examples/contract-and-usage-policy/templates/OfferTemplateShape.ttl> (HasProviderOrConsumerNodeShape): In a _:ContractOffer a) the ids:provider property must point to one participant or b) the ids:consumer property must point to one participant  or c) the ids:provider and the ids:consumer must point to one participant. This can in any case be a) an IRI or b) an ids:Participant.
```
