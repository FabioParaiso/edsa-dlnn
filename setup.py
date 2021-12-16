from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='group_labeling',
    version='0.1',
    author='Fabio Oliveira',
    author_email='paraiso.fabio@gmail.com',
    description='Create a model capable of identifying the persons of this group',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'setuptools'
    ],
    packages=[
        'group_labeling'
    ],
)