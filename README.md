Aluna: Ester Lohana Lopes Peres 


Prova: Python e Selenium

Parte 1: Questões Teóricas (5 questões)

1. Explique a diferença entre Selenium IDE e Selenium WebDriver. (2 pontos)
• Dica: Inclua a funcionalidade principal de cada um e seu propósito.

R= A principal diferença está na complexidade e no propósito. O Selenium IDE é uma extensão de navegador, intuitiva e voltada para quem não deseja programar. Já o Selenium WebDriver é uma biblioteca que exige conhecimento em linguagens de programação para criar automações mais robustas e personalizadas.

2. Quais são os principais tipos de localizadores (locators) usados no Selenium WebDriver para encontrar elementos na página? Explique dois deles. (2 pontos)

R= Entre os principais localizadores estão: ID, Name, Class Name, Xpath e Tag Name.
O ID localiza elementos pelo identificador único no HTML:
<input type="text" id="username" />
O Xpath permite navegar pela estrutura DOM do HTML, localizando elementos com base em atributos, hierarquia ou posição.

3. O que é um WebElement no Selenium? Dê um exemplo de como interagir com um WebElement usando Python. (2 pontos)

R= O WebElement representa um elemento único da página, como um botão ou um campo de texto, permitindo interações como clicar (elemento.Click()) ou digitar.

4. No Selenium WebDriver, o que acontece se você tentar interagir com um elemento que ainda não está visível ou carregado na página? Qual comando você usaria para resolver isso? (2 pontos)

R= Caso o elemento não seja encontrado, o Python retorna exceções como NoSuchElementException. Para evitar erros, pode-se adicionar um wait(1) ou utilizar espera explícita entre as ações.

5. Cite duas limitações do Selenium IDE que podem levar à escolha do Selenium WebDriver em projetos maiores. (2 pontos)

R= A maior limitação do Selenium IDE é a falta de flexibilidade, já que não permite programação. Isso dificulta lidar com eventos imprevisíveis, como pop-ups. Já o Selenium WebDriver oferece recursos avançados, como captura de tela e geração de relatórios.
