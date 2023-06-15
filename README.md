# my_portfolio_blog
Both backend and frontend was made by me

How to create a virtual python environment:

1. Pick a folder for a project
2. Use

```python -m venv venv``` for Windows or

```python3 -m venv venv``` for Linux.

3. Enter your vitrual environment ```source test/bin/activate``` for Linux or

```test/Scripts/activate.bat``` In Windows CMD 

```test/Scripts/Activate.ps1``` In Windows Powershell

How to clone project to your virtual environment:

1. ```git clone https://github.com/JuicyS8da/my_portfolio_blog.git``` (to your folder)
2. ```cd my_portfolio_blog/```
3. ```pip install -r requirements.txt```
4. ```cd portfolio_blog/```
5. ```python manage.py runserver```
6. Put http://127.0.0.1:8000/ into url field in your browser
7. (optional) If you want to user django admin http://127.0.0.1:8000/admin/, default superuser is:

Login: user

Password: 123

or you can create your own superuser by putting this command into your console:
```python manage.py createsuperuser```
