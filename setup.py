import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='plugs-newsletter',
    package = 'plugs_newsletter',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Reusable Newsletter APP',
    long_description=README,
    url='https://github.com/yo-solo/plugs-newsletter',
    author='Ricardo Lobo',
    author_email='ricardolobo@soloweb.pt',
    install_requires = [
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
