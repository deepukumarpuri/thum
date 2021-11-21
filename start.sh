echo "Cloning Repo...."
git clone https://github.com/deepukumarpuri/thum.git /thum
cd /thum
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
