#PFE project

python -m venv myVenv #set the virtuel enviroment
pip install django djangorestframework djangdso-cors-headers

pip install psycopg2 psycopg2-binary # to communicate with postgres

django-admin startproject myProject . #create a django in current directory
python manage.py startapp crm

pip install -U djoser
pip install -U djangorestframework_simplejwt
#add "restframework and djoser " you can see djoser documentation https://djoser.readthedocs.io/en/latest/getting_started.html

react :
npm install --save axios react-router-dom redux redux-devtools-extension react-redux redux-thunk
