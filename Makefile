install:
	poetry install

brain-games:
	poetry run brain-games
	
build:
	poetry build
	
publush:
	poetry publush --dry-run
	
package-install:
	python3 -m pip install --user dist/*.whl