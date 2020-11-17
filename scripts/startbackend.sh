# sudo apt-get update -y
# sudo apt-get install nginx -y
sudo service nginx start
sudo cp -f ./nginx.conf /etc/nginx/nginx.conf
sudo service nginx reload

