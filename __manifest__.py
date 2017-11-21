# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0',
    'author': 'Rohan',
    'category': 'Hospital',
    'depends': [
        'base','report'
    ],
    'data': [
        'report/report_action.xml',
        'report/report_patient_view.xml',
        'views/doctorallcategory.xml',
        'views/patientallcategory.xml',
        'views/facilityallcategory.xml',
        'data/patient_action_data.xml',
        
    ],
    'installable': True,
    'application': True,
}
