# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poet-with-pybind11']

package_data = \
{'': ['*'], 'poet-with-pybind11': ['src/*']}

install_requires = \
['pybind11>=2.10.1,<3.0.0']

setup_kwargs = {
    'name': 'poet-with-pybind11',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'wararaki',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
