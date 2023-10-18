from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import random
import pyautogui
from decouple import config



arq_seguidores = 'sequidores.txt'
arq_seguindo = 'seguindo.txt'
arquivo_saida = 'nao_segue_de_volta.txt'

usuario=config('usuario')
senha=config('senha')
loop=int(config('loop'))

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com/')
sleep(3)
perfil =input('DIGITE SEU @ DO INSTAGRAM! @')


user_element = driver.find_element(By.XPATH,
                                "//input[@name='username']")
user_element.clear()
sleep(random.randint(5, 10))
user_element.send_keys(usuario)
sleep(random.randint(5, 10))
password_element = driver.find_element(By.XPATH,
                                    "//input[@name='password']")
password_element.clear()
password_element.send_keys(senha)
sleep(random.randint(5, 10))
password_element.send_keys(Keys.RETURN)
sleep(random.randint(5, 10))


try:
    def meus_seguidores(perfil):
        print('!!!!!!!!O SCRIPT ESTA EM EXECUÇAO NAO MEXA NO MOUSE OU TECLADO POIS PODE ACABAR ENCERRANDO A EXECUÇAO!!!!!!!!')
        driver.get(f'https://www.instagram.com/{perfil}/followers/')
        sleep(random.randint(5, 10))
        arq_seguidores = 'sequidores.txt'    
  
        pyautogui.click(x=867, y=566)
        for _ in range(loop):
            pyautogui.scroll(-1)
            sleep(random.randint(1, 2))
    #
        seguindores = driver.find_elements(By.XPATH,
                                            "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
        with open(arq_seguidores, 'w',encoding='utf-8') as arquivo:
            for seguidor in seguindores:
                arquivo.write(seguidor.text + '\n')
        print(f'Dados foram escritos com sucesso no arquivo: {arq_seguidores}')

#   
    def Eu_sigo(perfil):
        print('!!!!!!!!O SCRIPT ESTA EM EXECUÇAO NAO MEXA NO MOUSE OU TECLADO POIS PODE ACABAR ENCERRANDO A EXECUÇAO!!!!!!!!')
        driver.get(f'https://www.instagram.com/{perfil}/following/')

        sleep(random.randint(5,10))

        arq_seguindo = 'seguindo.txt'
        pyautogui.click(x=692, y=640)
        for _ in range(loop):
            pyautogui.scroll(-1)
            sleep(random.randint(1, 2))
   
        following = driver.find_elements(By.XPATH,
                                        "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
        with open(arq_seguindo, 'w',encoding='utf-8') as arquivo:
            for seguindo in following:
                arquivo.write(seguindo.text + '\n')

        
        print(f'Dados foram escritos com sucesso no arquivo: {arq_seguindo}')
  
    def Comparar(arq_seguidores,arq_seguindo):
        with open(arq_seguidores,'r') as file1, open(arq_seguindo,'r') as file2:
            linhas1=set(file1.readlines())
            linhas2=set(file2.readlines())
#
        print(f'Comparando Seguindo com seguidores')
        diferencas = linhas2.difference(linhas1)
    #
        arquivo_saida = 'nao_segue_de_volta.txt'
    #
        sleep(random.randint(5,10))
    #
        with open(arquivo_saida,'w',encoding='utf-8') as file3:
            for linha in diferencas:
                file3.write(linha)

    def seguir():
        with open(arquivo_saida,'r') as file4:
            tamanho = file4.readlines()
            for linha in tamanho[:198]:
                pesquisa = driver.find_elements(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")
                pesquisa = pesquisa[2].click()
                driver.get(f'https://www.instagram.com/{linha}/')
                sleep(random.randint(5,10))

                #inserir_usuario = driver.find_element(by.XPATH,
                #                            "//input[@class='x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j']")

                #if inserir_usuario:
                #    inserir_usuario.send_keys(linha)
                #    sleep(random.randint(5,10))
                #    inserir_usuario.send_keys(Keys.RETURN)
                #    sleep(random.randint(5,10))
                #    
                deixar_de_seguir = driver.find_element(By.XPATH,
                                                    "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()
                print(f'comecei a seguir {linha}')
        driver.close()


    def unfollow():
        with open(arquivo_saida,'r') as file5:
            tamanho = file5.readlines()
            for linha in tamanho[:198]:
                pesquisa = driver.find_elements(By.XPATH,"//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd']")
                pesquisa = pesquisa[2].click()
                driver.get(f'https://www.instagram.com/{linha}/')
                sleep(random.randint(5,10))

                #inserir_usuario = driver.find_element(by.XPATH,
                #                            "//input[@class='x1lugfcp x19g9edo x1lq5wgf xgqcy7u x30kzoy x9jhf4c x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j']")

                #if inserir_usuario:
                #    inserir_usuario.send_keys(linha)
                #    sleep(random.randint(5,10))
                #    inserir_usuario.send_keys(Keys.RETURN)
                #    sleep(random.randint(5,10))
                    
                deixar_de_seguir = driver.find_element(By.XPATH,
                                                    "//div[@class='_aacl _aaco _aacw _aad6 _aade']").click()
                sleep(random.randint(1,3))                                    
                deixar= driver.find_elements(By.XPATH,"//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 x1l90r2v xyamay9 x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
                deixar[4].click()
                print(f'deixei de a seguir {linha}')
        driver.close()


except Exception as e:
    print(e)
    driver.close()

if __name__ == "__main__":
    while True:
        opçao = int(input(f'''
        PRIMEIRO ESCOLHA OQUE GOSTARIA DE FAZER ?

        1) --- APENAS LISTAR OS USUARIO QUE TE SEGUE ?
        2) --- APENAS LISTAR OS USUARIOS QUE VOCE SEGUE ?
        3) --- VERIFICAR OS USUARIOS QUE NAO TE SEGUE DE VOLTA ?
        4) --- DEIXAR DE SEGUIR USUARIOS ?
        5) --- SEGUIR USUARIOS ?
        0) --- Sair do boot?
        '''))
        if opçao not in [1,2,3,4,5,0]:
            print('Opçao invalida tente novamente')
            continue
        elif opçao ==0:
            break
        elif opçao == 1:
            meus_seguidores(perfil)
        elif opçao == 2:
            Eu_sigo(perfil)
        elif opçao ==3:
            Comparar(arq_seguidores,arq_seguindo)
        elif opçao ==4:
            unfollow()
        elif opçao ==5:
            seguir()