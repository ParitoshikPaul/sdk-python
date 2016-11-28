from setuptools import setup, find_packages

setup(
    name='thingspace_cloud_python_sdk',
    version='1.0.0',
    description='ThingSpace Cloud SDK for Python',
    url='https://thingspace.verizon.com/developer/apis#/vzcloud/v1/index.html',

    packages=find_packages(),
    #include certs for requests
    package_data={'': ['*.pem']},
)
