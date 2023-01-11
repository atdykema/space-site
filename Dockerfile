FROM python3

# RUN get from remote repo

#get Geckodriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz

RUN sudo tar -xvf geckodriver-v0.31.0-linux64.tar.gz

RUN sudo mv geckodriver /usr/local/bin/

RUN sudo chmod +x /usr/local/bin/geckodriver

#get Firefox
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A6DCF7707EBC211F

RUN sudo apt-add-repository "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu bionic main"

RUN sudo apt-get update

RUN sudo apt-get install -y firefox

#get Gunicorn
RUN sudo apt-get install -y Gunicorn

#get pip
RUN sudo apt-get install -y python3-pip

#get pip packages
RUN sudo pip3 install flask

RUN sudo pip3 install selenium

#get and update nginx
RUN sudo apt-get install -y nginx

RUN cd /

RUN cd /etc/nginx/sites-enabled

RUN touch space-site

#Run cat >  space-site

RUN sudo service nginx restart

RUN cd ~/space-site

#start server
RUN gunicorn app:app
