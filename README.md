# LinkedIn Advance #

A Flask app that utilizes a Celery task queue and Redis broker to schedule the sending of LinkedIn Messages and InMail. Selenium and ChromeDriver are used to automate headless browser interaction in lieu of the lack of exposure of messaging in the LinkedIn API.

## Quick Start ##

1.  Install Redis and project dependencies

    ```shell
    $ sudo apt-get install redis-server
    $ pip install -r requirements.txt
    ```
2.  Download the ChromeDriver binary for your platform and note its `PATH` (https://sites.google.com/a/chromium.org/chromedriver/downloads)
3.  Create a `.env` file with your LinkedIn information, ChromeDriver location and a secret key for the Flask app

    ```
    EMAIL=...
    PASSWORD=...
    CHROMEDRIVER_PATH=...
    SECRET_KEY=...
    ```

  * To generate the secret key (http://flask.pocoo.org/docs/0.12/quickstart/):

    ```python
    >>> import os
    >>> os.urandom(24)
    '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
    # Copy and paste the output into the .env file.
    ```

4.  Run the Flask app in your terminal

    ```shell
    $ export FLASK_APP=app.py
    $ export FLASK_DEBUG=1
    $ flask run
    ```
5.  Initialize the Redis server and the Celery worker in 2 separate terminal instances

    ```shell
    $ redis-server
    ```

    ```shell
    $ celery -A celery_tasks worker --loglevel=info
    ```
6.  Begin scheduling your LinkedIn Messages and InMail!
