### Install this locally:
0. Have python 3.12
1. Install
   ```shell
   pip install -r requirements.txt
   ```
2. Set up postgres database and adapt `testproject/settings.py`'s `DATABASES` as needed.
   - I just use `Posgtgres.app`, to make my life easier. Created a `user_has_substitute` database there.  My OS user is `user`, locally passwordless login is default.

### Run the test:
```shell
python manage.py migrate testapp zero \
&& rm -f testapp/migrations/0001_initial.py \
&& python manage.py makemigrations testapp \
&& python manage.py migrate \
&& python manage.py insert_test_sequence_table_4_2
```


-----

<br /><br /><br /><br />

----

###### creating this project in the first place.
> ```shell
> pip install -r requirements.txt      
> django-admin startproject testproject
> cd testproject/
> git init
> python manage.py startapp testapp
> 
> 
> python manage.py makemigrations testapp
> python manage.py migrate
> 
> mkdir -p testapp/management/commands
> touch testapp/management/commands/insert_testmodel.py
> 
> mv testapp/management/commands/insert_testmodel.py testapp/management/commands/insert_test_sequence_table_4.py
> mv testapp/management/commands/insert_test_sequence_table_4.py testapp/management/commands/insert_test_sequence_table_4_2.py
> 
> # reset / remove SQLITE 3:
> rm db.sqlite3 testapp/migrations/0001_initial.py && python manage.py makemigrations testapp && python manage.py migrate && python manage.py insert_test_sequence_table_4_2 
> ```
