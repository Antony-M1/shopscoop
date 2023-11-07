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

