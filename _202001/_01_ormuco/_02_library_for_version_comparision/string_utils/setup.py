import setuptools

setuptools.setup(
     name='StringUtilsDemo',
     version='0.0.1',
     scripts=['string_utils/string_utils.py'] ,
     author="Amandeep",
     url='http://pypi.python.org/pypi/StringUtilsDemo/',
     author_email="deep.aman91@gmail.com",
     description='An awesome package that does something',
     long_description='long_description: An awesome package that does something',
     # install_requires=['re==2.2.1', 'url'],
     packages=setuptools.find_packages(),
     # python_requires='>=3.6',
 )