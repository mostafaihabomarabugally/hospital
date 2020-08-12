{
    'name'       : 'Hospital Managment',
    'description': 'Module for managing the Hospital.',
    'author'     : 'Mostafa Ihab',
    'version'    : '1.0.0', 
    'depends'    : ['base'],
    'data':[
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml',
    ],
    'demo':[
        
        ],

    'application': True,
}