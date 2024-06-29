
# Build the package
build:
	- python3 -m build

# Publish to test.pypi.org
publish-test:
	- python3 -m twine upload --repository testpypi dist/*

# Publish the package
publish:
	- python3 -m twine upload dist/*