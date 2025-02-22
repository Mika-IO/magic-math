import requests
import browser_cookie3
from bs4 import BeautifulSoup

# URL da página que você deseja baixar
url = 'https://bb.cruzeirodosulvirtual.com.br/ultra/courses/_1010481_1/outline/assessment/_17689233_1/overview/attempt/_165641607_1/review/inline-feedback?attemptId=_165641607_1&mode=inline&isStudentFeedbackPeekPanel=false&columnId=_4092300_1&contentId=_17689233_1&courseId=_1010481_1'

# Carregar os cookies do navegador (ajusta para o navegador que você está usando)
cookies = browser_cookie3.chrome()

# Fazer a requisição GET com os cookies da sessão ativa
response = requests.get(url, cookies=cookies)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Utilizar BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar o elemento <h1> com a classe específica
    h1_element = soup.find('h1', class_='panel-title secondary-title student')

    # Verificar se o elemento foi encontrado e extrair o texto
    if h1_element:
        title = h1_element.get_text(strip=True)
    else:
        # Caso não tenha encontrado o título, usar um nome padrão
        title = 'pagina_sem_titulo'

    # Nome do arquivo baseado no título da página
    filename = f"{title.replace(' ', '_').replace('-', '_')}.html"

    # Salvar o conteúdo da página em um arquivo HTML
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f"Página salva como: {filename}")
else:
    print(f"Falha ao acessar a página. Código de status: {response.status_code}")
