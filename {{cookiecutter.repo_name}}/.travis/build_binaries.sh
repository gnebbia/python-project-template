#!/bin/bash

V_REMOVED=$(tr -d "v" <<< "$TRAVIS_TAG")
RELEASE_VER=$(tr "." "_" <<< "$V_REMOVED")

if [ $TRAVIS_OS_NAME = 'osx' ]; then
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${RELEASE_VER}_osx
elif [ $TRAVIS_OS_NAME = 'windows' ]; then
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${RELEASE_VER}_win
else
  pyinstaller --paths {{ cookiecutter.repo_name }}/ --onefile {{ cookiecutter.repo_name }}/__main__.py -n {{ cookiecutter.repo_name }}_${RELEASE_VER}_linux
fi

