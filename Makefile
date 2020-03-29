# constants

# output name
OUTPUT_NAME				=	$(shell basename $(CURDIR))
# source directory
SOURCE_DIRECTORY	=	$(CURDIR)/src
# build output directory
OUTPUT_DIRECTORY	=	$(CURDIR)/build

PYTHON_VERSION		=	3
PYTHON						=	"python$(PYTHON_VERSION)"
PIP								=	"pip$(PYTHON_VERSION)"
ifndef GOPATH
$(error GOPATH is not set)
endif

# host os detection
HOST_OS=unknown
ifeq ($(OS),Windows_NT)
	HOST_OS=windows
else
	UNAME=$(shell uname -s)
	ifeq ($(UNAME),Linux)
		HOST_OS=linux
	endif
	ifeq ($(UNAME),Darwin)
		HOST_OS=osx
	endif
endif

# default to test and build
all: test build

# check build environment consistency
check:
	@if [ "$(HOST_OS)" = 'unknown' ]; then echo "FATAL: Could not detect HOST_OS"; exit 1; fi

# install build dependencies
deps: check
	@$(PIP) install iterm2

# install development dependencies
deps-dev: check deps
	@$(PIP) install yapf futures isort flake8

# format code
format: check
	isort --skip-glob=.tox --recursive .
	yapf

# run golint on all source tree
lint: check
	flake8 --exclude=.tox

# build
build:
	$(PYTHON) setup.py sdist bdist_wheel

run: check build
	$(PYTHON) "$(SOURCE_DIRECTORY)/$(OUTPUT_NAME).py"

# run tests
test: check
	$(PYTHON) setup.py test

# clean build artefacts
clean:
	rm -rf "$(OUTPUT_DIRECTORY)"

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test:
	rm -rf .tox/
	rm -f .coverage
	rm -rf htmlcov/

# release & upload
release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
	@du -h dist

# install
install-develop:
	@$(PIP) install -e .

install: clean
	@$(PYTHON) setup.py install

# docs
docs:
	cd docs && make html