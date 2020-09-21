#!/bin/bash

if [ $TRAVIS_OS_NAME = 'osx' ]; then
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${TRAVIS_TAG}_osx
elif [ $TRAVIS_OS_NAME = 'windows' ]; then
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${TRAVIS_TAG}_win
else
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${TRAVIS_TAG}_linux
fi

