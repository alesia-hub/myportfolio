# My portfolio Website

Created using Django with python.
To run application on your local, run following command:
```bash
python manage.py runserver
```

## Starting New Project details:

- navigate to ne new project folder
- in terminal run django command:
    readme.md file formatting
```bash
django-admin startproject personal_portfolio
```

- adding new applications/apps:
```bash
python manage.py startapp blog 
python manage.py startapp portfolio
```

- **NOTE:** after adding new app, add these apps under `settings.py` file > INSTALLED_APPS


## Managing Admin user access:

In order to use admin part of the application, need to create superuser first.
Run following command in terminal to do that:
```bash
python manage.py createsuperuser
```

This superuser and passowrd are very important. It will be available online and anyone can access admin part with it. 

To change the passowrd run following:
```bash
python manage.py changepassword
```

multiple superusers can be created. 


## Managing Models:
In order for the new model been available under Admin side and for the rest of the project to be used, it needs to be added under `admin.py` file for each app which is going to use this model.
Checkout file `portfolio/admin.py` to see how it was done. 

## Managing Images:
All Images should be saved in the root/media/[app_name]/[your_fodlder_name] folder. 

### Add following variables under `settings.py` file:
- **MEDIA_ROOT** : contains a default root folder for all images
- **NEDIA_URL** : contains statis URLs for images 

After that image url should be added under `url.py` file.