# About This Project

> This project deploy jupyter notebook server on heruko through docker.

# How to use

* clone this repo
* `cd heroku_jupyter`

* you can also add other python packages: `pipenv install <package_name>`, or just replace pipfiles
* install Docker, Heroku CLI, and create an new app on Heruko first
* `mv envfile_example envfile` , fill your: notebook password `password`, app name `heroku_app`.
* `heroku login` & `heroku container:login`
* if you want to build locally `./scripts/d_build.sh` & `/usr/local/bin/jupyter notebook --allow-root --config=./conf/jupyter.py`
* push to heroku: `./scripts/h_push+release.sh`

> https://heroku-jupyter-87049.herokuapp.com/
