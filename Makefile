# full on
all: update-me buildout documentation # nginx

# update me from origin if possible, be graceful if not
update-me:
	git pull || exit 0

buildout:
	python bootstrap.py

# build documentation
documentation: update-sources changes statistics html
	#graphs bugs-everywhere

# update all projects from their origins
update-sources:
	#bin/buildout buildout:lib-prefix=/usr -vv
	bin/buildout -vv

# aggregate contents of CHANGES files across all projects
changes:
	bin/changes-aggregate

# build statistics across all projects
statistics:
	bin/statistics-build

# build graphviz images
graphs:
	mkdir -p var/sphinx/_downloads
	bin/laig > var/sphinx/_downloads/backend-graph.svg

# build html documentation with sphinx
html:
	bin/sphinx-build

pdf:
	bin/sphinx-latex
	cd var/latex; make; cd -


# optional

# install nginx
nginx:
	bin/buildout install nginx-headers_more_module nginx nginx-ctl templates

# generate videos using "gource" (to var/sphinx/_downloads/gource/)
videos:
	bin/gource-render-all

# publish videos, since normally rendered locally
videos-publish:
	rsync -auv --progress var/sphinx/_downloads/gource manticore@manticore.example.net:~/manticore/var/sphinx/_downloads/

# generate HTML views from "BugsEverywhere" issues
bugs-everywhere:
	bin/bugseverywhere-html
