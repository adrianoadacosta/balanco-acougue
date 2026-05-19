# balanco-acougue
# 🥩 Sistema de Balanço para Açougue

Sistema desenvolvido em Python para automatizar análise de estoque, vendas e compras de açougue através de planilhas Excel.

O projeto lê automaticamente arquivos `.xlsx`, classifica os produtos por categoria e gera um balanço organizado em abas separadas.

---

# 🚀 Funcionalidades

✅ Leitura automática de planilhas Excel  
✅ Identificação automática de:
- estoque
- vendas
- compras

✅ Classificação automática de carnes:
- Bovina
- Aves
- Suíno
- Peixes
- Ovinos
- Miúdos
- Linguiça/Salsichão

✅ Subcategorias para carnes bovinas:
- Costela
- Patinho
- Cupim
- Contra Filé
- Carne Moída
- etc.

✅ Geração automática de:
- resumo estoque
- resumo vendas
- resumo compras

✅ Criação automática de abas:
- ESTOQUE
- VENDAS
- COMPRAS
- NÃO IDENTIFICADOS

✅ Ignora automaticamente:
- osso
- sebo

---

# 📂 Estrutura esperada

Coloque os arquivos na mesma pasta:

```text
BALANCO_ACOUGUE/
│
├── gerar_balanco.py
├── rodar_balanco.bat
├── estoque_maio.xlsx
├── vendas_maio.xlsx
├── compras_maio.xlsx
```

---

# ▶️ Como usar

## 1. Instalar dependências

```bash
pip install pandas openpyxl
```

---

## 2. Executar

Basta clicar duas vezes em:

```text
rodar_balanco.bat
```

ou rodar manualmente:

```bash
py gerar_balanco.py
```

---

# 📊 Resultado

O sistema gera automaticamente:

```text
BALANCO_FINAL.xlsx
```

com abas separadas para:
- estoque
- vendas
- compras
- itens não identificados

---

# 🛠 Tecnologias utilizadas

- Python
- Pandas
- OpenPyXL
- Excel

---

# 💡 Objetivo

O projeto foi criado para reduzir trabalho manual em conferência de balanço de açougue, facilitando agrupamento de carnes e análise de estoque.

---

# 📌 Melhorias futuras

- Interface gráfica
- Exportação automática formatada
- Executável `.exe`
- Integração com ERP
- Preenchimento automático de modelo oficial

---

# 👨‍💻 Autor

Desenvolvido por Adriano Costa 😄
