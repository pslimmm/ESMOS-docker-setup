## Moodle Docker setup for Azure VM
for ESM (Enterprise Solution Development) 

credits to creator [seunayolu](https://github.com/seunayolu/docker-project)

Steps:

0. SSH into the Azure VM
```bash
ssh -i <private-key-file-path> <vm-user>@<vm-ip>
# if the key fails, use the vm account password
# vm-user is azureuser
```

1. create a .env file containing the variables below:
```bash
nano .env
```
```
MYSQL_ROOT_PASSWORD=YOUR_OWN_ROOT_PASSWORD_FOR_DATABASE
MYSQL_DATABASE=DATABASE_NAME_FOR_MOODLE
MYSQL_USER=MOODLE_USERNAME
MYSQL_PASSWORD=MOODLE_USER_PASSWORD
```
2. check all env variables are loaded/exists
```bash
docker compose config
```
3. build
```bash
docker compose up --build -d
```
4. once everything is set up, access the moodle page through your-vm-ip:80
   - set db driver as improved MySQL
   - change database host to clouddb (this is the container name for the database)
   - set everything else as default
