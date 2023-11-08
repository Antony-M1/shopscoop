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

We can test this by entering the project directory and using gunicorn to load the project’s ASGI module:

```
uvicorn shopscoop.asgi:application
```
Note: The admin interface will not have any of the styling applied since Gunicorn or Uvicorn does not know how to find the static CSS content responsible for this

## Step 5
Edit the gunicorn service for socket `gunicorn.socket`
```
sudo nano /etc/systemd/system/gunicorn.socket
```
Add this
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

# Step 6
Next, Create and open a systemd service file for Gunicorn with sudo privileges in your text editor. The service filename should match the socket filename with exception of the extension
```
sudo nano /etc/systemd/system/gunicorn.service
```
Add this
```
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/shopscoop
ExecStart=/home/ubuntu/shopscoop/env/bin/gunicorn \
          --access-logfile - \
          -k uvicorn.workers.UvicornWorker \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          shopscoop.asgi:application

[Install]
WantedBy=multi-user.target
```
You can now start and enable the Gunicorn socket. This will create the socket file at /run/gunicorn.sock now and at boot. When a connection is made to that socket, systemd will automatically start the gunicorn.service to handle it:
```
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

You can confirm that the operation was successful by checking for the socket file.

**Checking for the Gunicorn socket file**
```
sudo systemctl status gunicorn.socket
```
Next, check for the existence of the gunicorn.sock file within the /run directory:
```
file /run/gunicorn.sock
```
**output**
```
Output
/run/gunicorn.sock: socket
```

**Testing Socket Activation**
Currently, if you’ve only started the gunicorn.socket unit, the gunicorn.service will not be active yet since the socket has not yet received any connections. You can check this by typing:
```
sudo systemctl status gunicorn
```
You should receive output like this

Output
```
○ gunicorn.service - gunicorn daemon
     Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: ● gunicorn.socket
```
You can verify that the Gunicorn service is running by typing:
```
sudo systemctl status gunicorn
```
## Configure Nginx to Proxy Pass to Gunicorn or Uvicorn
Now that Gunicorn is set up, you need to configure Nginx to pass traffic to the process Start by creating and opening a new server block in Nginx sites-available directory
```
sudo nano /etc/nginx/sites-available/shopscoop
```
add this
```
server {
    listen 80;
    server_name shopscoop.in;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/ubuntu/shopscoop;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Save and close the file when We're finished. Now we can enable the file by linking it to the sites-enabled directory

```
sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```
If already exsists
```
sudo ln -sf /etc/nginx/sites-available/shopscoop /etc/nginx/sites-enabled
```
Test our Nginx configuration for syntax errors by typing

```
sudo nginx -t
```
If no errors are reported, go ahead and restart Nginx by typing:

```
sudo systemctl restart nginx
```
Finally, We will need to open up our firewall to normal traffic on port 80. Since we no longer need access to the development server, We can remove the rule to open port 8000 as well:
```
sudo ufw delete allow 8000
sudo ufw allow 'Nginx Full'
```
We should now be able to go to our server’s domain or IP address to view our application.

Check the site it is serving the static file if not please add this command & also if your getting `404` please run this command
```
sudo usermod -a -G ubuntu www-data
```
restart the `Nginx`
```
sudo systemctl restart nginx
```
