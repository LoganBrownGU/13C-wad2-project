# PopPopCinema

## Setup Instructions
Navigate to the project directory and follow steps:
1. Create a virtual environment: `python3 -m venv env`.
You should now see a folder labelled 'env' in the project directory.

2. Ativate the virtual environment:
Mac/Linux - `source env/bin/activate`
Windows - `env/scripts/activate`
<br />(to deactivate the virtual environment: `deactivate`).

3. Install required packages: `pip3 install -r requirements.txt`.

4. Delete old database if it exists: `rm db.sqlite3`

5. Migrate: `python manage.py migrate --run-syncdb`

6. Run population script: `python populate_cinema.py`

7. Run server: `python3 manage.py runserver`.
