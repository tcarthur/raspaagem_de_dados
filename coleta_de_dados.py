import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

class Url(object):

    def iniciar(self):
        self.gerar_url()

    def gerar_url(self):
        url = 'https://www.atualcard.com.br/cartoes-de-visita/74/75/cartoes-de-visita-couche-250g-4x0-uv-total-frente-8-8x4-8-cm-1000-12717'

        r = requests.get('http://localhost:8050/render.html', params={'url':url, 'wait': 2  })
        soup = BeautifulSoup(r.text, 'html.parser')

        categoria = soup.select('.js-select-submenu > option[value]')
        contador = 0
        global dictionary_categoria
        dictionary_categoria = {}
        for categoria_valor in categoria:
            contador += 1
            dictionary_categoria.update({categoria_valor.contents[0] : categoria_valor.get('value')})
            # print(dictionary_categoria)
        df_categoria = pd.Series(dictionary_categoria)

        material = soup.select('#atributo_1 > option[value]')
        contador = 0
        global dictionary_material
        dictionary_material = {}
        for material_valor in material:
            contador += 1
            dictionary_material.update({material_valor.contents[0] : material_valor.get('value')})
        df_material = pd.Series(dictionary_material)
        # print(dictionary_material)

        cor = soup.select('#atributo_2 > option[value]')
        contador = 0
        global dictionary_cor
        dictionary_cor = {}
        for cor_valor in cor:
            contador += 1
            dictionary_cor.update({cor_valor.contents[0] : cor_valor.get('value')})
        df_cor = pd.Series(dictionary_cor)
        # print(dictionary_cor)

        cobertura = soup.select('#atributo_3 > option[value]')
        contador = 0
        global dictionary_cobertura
        dictionary_cobertura = {}
        for cobertura_valor in cobertura:
            contador += 1
            dictionary_cobertura.update({cobertura_valor.contents[0] : cobertura_valor.get('value')})
        df_cobertura = pd.Series(dictionary_cobertura)
        # print(dictionary_cobertura)

        tamanho = soup.select('#atributo_4 > option[value]')
        contador = 0
        global dictionary_tamanho
        dictionary_tamanho = {}
        for tamanho_valor in tamanho:
            contador += 1
            dictionary_tamanho.update({tamanho_valor.contents[0] : tamanho_valor.get('value')})
        # print(dictionary_tamanho)
        df_tamanho = pd.Series(dictionary_tamanho)

        df_values = pd.concat([df_categoria,df_material, df_cor, df_cobertura, df_tamanho ])
        # print(df_values)

        url_start = []
        contador = 0
        for value in dictionary_categoria:
            contador += 1
            url_start.append(f'https://www.atualcard.com.br/cartoes-de-visita/74/{dictionary_categoria[value]}')

        url_df = pd.DataFrame(url_start)
        url_df.to_excel('url.xlsx')
        print(url_df)
start = Url()
start.iniciar()
