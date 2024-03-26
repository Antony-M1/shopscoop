# shopscoop
Django, django, shopscoop


# Prerequisites
* Python3.11
* Postgresql 16

# .env
Basically the `.env` file contains the environment variables.
Rename the **.env.example** to **.env** file and fill the needed variables.

# Media
Create a folder with the name of **media** inside the Project


# Postgres backup and restore
<details>
  <summary> postgres backup </summary>
  ```
  pg_dump -h localhost -U {postgres_user} -d {db_name} -Fc -f {filename}.dump
  ```
</details>

<details>
  <summary>postgres restore </summary>
  ```
  pg_restore -h localhost -p 5432 -U {postgres_user} -d {db_name} {filename}.dump
  ```
</details>

# Issues
<details>
  <summary>psycopg installing issues</summary>


If you facing any issues while install `psycopg` please refere this [link](https://stackoverflow.com/questions/19843945/psycopg-python-h-no-such-file-or-directory/74544823#74544823).

Or run this command
```
sudo apt-get install libpq-dev
```
</details>
