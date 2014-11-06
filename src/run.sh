#!/bin/bash
echo "Mounting smb://$KV_HOST/$KV_PATH in /koppelvlak/orcaexports .. "
mount.cifs -o user=$KV_USER //$KV_HOST/$KV_PATH /koppelvlak/orcaexports
python producer.py
