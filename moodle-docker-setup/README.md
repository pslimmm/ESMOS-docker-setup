## Moodle Docker setup for Azure VM

credits to creator [seunayolu](https://github.com/seunayolu/docker-project)

Steps:

1. SSH into the Azure VM
```bash
ssh -i <private-key-file-path> <vm-user>@<vm-ip>
# if the key fails, use the vm account password
# vm-user is azureuser
```

2. install all needed apps and dependencies
```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose-v2 containerd
```

3. clone this repository into the VM
```bash
git clone https://github.com/pslimmm/moodle-docker-setup.git
```
change your directory to moodle-docker-setup
```bash
cd moodle-docker-setup
```

4. create a .env file containing the variables below:
```bash
nano .env
```
```
MYSQL_ROOT_PASSWORD=YOUR_OWN_ROOT_PASSWORD_FOR_DATABASE
MYSQL_DATABASE=DATABASE_NAME_FOR_MOODLE
MYSQL_USER=MOODLE_USERNAME
MYSQL_PASSWORD=MOODLE_USER_PASSWORD
```

5. check all env variables are loaded/exists
```bash
docker compose config
```

6. build
```bash
docker compose up --build -d
```


7. Set up SSL. The easiest way is to run Certbot on the host machine (the Azure VM).
```bash   
# Install Certbot:
sudo apt update && sudo apt install certbot

# Stop your Nginx container temporarily (to free up port 80 for validation):
docker compose stop nginx-proxy

# Run Certbot:
sudo certbot certonly --standalone -d yourdomain.com
```

8. once everything is set up, access the moodle page through your-vm-ip:80
   - set db driver as improved MySQL
   - change database host to clouddb (this is the container name for the database)
   - set everything else as default




