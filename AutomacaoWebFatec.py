# importando as bibliotecas.
from selenium import webdriver
# Executa o ChromeDriverManager.
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Criando um instalador e para reconher a verção atual do meu Crome e atualizar o ChromeDriver.
servico = Service(ChromeDriverManager().install())

# criando a conecção com o navegador.
navegador = webdriver.Chrome(service=servico)
time.sleep(3)  # Tempo para abrir o Chrome.

# Criando um comando para o robo entrar em algum site escolido.
navegador.get("https://fatecrl.edu.br/")
time.sleep(3)  # Tempo para acessar o site da Fatec.

# Criando um endereço com xpath do site.
# Clicando no icone do curso CIÊNCIA DE CADOS.
navegador.find_element(
    'xpath', '//*[@id="main"]/main/div[2]/section[1]/div/div[2]/a/img').click()
time.sleep(3)  # Tempo para clicar no curso de CD.

# Indo para a pagina da fatec no Intagram.
navegador.get(
    'https://www.instagram.com/accounts/login/?source=logged_out_megaphone_signup')
time.sleep(3)  # Tempo para acessar o site da Fatec no Instagram

# Inserindo o Usuario.
navegador.find_element(
    'xpath', '//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys('USUARIO_DO_INSTAGRAM')
time.sleep(2)

# Inserindo a Senha.
navegador.find_element(
    'xpath', '//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys('SENHA_DO_INSTAGRAM')
time.sleep(2)

# Clicando no botão de Entrar.
navegador.find_element('xpath', '//*[@id="loginForm"]/div[1]/div[3]').click()
time.sleep(10)

# Indo para a pagina da fatec no Intagram.
navegador.get('https://www.instagram.com/fatecrl/')
time.sleep(3)  # Tempo para acessar o site da Fatec no Instagram

# Click em seguir a fatec.
navegador.find_element(
    'xpath', '//*[@id="mount_0_0_dQ"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button').click()
