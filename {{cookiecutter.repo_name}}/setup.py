#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import io
from setuptools import setup, find_packages


setup(name='{{ cookiecutter.repo_name }}',
      version='{{ cookiecutter.version }}',
      description='{{ cookiecutter.project_short_description }}',
      keywords='{{ cookiecutter.repo_name }}',
      author='{{ cookiecutter.full_name }}',
      author_email='{{ cookiecutter.email }}',
      url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
      download_url='https://github.com/gnebbia/{{ cookiecutter.repo_name }}/archive/v{{ cookiecutter.version }}.tar.gz',
      license='GPLv3',
      long_description=io.open(
          './docs/README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      platforms='any',
      zip_safe=False,
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Development Status :: 1 - Planning',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   ],
      packages=find_packages(exclude=('tests',)),
      include_package_data=True,
      install_requires=[],{% if cookiecutter.entry_point == 'cli' %}
      entry_points={
           'console_scripts':[
               '{{ cookiecutter.repo_name }} = {{ cookiecutter.repo_name }}.main:main',
           ]
      },{% endif %}
      )
