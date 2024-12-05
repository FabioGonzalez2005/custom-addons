{
    'name': "Lista de tareas",

    'summary': """
    Sencilla Lista de tareas""",

    'description': """
    Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo
modelo de datos
    """,

    'author': "Fabio",
    'website': "https://fabiosoft.es",
    'application': True,

    'category': 'Productivity',
    'version': '0.1',

    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/views.xml',
    ]
}