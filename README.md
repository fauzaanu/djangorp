## DRP

Django + Redis + Postgres

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-h8kBw?referralCode=NC4Tt6)

### Tailwindcss

- The `jstoolchain` folder includes a tailwindcss setup
- You should run `npm i` to install the dependencies
- There is also a `.xml` file for PyCharm users to make it a `File Watcher`
- The `tailwind.config.js` file is configured to search for `html` and `py` files
- `.py` files because forms.py could have tailwindcss classes due to the user of `crispy-forms` with `crispy-tailwind`

### Role of Redis

- Redis is used as a cache firstly
- Secondly, it is used as a message broker for Celery
- Thirdly, it is used as a session store

### Celery

- Celery is used for background tasks that take a long time to complete.
- `tasks.py` is where the tasks are defined and they can be called from anywhere in the project
- `celery.py` is where the celery app is created and configured, explicitly adding the tasks may be required

### Important Notes

- Generate migrations from dev environment and commit them to the repo
- Anything that takes too long to run should be a background task
- There is no need for a `.env` file to be committed to the repo as the `settings.py` file is configured to read from
  the variables defined in railway
- To create a superuser install railway cli and run `railway run python manage.py createsuperuser`
- Split into apps as much as possible (does not make sense early on but will later on)
- `Templates` folder outside will be used for base / navbar / footer templates and anything that is not app specific
- Other templates should be inside the app folder with the recommended naming convention
  of `appfolder/templates/app_name/template_name.html` (e.g. `users/templates/users/login.html`)
- `static` folder outside will be used for base / navbar / footer css and js files and anything that is not app specific
- Other static files should be inside the app folder with the recommended naming convention
  of `appfolder/static/app_name/css/style.css` (e.g. `users/static/users/css/style.css`)
- CSRFTRUSTEDORIGINS might be needed and ifso set to the domain name of the website (e.g. `example.com`)
  inside `settings.py`

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/-h8kBw?referralCode=NC4Tt6)