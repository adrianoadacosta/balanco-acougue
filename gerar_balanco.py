import os
import pandas as pd

def encontrar_arquivo(palavra):

    arquivos = os.listdir()

    for arquivo in arquivos:

        nome = arquivo.lower()

        if palavra in nome and arquivo.endswith(".xlsx"):
            return arquivo

    return None

# =========================
# CLASSIFICAR CATEGORIA
# =========================

def classificar(produto):
    produto = str(produto).lower()

    # IGNORAR
    if (
        "osso" in produto
        or "sebo" in produto
    ):
        return "Ignorar"

    # LINGUIÇA / SALSICHÃO
    elif (
        "linguiça" in produto
        or "linguica" in produto
        or "calabresa" in produto
        or "salsich" in produto
        or "cuiabana" in produto
        or "jiboia" in produto
        or "salaminho" in produto
        or "ling calab" in produto
    ):
        return "Linguiça/Salsichão"

    # MIÚDOS
    elif (
        "figado" in produto
        or "fígado" in produto
        or "mondongo" in produto
        or "coração" in produto
        or "coracao" in produto
        or "coraçao" in produto
        or "moela" in produto
    ):
        return "Miúdos"

    # PEIXES
    elif (
        "tilapia" in produto
        or "tilápia" in produto
        or "peixe" in produto
        or "salmao" in produto
        or "salmão" in produto
        or "camarao" in produto
        or "camarão" in produto
        or "merluza" in produto
        or "polaca" in produto
        or "panga" in produto
        or "vannamei" in produto
    ):
        return "Peixes"

    # OVINOS
    elif (
        "cordeiro" in produto
        or "ovina" in produto
        or "ovelha" in produto
    ):
        return "Ovinos"

    # SUÍNO
    elif (
        "suino" in produto
        or "suin" in produto
        or "pernil" in produto
        or "lombo" in produto
        or "porco" in produto
        or "torresmo" in produto
    ):
        return "Suíno"

    # AVES
    elif (
        "frango" in produto
        or "coxa" in produto
        or "sobrecoxa" in produto
        or "ave" in produto
        or "sassami" in produto
        or "asa" in produto
        or "galinha" in produto
        or "peito" in produto
        or "file de fgo" in produto
        or "bruster" in produto
        or "petisco" in produto
    ):
        return "Aves"

    # BOVINA
    elif (
        "bov" in produto
        or "maminha" in produto
        or "entrecot" in produto
        or "contra file" in produto
        or "contrafile" in produto
        or "carne moida" in produto
        or "costela" in produto
        or "prime ribe" in produto
        or "prime rib" in produto
        or "capa de file" in produto
        or "assado de tiras" in produto
        or "agulha" in produto
        or "picadao" in produto
        or "vazio" in produto
        or "entrevero" in produto
        or "paleta" in produto
        or "amaciado" in produto
    ):
        return "Bovina"

    return "Não identificado"


# =========================
# SUBCATEGORIA
# =========================

def subcategoria(produto, categoria):
    produto = str(produto).lower()

    if categoria == "Bovina":

        if "picanha" in produto:
            return "Picanha"

        elif "costela" in produto:
            return "Costela"

        elif "maminha" in produto:
            return "Maminha"

        elif "cupim" in produto:
            return "Cupim"

        elif "patinho" in produto:
            return "Patinho"

        elif "carne moida" in produto:
            return "Carne Moída"

        elif "contra file" in produto or "contrafile" in produto:
            return "Contra Filé"

        elif "entrecot" in produto:
            return "Entrecot"

        elif "prime rib" in produto or "prime ribe" in produto:
            return "Prime Rib"

        else:
            return "Outros Bovinos"

    return categoria


# =========================
# PROCESSAR PLANILHA
# =========================

def processar_planilha(
    nome_arquivo,
    coluna_produto,
    coluna_valor
):

    df = pd.read_excel(nome_arquivo)

    # Converter para número
    df[coluna_valor] = pd.to_numeric(
        df[coluna_valor],
        errors="coerce"
    )

    # Filtrar maiores que zero
    df = df[df[coluna_valor] > 0]

    # Categoria
    df["Categoria"] = df[coluna_produto].apply(classificar)

    # Subcategoria
    df["Subcategoria"] = df.apply(
        lambda linha: subcategoria(
            linha[coluna_produto],
            linha["Categoria"]
        ),
        axis=1
    )

    # Remover ignorados
    df = df[df["Categoria"] != "Ignorar"]

    return df


# =========================
# ESTOQUE
# =========================

""" estoque = processar_planilha(
   "Estoques new Aç Unisuper Matriz 04 05 2026.xlsx",
   "Desc. Produto",
    "Est. Fisíco", 
)"""

arquivo_estoque = encontrar_arquivo("estoque")

estoque = processar_planilha(
    arquivo_estoque,
    "Desc. Produto",
    "Est. Fisíco"
)

resumo_estoque = estoque.groupby(
    ["Categoria", "Subcategoria"]
)["Est. Fisíco"].sum().reset_index()


# =========================
# VENDAS
# =========================

""" vendas = processar_planilha(
    "Vendas new Aç Unisuper Matriz 04 05 2026.xlsx",
    "Descrição",
    "Qtdade",
) """

arquivo_vendas = encontrar_arquivo("venda")

vendas = processar_planilha(
    arquivo_vendas,
    "Descrição",
    "Qtdade"
)

resumo_vendas = vendas.groupby(
    ["Categoria", "Subcategoria"]
)["Qtdade"].sum().reset_index()


# =========================
# RENOMEAR COLUNAS
# =========================

resumo_estoque = resumo_estoque.rename(
    columns={"Est. Fisíco": "Estoque"}
)

resumo_vendas = resumo_vendas.rename(
    columns={"Qtdade": "Vendas"}
)


# =========================
# COMPRAS
# =========================

""" compras = processar_planilha(
    "Compras new Aç Unisuper Matriz 04 05 2026.xlsx",
    "Descrição",
    "Qtdade",
) """

arquivo_compras = encontrar_arquivo("compra")

compras = processar_planilha(
    arquivo_compras,
    "Descrição",
    "Qtdade"
)

resumo_compras = compras.groupby(
    ["Categoria", "Subcategoria"]
)["Qtdade"].sum().reset_index()

resumo_compras = resumo_compras.rename(
    columns={"Qtdade": "Compras"}
)


# =========================
# NÃO IDENTIFICADOS
# =========================

nao_identificados_estoque = estoque[
    estoque["Categoria"] == "Não identificado"
]

nao_identificados_vendas = vendas[
    vendas["Categoria"] == "Não identificado"
]

nao_identificados_compras = compras[
    compras["Categoria"] == "Não identificado"
]


# =========================
# EXPORTAR EXCEL
# =========================

""" with pd.ExcelWriter("BALANCO_FINAL.xlsx") as writer:

    # Balanço principal
    balanco.to_excel(
        writer,
        sheet_name="BALANCO",
        index=False
    )

    # Não identificados estoque
    nao_identificados_estoque.to_excel(
        writer,
        sheet_name="NAO_IDENT_ESTOQUE",
        index=False
    )

    # Não identificados vendas
    nao_identificados_vendas.to_excel(
        writer,
        sheet_name="NAO_IDENT_VENDAS",
        index=False
    )

    # Não identificados compras
    nao_identificados_compras.to_excel(
        writer,
        sheet_name="NAO_IDENT_COMPRAS",
        index=False
    ) """

with pd.ExcelWriter("BALANCO_FINAL.xlsx") as writer:

    resumo_estoque.to_excel(
        writer,
        sheet_name="ESTOQUE",
        index=False
    )

    resumo_vendas.to_excel(
        writer,
        sheet_name="VENDAS",
        index=False
    )

    resumo_compras.to_excel(
        writer,
        sheet_name="COMPRAS",
        index=False
    )

    nao_identificados_estoque.to_excel(
        writer,
        sheet_name="NAO_IDENT_ESTOQUE",
        index=False
    )

    nao_identificados_vendas.to_excel(
        writer,
        sheet_name="NAO_IDENT_VENDAS",
        index=False
    )

    nao_identificados_compras.to_excel(
        writer,
        sheet_name="NAO_IDENT_COMPRAS",
        index=False
    )

print("\nBALANCO_FINAL.xlsx gerado com sucesso!")

