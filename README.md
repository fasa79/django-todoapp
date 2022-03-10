
# Django ToDoApp

This project is developed as an exercise during TM R&D Internship. Link for the deployed website is [here][df1]



### Running the project locally

First, clone the repository to the local machine: <br />
`git clone https://github.com/fasa79/django-todoapp.git`

Then install the requirements
`pip install -r requirements.txt`

Convert the filename `todoapp/example.settings` to `todoapp/settings.py`

Run Mysql server in your local machine and create a new database for this project

Update database setting in `todoapp/settings.py` based on your database

Apply the migrations:
`python manage.py migrate`

Finally, run the development server:
`python manage.py migrate`

**Have Fun!**

[df1]: <http://chocoberry.pythonanywhere.com/>
