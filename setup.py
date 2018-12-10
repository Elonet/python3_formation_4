from setuptools import setup

# On importe notre bibliothèque
import elonet_formation_4

setup(
    name='elonet_formation_4',
    version='0.0.1',
    author='Rasta dev',
    author_email='arthur@elonet.fr',
    url='https://elonet.github.io/python3_formation_4/',
    packages=['elonet_formation_4'],                                          # On ajoute notre bibliothèque au setup
    install_requires=['requests==2.20.1'],
    description='Demonstration de creation d\'un package Python',
    plateformes='ALL',
)