PACKAGE=papaya
TESTS_DIR=tests
DOC_DIR=docs

# Use current python binary instead of system default.
COVERAGE = python $(shell which coverage)
FLAKE8 = flake8
DJANGO_ADMIN = django-admin.py
PO_FILES = $(shell find $(PACKAGE) -name '*.po')
MO_FILES = $(PO_FILES:.po=.mo)

all: default


default: build


clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -path '*/__pycache__/*' -delete
	find . -type d -empty -delete
	rm -f $(MO_FILES)
	@rm -rf tmp_test/

build: $(MO_FILES)


%.mo: %.po
	cd $(abspath $(dir $<)/../../..) && $(DJANGO_ADMIN) compilemessages

update:
	pip install --upgrade pip setuptools
	pip install --upgrade -r requirements_dev.txt
	pip freeze

testall:
	tox

test: build
	PYTHONPATH=. python -Wdefault manage.py test $(TESTS_DIR)



# Note: we run the linter in two runs, because our __init__.py files has specific warnings we want to exclude
lint:
	check-manifest
	$(FLAKE8) --config .flake8 --exclude $(PACKAGE)/__init__.py $(PACKAGE)
	$(FLAKE8) --config .flake8 --ignore F401 $(PACKAGE)/__init__.py
	$(FLAKE8) --config .flake8 $(TESTS_DIR)

coverage:
	$(COVERAGE) erase
	$(COVERAGE) run "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py" --branch setup.py test
	$(COVERAGE) report "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py"
	$(COVERAGE) html "--include=$(PACKAGE)/*.py,$(TESTS_DIR)/*.py"

doc:
	$(MAKE) -C $(DOC_DIR) html


.PHONY: all default clean coverage doc install-deps lint test
