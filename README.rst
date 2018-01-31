Meu Legislador
==============

O esse projeto tem como objetivo facilitar os estudos dos dados disponíveis 
pela `API dados abertos <https://dadosabertos.camara.leg.br/swagger/api.html>`_ 
da câmara dos deputados federais.

Organização dos arquivos
------------------------
- `data/ds` Onde se encontra os dados para estudos
- `data/notebooks` Os estudos, usando o jupyter notebooks 

Como usar os dados
------------------
Os dados dentro da pasta `data\ds` e com a extensão `.json.gz` podem ser utilizados diretamente no pandas
usando o seguinte código::

    #Se a versão do panda for 0.21 (ou superior)
    import pandas as pd
    df = pd.read_json('data/ds/deputados.json.gz', orient='split')

    #Se a versão do panda for inferior a 0.21, ou seja, qualquer versão
    import pandas as pd
    import gzip
    with gzip.open('data/ds/deputados.json.gz', 'rb') as f:
        df = pd.read_json(f, orient='split')

Pode-se, também, obter os dados diretamente pela internet, e com isso não sendo necessário o download do projeto inteiro.
Para isso usa-se o código::

    import numpy as np
    import pandas as pd
    import gzip
    import io
    import requests

    web_response = requests.get(PROPOSICAO_JSON_DS_FILE, timeout=30, stream=True)
    f = io.BytesIO(web_response.content)

    with gzip.GzipFile(fileobj=f) as fh:
        df = pd.read_json('https://github.com/bozoh/meu-legislador/raw/master/data/ds/deputados/deputados.json.gz', orient='split')

O que os demais arquivos fazem?
-------------------------------
Basicamente oferece uma estrutura (longe de estar completa) para obter os dados e salva-los em um formato que facilite o estuto
através de ferramentas como o pandas + jupyter notebooks

Instalando dependências 
-----------------------
Para instalar as bibliotecas necessárias use o comando::

    pip install -r requirements.txt


Descrição dos dados disponíveis
-------------------------------
Até o momento:

- `data/ds/deputados/deputados-ids.dat` - Contém os Números identificadores de todos os deputados deste o 1983
- `data/ds/deputados/deputados.json.gz` - Contém os dados dos deputados, desde 1983, disponibilizado pelo dados abertos, dados como Nome, partido, situação, ...
- `data/ds/deputados/deputados.despesas-[ano(s)].json.gz` - Contém os dados dos gastos dos deputados, referente a um ou mais anos, a partir de 2008 (não há dados anteriores disponíveis)
- `data/ds/proposicoes/proposicoes-ids.dat` - Contém os Números identificadores de todas as proposições (PL, PLP, PEC, PLV, PDC, MPV) a partir de 01/01/1984
- `data/ds/proposicoes/proposicoes.json.gz` - Contém os dados de todas as proposições (PL, PLP, PEC, PLV, PDC, MPV) da câmara dos deputados a partir de 01/01/1984

