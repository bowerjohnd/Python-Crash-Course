# The settings.py file has django generated sensitive data.
#       The following is my additions to settings.py:

INSTALLED_APPS = [
    # My apps.
    'learning_logs',
    'accounts',

    # Third party apps
    'django_bootstrap5',

    # default django apps
    # ...
]

# My settings.
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'
LOGIN_URL = 'accounts:login'