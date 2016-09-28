from setuptools import setup, find_packages

#not quite worked out yet, leaving it for now

setup(name='thingspace.cloud',
      version='1.0',
      description='Verizon Personal Cloud SDK',
      author='Verizon',
      author_email=' m2msupport@verizon.com',
      license='MIT',
      url='https://thingspace.verizon.com/developer/apis#/vzcloud/v1/index.html',
      install_requires=['requests'],
      packages=find_packages(),
      zip_safe=False,
      )
