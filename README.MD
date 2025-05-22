
## Execucao Do Projeto

Para executar o projeto (Inicializar venv / Baixar Blibiotecas)

```bash
  node stup.js
```

Acessar o Ambiente Virtual (Linux)

```bash
source venv/bin/activate
```

Acessar o Ambiente Virtual (Windows PowerShell)
```bash
.\venv\Scripts\Activate.ps1
```


Executar o Aplicativo
```bash
python dashboard.py
```

Sair  do Ambiente virtual
```bash
deactivate
```
## Funcionalidades

### Leitura e limpeza dos dados  
- O arquivo `train.csv` é carregado.  
- Linhas com valores ausentes nas colunas **Age** e **Fare** são removidas para garantir a qualidade da análise.

### Cálculo de estatísticas básicas  
- Calcula e exibe no console:  
  - Média e mediana da **idade** e **tarifa**.  
  - Correlação entre idade e tarifa, permitindo entender a relação entre essas variáveis.

### Interface interativa  
- Dropdown para o usuário escolher o tipo de gráfico desejado:  
  - **Dispersão** (Idade x Tarifa)  
  - **Histograma** (Distribuição de Idade)  
  - **Boxplot** (Tarifa por Classe)  
  - **Barras** (Número de sobreviventes por sexo)  

- Slider que filtra os dados por **idade máxima**, ajustando dinamicamente os gráficos conforme a seleção.

### Visualizações dinâmicas  
- Os gráficos são atualizados automaticamente conforme o usuário modifica as opções, proporcionando uma análise exploratória interativa dos dados.

---

## Objetivo

Permitir uma exploração visual e interativa dos dados do Titanic, facilitando o entendimento das relações entre idade, tarifa, classe e sobrevivência dos passageiros, por meio de gráficos dinâmicos e filtráveis.

## Authors

- [@arthurcamp.ss](https://www.github.com/arthurd3)

