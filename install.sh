sudo add-apt-repository ppa:deadsnakes/ppa;
sudo apt update;
sudo apt-get install python3.10;
sudo apt install python3-pip;
sudo apt install python3-virtualenv;
virtualenv -p python3.10 venv;
source venv/bin/activate;
pip install -r requirements.txt;
python manage.py makemigrations cadastro;
python manage.py migrate;
python manage.py runserver;