FROM python:3.9-slim

# Installing Unzip
RUN apt-get install -yqq unzip

# Download the Chrome Driver
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`
curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE
`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
ENV DISPLAY=:99

ADD requirements.txt /
RUN pip install -r requirements.txt
ADD main.py /
CMD [ "python", "./main.py"]