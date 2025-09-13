rm -rf dist build *.egg-info **/*.egg-info
python -m pip install --upgrade pip setuptools wheel build twine
python -m build
python -m twine check dist/*
python -m twine upload dist/*