{
    'name': 'Módulo de instituto',
    'summary': 'Módulo para realizar la gestión del instituto.',
    'description': 'Este módulo puede ser utilizado por alumnos, maestros y padres para visualizar y gestionar las notas de los alumnos en sus actividades.',
    'version': '1.0.0',
    'category': 'Human Resources',
    'author': 'Sergio Groppa',
    'data': [
        'security/groups.xml',
        'security/tutoria_fct.xml',
        'security/alumno.xml',
        'security/empresa.xml',

        'views/menu_principal.xml',

        'views/alumno/view_form.xml',
        'views/alumno/view_tree.xml',
        'views/alumno/menu.xml',

        'views/empresa/view_form.xml',
        'views/empresa/view_tree.xml',
        'views/empresa/menu.xml',

        'views/tutoria_fct/view_form.xml',
        'views/tutoria_fct/view_tree.xml',
        'views/tutoria_fct/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}