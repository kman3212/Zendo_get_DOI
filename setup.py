from setuptools import setup

setup(name='zenodo_get_DOI',
      description='get the dataset from Zenodo using DOI',
      packages=['zenodo_get_DOI'],
      version="0.0.1",
      install_requires=['requests','wget','json']
     )
