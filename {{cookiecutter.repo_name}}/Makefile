.PHONY: default, lint

default:
	python -m {{ cookiecutter.repo_name }}
lint:
	pylint {{ cookiecutter.repo_name }}
pep8:
	autopep8 {{ cookiecutter.repo_name }} --in-place --recursive --aggressive --aggressive
clean:
	rm -rf build/ dist/ {{ cookiecutter.repo_name }}.egg-info/
test:
	pytest
reinstall:
	pip uninstall {{ cookiecutter.repo_name }}
	pyenv rehash
	pip install --upgrade .
	pyenv rehash
