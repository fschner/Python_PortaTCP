# Python_PortaTCP
Script em Python verifica se uma porta TCP esta ativa caso Inativa Executa Script.sh para reiniciar serviço

# Crontab com saida para log

*/3 * * * * /usr/bin/python3 /home/fschner/python/monitor_grafana/script.py >> /home/fschner/python/monitor_grafana/log.txt
