# boubyan-task

## Database config:
* ### create new mysql DB
        mysql -u root -p
    then enter root password on mysql.

        mysql> CREATE DATABASE boubyandb;

* ### create new user
        mysql> CREATE USER 'boubyanuser'@'localhost' IDENTIFIED BY 'boubyanpassword';

* ### give user access to DB
       mysql> GRANT ALL PRIVILEGES ON boubyandb.* TO 'boubyanuser'@'localhost';


## Django config:
* ### create new virtualenv and install requirements file.
        virtualenv env
        source env/bin/activate
        (env)pip install -r "path to project"/requirements.txt

* ### migrate data
        (env)python "path to manage.py file" makemigrations
        (env)python "path to manage.py file" migrate

* ### create new super user
        (env)python "path to manage.py file" createsuperuser
        Username: "your username"
        Email:
        Password: "your password"
        Password(again): "your password"

* ### load database data
        (env)ptyhon "path to manage.py file" loaddata fixtures/boubyandb.json

