SHELL := /bin/bash
env :
	rm ./env −fr
	virtualenv ./env
	/bin/bash −c 'source ./env/bin/activate ; pip install wxmplot; \
	 pip install −e . '

clean :
	git clean −Xfd
dist :
	python setup . py sdist
upload :
	python setup . py sdist upload
