#!/usr/bin/env bash
# Bash script that sets up a web servers for the deployment of web_static

# check the installed packages on the system with dpkg -l 
if ! dpkg -l | grep -q nginx; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html


echo "Hello Everyone" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# check if symbolic link exists
if [ -L "/data/web_static/current" ]; then
	sudo rm -rf "/data/web_static/current"
fi
# creating symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# give the ownership to the user (chown) and the group (chgrp)
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

# updating the nginx config to serve the content of /data/web_static/current/ to hbnb_static
file_to_config="/etc/nginx/sites-available/default"
text_in_file=$(mktemp)
echo -e "\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n" >> "$text_in_file"
sudo sed -i "/listen 80 default_server/r $text_in_file" "$file_to_config"
sudo rm "$text_in_file"

sudo service nginx restart
