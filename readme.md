# About This Project
> This project deploy jupyter notebook server on heruko through docker.




# How to use
1. clone this repo
1. `cd heroku_jupyter`
1. you can also add other python packages: `pipenv install <package_name>`, or just replace pipfiles
1. install docker, heroku cli first
1. create an new app on heruko
1. `mv envfile_example envfile` then fill your: notebook password `password`, app name `heroku_app`.
1. `heroku container:login`
1. login heroku (cli) `heroku container:login`
1. docker build & push to heroku: `./scripts/d_b+h_r.sh`

> https://stark-sands-87049.herokuapp.com/


