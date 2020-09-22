.PHONY: default, lint

default:
	python -m {{ cookiecutter.repo_name }} 
spell:
	codespell . --ignore-words-list=hist --skip=./.* --quiet-level=2 || true
lint:
	pylint {{ cookiecutter.repo_name }} 
pep8:
	autopep8 {{ cookiecutter.repo_name }}  --in-place --recursive --aggressive --aggressive
clean:
	rm -rf build/ dist/ {{ cookiecutter.repo_name }}_manager.egg-info/
test:
	codespell . --ignore-words-list=hist --quiet-level=2
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	pytest
reinstall:
	pip uninstall {{ cookiecutter.repo_name }} 
	pyenv rehash
	pip install .
	pyenv rehash
