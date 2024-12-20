def generate_referral():
    return {
        "resourceType": "ServiceRequest",
        "id": "AUSBIZBOOTCAMP-REFERRAL-677",
        "contained": [
            {
                "resourceType": "PractitionerRole",
                "id": 220679,
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
                        "value": 244478
                    }
                ],
                "practitioner": {
                    "reference": "#51d4543d-1456-4497-bb2e-0e8f3b4c8ce1",
                    "type": "Practitioner"
                },
                "organization": {
                    "reference": "#a0d67bc1-6a1f-4d6f-811f-5dcc25405b93",
                    "type": "Organization"
                }
            },
            {
                "resourceType": "Practitioner",
                "id": "51d4543d-1456-4497-bb2e-0e8f3b4c8ce1",
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
                        "value": 5759318231854656
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": "Mills",
                        "given": [
                            "Eric"
                        ]
                    }
                ]
            },
            {
                "resourceType": "Organization",
                "id": "a0d67bc1-6a1f-4d6f-811f-5dcc25405b93",
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
                        "value": 282801
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
                        "value": "Bc19857"
                    }
                ],
                "active": True,
                "name": "Green Valley Family Clinic",
                "telecom": [
                    {
                        "system": "phone",
                        "value": "0432 274 223",
                        "use": "work"
                    },
                    {
                        "system": "email",
                        "value": "benjamincollier@example.com",
                        "use": "work"
                    }
                ],
                "address": [
                    {
                        "use": "work",
                        "type": "physical",
                        "line": [
                            "Level 4 7 Jessica Wade"
                        ],
                        "city": "South Brian",
                        "state": "SA",
                        "postalCode": "7078",
                        "country": "AUS"
                    }
                ]
            },
            {
                "resourceType": "Patient",
                "id": "a694c9e5-be8d-443c-97b0-af7a7d542f4c",
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
                        "value": 4427019257275108
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
                        "value": 4888825701
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
                        "value": "ftIfWwGU"
                    }
                ],
                "name": [
                    {
                        "use": "official",
                        "family": "Hoffman",
                        "given": [
                            "Michael",
                            "Joseph"
                        ]
                    }
                ],
                "telecom": [
                    {
                        "system": "phone",
                        "value": "1210-9693",
                        "use": "work",
                        "rank": 2
                    },
                    {
                        "system": "phone",
                        "value": "+61.7.9205.6604",
                        "use": "home",
                        "rank": 2
                    },
                    {
                        "system": "phone",
                        "value": "+61-8-2638-6349",
                        "use": "mobile",
                        "rank": 1
                    },
                    {
                        "system": "email",
                        "value": "brandyrobertson@example.net",
                        "use": "home",
                        "rank": 2
                    }
                ],
                "gender": "non-binary",
                "birthDate": "2005-10-27",
                "address": [
                    {
                        "use": "home",
                        "type": "postal",
                        "line": [
                            "649 Tracey Walkway"
                        ],
                        "city": "North Lisa",
                        "state": "WA",
                        "postalCode": "2619",
                        "country": "AUS"
                    },
                    {
                        "use": "home",
                        "type": "physical",
                        "line": [
                            "25 Smith Strip"
                        ],
                        "city": "New Christopher",
                        "postalCode": "2647",
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
                            "family": "Benitez",
                            "given": [
                                "Brittany"
                            ]
                        },
                        "telecom": [
                            {
                                "system": "phone",
                                "value": "0202 1667",
                                "use": "home"
                            }
                        ]
                    }
                ],
                "generalPractitioner": [
                    {
                        "reference": "#220679",
                        "type": "PractitionerRole"
                    }
                ],
                "managingOrganization": {
                    "reference": "#a0d67bc1-6a1f-4d6f-811f-5dcc25405b93",
                    "type": "Organization"
                }
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
                "value": "GPEREFERRAL-10220033"
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
        "authoredOn": "2024-03-17T16:54:58+00:00",
        "requester": {
            "reference": "#220679",
            "type": "PractitionerRole"
        },
        "performer": [
            {
                "type": "HealthcareService",
                "identifier": {
                    "value": "dummy"
                },
                "display": "Australian Bootcamp of Clinical Health Clinic Referral Service"
            },
            {
                "type": "Organization",
                "identifier": {
                    "value": "aubootcampref"
                },
                "display": "Australian Bootcamp of Mental Health Clinic"
            }
        ]
    }


if __name__ == "__main__":
    referral = generate_referral()
    print(referral)
