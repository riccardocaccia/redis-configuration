# redis-configuration
Set of script and configurations useful to configure a VM as a Redis queue

### 1. Install Redis on its own dedicated VM
```bash
sudo apt update
sudo apt install redis-server -y
```

Modify the configuration file:
Bash

sudo nano /etc/redis/redis.conf

Add or update the following parameters:
```bash
    bind 0.0.0.0 (per accettare connessioni da altre VM)

    protected-mode no

    requirepass PasswordMasterAdmin (Imposta una password principale per te)
```
3. Restart and Configure Agents

Restart the service to apply changes:
Bash
```bash

sudo systemctl restart redis
```

Access the Redis CLI and configure the ACL for the various agents:
Bash
```bash
# Accedi con la password impostata
redis-cli -a PasswordMasterAdmin
```
Esegui i comandi per gli utenti:
```bash
# Utente Agente 1
ACL SETUSER agente1 on >secret_agente1 ~rq:queue:coda_agente1* +@all -@admin

# Utente Agente 2
ACL SETUSER agente2 on >secret_agente2 ~rq:queue:coda_agente2* +@all -@admin

# Utente Agente AWS
ACL SETUSER agente_aws on >secret_aws ~rq:queue:coda_aws* +@all -@admin
```
# Salva la configurazione
ACL save
