
tf init
tf plan -var nc_api_key="${NC_API_KEY}" -var do_token="${DIGITALOCEAN_TOKEN}"
tf apply -var nc_api_key="${NC_API_KEY}" -var do_token="${DIGITALOCEAN_TOKEN}" -auto-approve
tf destroy -var nc_api_key="${NC_API_KEY}" -var do_token="${DIGITALOCEAN_TOKEN}" -auto-approve

tail -f /var/log/cloud-init-output.log

ssh root@143.198.152.193