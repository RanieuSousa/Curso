

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))


tamanho_arquivo_mbps = tamanho_arquivo_mb * 8

tempo_download_minutos = tamanho_arquivo_mbps / velocidade_internet_mbps

print("O tempo aproximado de download do arquivo é de", tempo_download_minutos, "minutos.")
