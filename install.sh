sudo add-apt-repository ppa:deadsnakes/ppa -y;
sudo apt update -y;
sudo apt-get install python3.10 -y;
sudo apt install python3-pip -y;
sudo apt install python3-virtualenv -y;
virtualenv -p python3.10 venv;
source venv/bin/activate;
pip install -r requirements.txt;
python manage.py makemigrations cadastro;
python manage.py migrate;
python manage.py runserver;