release: bash launch.sh
web: gunicorn --chdir project/server __init__:app
heroku ps:scale web=1


