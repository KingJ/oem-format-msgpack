from setuptools import setup


setup(
    name='oem-format-msgpack',
    version='1.0.0',

    author="Dean Gardiner",
    author_email="me@dgardiner.net",

    install_requires=[
        'oem-framework>=1.0.0',

        'msgpack-python>=0.4.7'
    ]
)
