from setuptools import setup
 
setup(
    name='Sisenik',
    version='1.0',
    py_modules=['sisenik'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sisenik=sisenik:cli
    '''
)
