Catalog Project
=============

This is second project for Full Stack Developer Nano-Degree

## Requirements
  - Vagrant
  - VirtualBox (as a provider)

## Install and usage
  - Clone this repository: `git clone https://github.com/vanadium23/catalog-project`
  - Put your client_secrets.json from Google+ to catalog dir
  - Start vagrant using `vagrant up`
  - Connect to vagrant using `vagrant ssh`
  - Go to catalog dir `cd /vagrant/catalog`
  - Run `python database_setup.py` to setup database
  - Run `python database_seed.py` to add initial values
  - Run `python application.py` to add initial values
  - Go to your browser and open link `localhost:8080`