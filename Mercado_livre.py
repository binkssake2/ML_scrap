#!/usr/bin/env python
# coding: utf-8

# In[504]:


import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


# In[550]:


produto = "termomentro"
infos = []
chromedriver = r"C:\Users\binks\Desktop\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.mercadolivre.com.br/")
sleep(2)


# In[551]:


barra_busca = driver.find_element_by_xpath("/html/body/header/div/form/input")
barra_busca.click()
barra_busca.send_keys(produto)

search = driver.find_element_by_xpath("/html/body/header/div/form/button")
search.click()
sleep(3)


# In[552]:


urls_produtos = driver.find_elements_by_class_name("main-title")
price_produtos = driver.find_elements_by_class_name("item__price")
sleep(5)


# In[553]:


infos_preliminares = []
name_produtos = []
preco_produto = []
for el in urls_produtos:
    name_produtos.append(el.text)
for el in price_produtos:
    preco_produto.append(el.text)

for i in range(len(name_produtos)):
    try:
        infos_preliminares.append({"nome":name_produtos[i],"preco":preco_produto[i]})
    except:
        continue


# In[ ]:


num_vendas_cada = []
for el in infos_preliminares:
    conta_pags = 1
    driver.find_element_by_link_text(el['nome']).click()
    sleep(2)
    
    try:
        num_vendas = driver.find_element_by_xpath("//*[@id=\"root-app\"]/div/div[1]/div[2]/div[1]/section[2]/div[4]/dl/dd[1]/strong").text
    except:
        try:
            num_vendas = driver.find_element_by_xpath("//*[@id=\"root-app\"]/div/div[1]/div[2]/div[1]/section[2]/div[3]/dl/dd[1]/strong").text
        except:
            try:
                num_vendas = driver.find_element_by_xpath("//*[@id=\"root-app\"]/div/div[1]/div[2]/div[1]/section[2]/div[2]/dl/dd[1]/strong").text
            except:
                num_vendas_stri = driver.find_element_by_xpath("//*[@id=\"root-app\"]/div[2]/div[2]/div[1]/div[2]/div[1]/form/div[3]/div/div/p")
                num_vendas = num_vendas_stri.text.replace(" vendas","")

    num_vendas_cada.append(num_vendas)
    
    for i in range(conta_pags):
        driver.execute_script("window.history.go(-1)")
        
    sleep(2)
    


# In[ ]:


final_tchuru = []
for i in range(len(infos_preliminares)):
    final_tchuru.append({"nome_anuncio":infos_preliminares[i]["nome"],"preco":infos_preliminares[i]["preco"],"num_vendas":num_vendas_cada[i]})


# In[ ]:


print(final_tchuru)


# In[ ]:


####embaixo é tudo teste, relaxa a pica#


# In[ ]:


###############################################################################################################################



