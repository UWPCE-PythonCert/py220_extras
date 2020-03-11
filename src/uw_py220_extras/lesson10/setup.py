from setuptools import setup, find_namespace_packages

setup(
    name='my_example',
    description = "Add a short description here!",
    author = "Andy Miles",
    author_email = "me@andykmiles.net",
    version='0.1dev',
    package_dir = {'': 'src'},
    packages = find_namespace_packages(where='src'),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.rst').read(),
    long_description_content_type="text/x-rst; charset=UTF-8",
    url="https://gitlab.com/blah",
)
