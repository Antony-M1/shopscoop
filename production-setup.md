# DJANGO PRODUCTION SETUP WITH NGINX AND ASGI
In this setup, we are going to set up the production setup in `AWS EC2` instance.

Here the way to connect the `AWS EC2` from `VS-Code` using `.pem` file
`Note: Make sure You have converted the **.pem** file into read only file` If not please yous this command to change the file
```
chmod 400 your-key-pair.pem
```
Add this configuration in your local machine in this path `/home/$USER/.ssh/config`
```
Host shopscoop
    HostName <YOUR-IP>
    User ubuntu
    IdentityFile /home/ubuntu/_practice/python/django/shopscoop_production/my-ec2.pem
```
the default user is `ubuntu` make sure which user your using.

# Prequisites
* [Python3.11](https://www.linuxcapable.com/how-to-install-python-3-11-on-ubuntu-linux/)
* [Postgresql 16 Setup](https://computingforgeeks.com/install-and-configure-postgresql-on-ubuntu/)
* [Nginx](https://ubuntu.com/tutorials/install-and-configure-nginx#2-installing-nginx)

Make sure you have the above service installed in your ubuntu machine.

# Get Started
## Step 1
Clone the project
```
git clone https://github.com/Antony-M1/shopscoop.git
```
Create the `.env` file from `.env.example` and fill the needed data

## Step 2
Create the `environment` using `python 3.11`
```
python3.11 -m venv env
```
Activate the environment using this command
```
source env/bin/activate
```
Install all the requirements packages using this command
```
pip install -r requirements.txt
```
If your facing any issue while install `psycopg2` refer this [link](https://stackoverflow.com/questions/74727501/error-could-not-build-wheels-for-psycopg2-which-is-required-to-install-pyproje)

## Step 3
Migrate the changes
```
python manage.py makemigrations
python manage.py migrate
```
Collect the static files
```
python manage.py collectstatic
```

## Step 4
**[Add Inbound rules](https://github.com/Antony-M1/django-production-setup/blob/main/prod_docs/django-with-gunicorn-and-nginx.md#add-inbound-rules)** Have to add in EC2

Uvicorn
```
uvicorn shopscoop.asgi:application
```
