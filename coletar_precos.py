from selenium.webdriver.support.select import Select
from selenium.webdriver import Chrome
from selenium import webdriver
import pandas as pd
import time
import coleta_de_dados as cdd


def iniciar_navegador():
    global navegador
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    navegador = Chrome(chrome_options = options)
    url = ('https://www.atualcard.com.br/cartoes-de-visita/74/75')
    navegador.get(url)
iniciar_navegador()

def coletar_valores_e_quantidade():
    valores={}
    lista_valores = navegador.find_elements_by_xpath(
        '//div[@class="js-quantity-container u-flex u-flex-flex-wrap-wrap u-flex-justify-content-space-between"]//li/span')
    indice_dos_valores = 0
    for value in lista_valores:
        indice_dos_valores += 1
        valores.update({indice_dos_valores: value.text})
    print(valores)

    index = {}
    lista_quantidade = navegador.find_elements_by_xpath(
    '//div[@class="js-quantity-container u-flex u-flex-flex-wrap-wrap u-flex-justify-content-space-between"]//label/span')
    indice_das_quantidades = 0
    for value in lista_quantidade:
        indice_das_quantidades += 1
        index.update({value.text: indice_das_quantidades})
        # print(index)c

def acessar_site_e_raspar_dados():
    lista_material = cdd.dictionary_material.values()
    lista_material = list(lista_material)
    lista_cor = cdd.dictionary_cor.values()
    lista_cor = list(lista_cor)
    lista_cobertura = cdd.dictionary_cobertura.values()
    lista_cobertura = list(lista_cobertura)
    lista_tamanho = cdd.dictionary_tamanho.values()
    lista_tamanho = list(lista_tamanho)


    for valor in lista_material:

        select_material = navegador.find_element_by_css_selector("#atributo_1")
        material_obj = Select(select_material)
        mo = material_obj.select_by_value(valor)
        time.sleep(4)
        for valor_cor in lista_cor:
            try:
                select_cor = navegador.find_element_by_css_selector("#atributo_2")
                cor_obj = Select(select_cor)
                co = cor_obj.select_by_value(valor_cor)
                # print(valor_cor)
                time.sleep(5)
            except:
                pass
            for valor_cobertura in lista_cobertura:
                try:
                    select_cobertura = navegador.find_element_by_css_selector("#atributo_3")
                    cobertura_obj = Select(select_cobertura)
                    cob = cobertura_obj.select_by_value(valor_cobertura)
                    # print(valor_cobertura)
                    time.sleep(5)
                except:
                    pass
                for valor_tamanho in lista_tamanho:
                    try:
                        select_tamanho = navegador.find_element_by_css("atributo_4")
                        tamanho_obj = Select(select_tamanho)
                        tam = tamanho_obj.select_by_value(valor_tamanho)
                        # print(valor_tamanho)
                        time.sleep(5)
                        coletar_valores_e_quantidade()
                    except:
                        coletar_valores_e_quantidade()




coletar_valores_e_quantidade()
acessar_site_e_raspar_dados()

navegador.close()
