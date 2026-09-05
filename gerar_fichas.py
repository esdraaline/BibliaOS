#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria as 66 fichas de livro em 02-Livros/. Idempotente."""

from pathlib import Path

DESTINO = Path(__file__).parent / "02-Livros"

# (seção, testamento, [(nome, [aliases...]), ...])
SECOES = [
    ("Pentateuco", "AT", [
        ("Gênesis", ["Gn", "Genesis"]), ("Êxodo", ["Ex", "Exodo"]),
        ("Levítico", ["Lv", "Levitico"]), ("Números", ["Nm", "Numeros"]),
        ("Deuteronômio", ["Dt", "Deuteronomio"]),
    ]),
    ("Históricos", "AT", [
        ("Josué", ["Js", "Josue"]), ("Juízes", ["Jz", "Juizes"]), ("Rute", ["Rt"]),
        ("1 Samuel", ["1Sm"]), ("2 Samuel", ["2Sm"]), ("1 Reis", ["1Rs"]),
        ("2 Reis", ["2Rs"]), ("1 Crônicas", ["1Cr"]), ("2 Crônicas", ["2Cr"]),
        ("Esdras", ["Ed"]), ("Neemias", ["Ne"]), ("Ester", ["Et"]),
    ]),
    ("Poéticos", "AT", [
        ("Jó", ["Job"]), ("Salmos", ["Sl"]), ("Provérbios", ["Pv", "Proverbios"]),
        ("Eclesiastes", ["Ec"]), ("Cânticos", ["Ct", "Canticos", "Cantares"]),
    ]),
    ("Profetas Maiores", "AT", [
        ("Isaías", ["Is", "Isaias"]), ("Jeremias", ["Jr"]),
        ("Lamentações", ["Lm", "Lamentacoes"]), ("Ezequiel", ["Ez"]), ("Daniel", ["Dn"]),
    ]),
    ("Profetas Menores", "AT", [
        ("Oseias", ["Os"]), ("Joel", ["Jl"]), ("Amós", ["Am", "Amos"]),
        ("Obadias", ["Ob"]), ("Jonas", ["Jn"]), ("Miqueias", ["Mq"]),
        ("Naum", ["Na"]), ("Habacuque", ["Hc"]), ("Sofonias", ["Sf"]),
        ("Ageu", ["Ag"]), ("Zacarias", ["Zc"]), ("Malaquias", ["Ml"]),
    ]),
    ("Evangelhos e Atos", "NT", [
        ("Mateus", ["Mt"]), ("Marcos", ["Mc"]), ("Lucas", ["Lc"]),
        ("João", ["Jo", "Joao"]), ("Atos", ["At"]),
    ]),
    ("Cartas Paulinas", "NT", [
        ("Romanos", ["Rm"]), ("1 Coríntios", ["1Co"]), ("2 Coríntios", ["2Co"]),
        ("Gálatas", ["Gl", "Galatas"]), ("Efésios", ["Ef", "Efesios"]),
        ("Filipenses", ["Fp"]), ("Colossenses", ["Cl"]),
        ("1 Tessalonicenses", ["1Ts"]), ("2 Tessalonicenses", ["2Ts"]),
        ("1 Timóteo", ["1Tm"]), ("2 Timóteo", ["2Tm"]),
        ("Tito", ["Tt"]), ("Filemom", ["Fm"]),
    ]),
    ("Cartas Gerais e Apocalipse", "NT", [
        ("Hebreus", ["Hb"]), ("Tiago", ["Tg"]), ("1 Pedro", ["1Pe"]),
        ("2 Pedro", ["2Pe"]), ("1 João", ["1Jo"]), ("2 João", ["2Jo"]),
        ("3 João", ["3Jo"]), ("Judas", ["Jd"]), ("Apocalipse", ["Ap"]),
    ]),
]

MODELO = """---
tipo: livro
nome: {nome}
aliases: [{aliases}]
testamento: {testamento}
secao: {secao}
status: vazio
fontes: []
lacunas: []
termos_originais: []
tags: []
ultima_revisao: null
---

## Panorama

## Contexto histórico e cultural

## Estrutura

## Temas centrais

## Termos originais

## Reflexão pessoal

## Lacunas a conferir
- [ ] 
"""

def main():
    DESTINO.mkdir(parents=True, exist_ok=True)
    criados = pulados = total = 0
    for secao, testamento, livros in SECOES:
        for nome, aliases in livros:
            total += 1
            arquivo = DESTINO / f"{nome}.md"
            if arquivo.exists():
                pulados += 1
                print(f"  pulado (já existe): {arquivo.name}")
                continue
            arquivo.write_text(
                MODELO.format(
                    nome=nome, aliases=", ".join(aliases),
                    testamento=testamento, secao=secao,
                ),
                encoding="utf-8", newline="\n",
            )
            criados += 1
    print(f"\n{total} livros | {criados} criados | {pulados} pulados")
    assert total == 66, f"esperado 66 livros, encontrado {total}"

if __name__ == "__main__":
    main()
