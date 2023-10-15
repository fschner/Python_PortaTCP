import socket
import subprocess

# Configurações
host = 'localhost'  # Endereço do host
port = 3000         # Número da porta que você deseja testar
script_path = './auto_porta.sh'  # Caminho para o script shell Executar pelo terminal
# script_path = '/home/fschner/python/monitor_grafana/auto_porta.sh' Executar pelo CRONTAB

def test_tcp_connection(host, port):
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)  
            s.connect((host, port))
        return True  # Conexão bem-sucedida
    except (ConnectionRefusedError, socket.timeout):
        return False  # Conexao falhou

if not test_tcp_connection(host, port):
    print(f"A porta {port} esta inativa. Executando o script shell...")
    try:
        # Execute o script shell usando subprocess
        subprocess.run([script_path], check=True, shell=True)
        print("Script shell executado com sucesso.")
    except subprocess.CalledProcessError:
        print("Erro ao executar o script shell.")
else:
    print(f"A porta {port} esta ativa.")
