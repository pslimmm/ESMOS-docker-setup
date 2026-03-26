## Odoo Docker setup for Azure VM
Setting up prebuilt odoo app on Azure VM using docker

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
cd odoo-setup
```

4. create a .env file containing the variables below:
```bash
nano .env
```
```
POSTGRES_HOST=odoo-db
POSTGRES_PORT=5432
POSTGRES_DB_USER=odoo
POSTGRES_DB_PASSWORD=YOUR_OWN_POSTGRES_DB_PASSWORD
PGADMIN_EMAIL=YOUR_OWN_PGADMIN_EMAIL
PGADMIN_PASSWORD=YOUR_OWN_PGADMIN_PASSWORD
```

5. check all env variables are loaded/exists
```bash
docker compose config
```

6. build
```bash
docker compose up --build -d
```

7. once everything is set up, access the odoo page through your-vm-ip/web/database/manager
    - restore a database backup you have installed (zip file)
    - set the master password