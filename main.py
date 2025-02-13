import google.generativeai as genai
from colorama import Fore, Style, init

init(autoreset=True)  

genai.configure(api_key="AIzaSyAVHw-tmhFmmcucXjiI6OXSQ6R_HU-1y8c")


prompts = {
    "resumo": "Resuma o seguinte assunto de forma clara e objetiva: ",
    "explicacao_simples": "Explique de forma simples e didática para um iniciante:",
    "geracao_de_ideias": "Gere ideias criativas sobre o seguinte tema:",
    "traducao": "Traduza o seguinte texto para inglês, coloque uma aplicação em uma frase e explique palavra por palavra:"
}


def gerar_resposta(opcao, entrada_usuario):
        prompt_escolhido = f"{prompts[opcao]} {entrada_usuario}"
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt_escolhido)

        return response.text




opcoes = ['resumo', 'explicacao_simples', 'geracao_de_ideias', 'traducao']

while True:
    posicao_escolhida = int(input("""
    📜 MENU DE OPÇÕES 📜
    1️⃣ - Resumo
    2️⃣ - Explicação Simples
    3️⃣ - Geração de Ideias
    4️⃣ - Tradução
    0️⃣ - Sair
    🛑 Digite o número da opção desejada:
        """))
    if posicao_escolhida > 0 and posicao_escolhida <= len(opcoes):
        opcao = opcoes[posicao_escolhida - 1]

        if opcao not in prompts:
            print("❌ Opção inválida. Tente novamente. ❌ ")
        else:
            entrada_usuario = input("Digite o tema: ").strip()
            resposta = gerar_resposta(opcao, entrada_usuario)
            resposta = resposta.replace("**", "").replace("* ", "- ")
            print(f"""
🤖🤖🤖🤖🤖🤖🤖🤖

Resposta da IA: 
{Fore.GREEN}{resposta}{Style.RESET_ALL}

🤖🤖🤖🤖🤖🤖🤖🤖
            """)
    elif posicao_escolhida == 0:
        print("👋  Fim do programa 👋 " )
        break
    else:
        print("❌ Opção inválida ❌")

