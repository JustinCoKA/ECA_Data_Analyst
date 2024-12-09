import json
from faker import Faker
from lib.common_health import generate_medicare_number, generate_ihi_number, generate_dva_number

fake = Faker('en_AU')


def generate_referral():
    return {
        "resourceType": "ServiceRequest",
        "id": "AUSBIZBOOTCAMP-REFERRAL-677",
        "contained": [
            {
                "resourceType": "PractitionerRole",
                "id": fake.random_number(digits=6, fix_len=True),
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "UPIN"
                                }
                            ],
                            "text": "Medicare Provider Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/medicare-provider-number",
                        "value": fake.random_number(digits=6, fix_len=True)
                    }
                ],
                "practitioner": {
                    "reference": f"#{fake.uuid4()}",
                    "type": "Practitioner"
                },
                "organization": {
                    "reference": f"#{fake.uuid4()}",
                    "type": "Organization"
                }
            },
            {
                "resourceType": "Practitioner",
                "id": f"#{fake.uuid4()}",
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://hl7.org.au/fhir/v2/0203",
                                    "code": "NPI",
                                    "display": "National provider identifier"
                                }
                            ],
                            "text": "HPI-I"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/hpii/1.0",
                        "value": fake.random_number(digits=16)
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": fake.last_name(),
                        "given": [
                            fake.first_name()
                        ]
                    }
                ]
            },
            {
                "resourceType": "Organization",
                "id": f"{fake.uuid4()}",
                "meta": {
                    "profile": [
                        "http://hl7.org.au/fhir/StructureDefinition/au-organization"
                    ]
                },
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "NOI",
                                    "display": "National Organisation Identifier"
                                }
                            ],
                            "text": "HPI-O"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/hpio/1.0",
                        "value": fake.random_number(digits=6, fix_len=True)
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://hl7.org.au/fhir/v2/0203",
                                    "code": "RI",
                                    "display": "Resource identifier"
                                }
                            ],
                            "text": "EDI"
                        },
                        "system": "https://www.healthlink.net/edi-address",
                        "value": fake.pystr(min_chars=6, max_chars=8)
                    }
                ],
                "active": True,
                "name": fake.company(),
                "telecom": [
                    {
                        "system": "phone",
                        "value": fake.phone_number(),
                        "use": "work"
                    },
                    {
                        "system": "email",
                        "value": fake.company_email(),
                        "use": "work"
                    }
                ],
                "address": [
                    {
                        "use": "work",
                        "type": "physical",
                        "line": [
                            fake.street_address()
                        ],
                        "city": fake.city(),
                        "state": fake.state_abbr(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    }
                ]
            },
            {
                "resourceType": "Patient",
                "id": f"{fake.uuid4()}",
                "meta": {
                    "profile": [
                        "http://hl7.org.au/fhir/StructureDefinition/au-patient"
                    ]
                },
                "extension": [
                    {
                        "url": "http://hl7.org.au/fhir/StructureDefinition/indigenous-status",
                        "valueCoding": {
                            "system": "https://healthterminologies.gov.au/fhir/CodeSystem/australian-indigenous-status-1",
                            "code": "9",
                            "display": "Not stated/inadequately described"
                        }
                    }
                ],
                "identifier": [
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "NI",
                                    "display": "National unique individual identifier"
                                }
                            ],
                            "text": "IHI"
                        },
                        "system": "http://ns.electronichealth.net.au/id/hi/ihi/1.0",
                        "value": fake.random_number(digits=16)
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                                    "code": "MC",
                                    "display": "Patient's Medicare Number"
                                }
                            ],
                            "text": "Medicare Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/medicare-number",
                        "value": fake.random_number(digits=10)
                    },
                    {
                        "type": {
                            "coding": [
                                {
                                    "system": "http://terminology.hl7.org.au/CodeSystem/v2-0203",
                                    "code": "DVAU",
                                    "display": "DVA Number"
                                }
                            ],
                            "text": "DVA Number"
                        },
                        "system": "http://ns.electronichealth.net.au/id/dva",
                        "value": fake.pystr(min_chars=6, max_chars=8)
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": fake.last_name(),
                        "given": [fake.first_name(), fake.first_name()]
                    }
                ],
                "telecom": [
                    {"system": "phone", 
                     "value": fake.phone_number(), 
                     "use": "work", 
                     "rank": 2},
                    
                    {"system": "phone", 
                     "value": fake.phone_number(), 
                     "use": "home", 
                     "rank": 2},
                    
                    {"system": "phone", 
                     "value": fake.phone_number(), 
                     "use": "mobile", 
                     "rank": 1},
                    
                    {"system": "email", 
                     "value": fake.email(), 
                     "use": "home", 
                     "rank": 2}
                ],
                    
                "gender": fake.random_element(["male", "female", "non-binary"]),
                "birthDate": fake.date_of_birth(minimum_age=18, maximum_age=100).isoformat(),
                
                "address": [
                    {
                        "use": "home",
                        "type": "postal",
                        "line": [fake.street_address()],
                        "city": fake.city(),
                        "state": fake.state_abbr(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    },
                    {
                        "use": "home",
                        "type": "physical",
                        "line": [fake.street_address()],
                        "city": fake.city(),
                        "postalCode": fake.postcode(),
                        "country": "AUS"
                    }
                ],
                
                 "contact": [
                    {
                        "relationship": [
                            {
                                "coding": [
                                    {
                                        "system": "http://internal4.health.nsw.gov.au/hird/view_domain_values_list.cfm?ItemID=10813",
                                        "code": "27",
                                        "display": "Carer"
                                    }
                                ]
                            }
                        ],
                        "name": {
                            "use": "official",
                            "family": fake.last_name(),
                            "given": [fake.first_name()]
                        },
                        "telecom": [
                            {"system": "phone", "value": fake.phone_number(), "use": "home"}
                        ]
                    }
                ],
                 
                "generalPractitioner": [
                    {"reference": f"#{fake.uuid4()}", "type": "PractitionerRole"}
                ],
                
                "managingOrganization": {"reference": f"#{fake.uuid4()}", "type": "Organization"}
            }
        ],
        
        "identifier": [
            {
                "use": "official",
                "type": {
                    "coding": [
                        {
                            "system": "http://terminology.hl7.org/CodeSystem/v2-0203",
                            "code": "PLAC",
                            "display": "Placer Identifier"
                        }
                    ],
                    "text": "Placer Identifier"
                },
                "system": "http://ausbizconsultingservices.com.au/ereferral/referralIds",
                "value": f"GPEREFERRAL-{fake.random_number(digits=8, fix_len=True)}"
            }
        ],
        
        "basedOn": [
            {
                "display": "ServiceRequest"
            }
        ],
        
        "status": "active",
        "intent": "order",
        "priority": "routine",
        "code": {
            "coding": [
                {
                    "system": "https://www.findacode.com/snomed/306206005--referral-to-service.html",
                    "code": "306206005",
                    "display": "Referral to service"
                }
            ],
            "text": "Bootcamp Healthcare e-Referral Service"
        },
        
        "subject": {
            "reference": "#a694c9e5-be8d-443c-97b0-af7a7d542f4c",
            "type": "Patient"
        },
        "occurrenceTiming": {
            "repeat": {
                "duration": 12,
                "durationUnit": "mo"
            }
        },
        "authoredOn": fake.date_time_this_year().isoformat(),
        "occurrenceTiming": {
            "repeat": {"duration": 12, "durationUnit": "mo"}
        },
        "requester": {"reference": f"#{fake.uuid4()}", "type": "PractitionerRole"},
        
        "performer": [
            {
                "type": "HealthcareService",
                "identifier": {"value": fake.pystr(min_chars=4, max_chars=10)},
                "display": fake.company()
            },
            
            {
                "type": "Organization",
                "identifier": {"value": fake.pystr(min_chars=4, max_chars=10)},
                "display": fake.company()
            }
        ]
    }



if __name__ == "__main__":
    referral = generate_referral()
    with open("referral.json", "w") as file:
        json.dump(referral, file, indent=4)
    print("Referral JSON saved to 'referral.json'")
