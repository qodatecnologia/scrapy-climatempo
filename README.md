#Tarefa
![](https://lh3.googleusercontent.com/pw/ACtC-3dhGywOBQhaeDTjNyOamyJxopQYiGW6S9HDtKmUyVeE35EBosvlc8G_ukQ4DZ3HzBoAG_jDiconDG0mZ4TlVE2Gf42FFd-Tx-3iDABXxaNdajMidID_uBaAoT_2cULVTXCpIRwXlurpZYSoV2UWfcsY=w340-h319-no?authuser=0)
---

"Basicamente, você deverá usar<br> 
* um site de Climatempo, por exemplo, e 
* salvar na frequência horária um ou X municípios dos dados apresentados como esse componente(cidade/estado/temperatura/descrição/sensação/umidade/Pressão/vento/atualização). 
* Estruturar em um mongo ou MySQL e usar o scrapy para isso."

# Executando aplicação:
1. ative o ambiente isolado em /ct_env/Scripts/activate
2. instale as libs necessárias com "pip install -r requirements.txt" no diretório principal
3. Inicie mongodb localmente e altere -se necessário- os dados de localhost com porta 27017
4. execute no terminal "scrapy crawl ct" para execução dp crawler que de hora em hora executará a requisição e armazenará em collections(mongodb)
