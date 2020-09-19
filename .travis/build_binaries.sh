#!/bin/bash

if [ $TRAVIS_OS_NAME = 'osx' ]; then
  pyinstaller --onefile --paths kb/ kb/__main__.py -n kb_v011_osx
elif [ $TRAVIS_OS_NAME = 'windows' ]; then
  pyinstaller --onefile --paths kb/ kb/__main__.py -n kb_v011_win
else
  pyinstaller --onefile --paths kb/ kb/__main__.py -n kb_v011_linux
fi

