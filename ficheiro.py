import os
import random
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def generate_ai_content():
    topics = [
        "Tecnologia",
        "Ciência",
        "Viagens",
        "Literatura",
        "Música",
        "Filosofia",
        "Esportes",
        "Culinária"
    ]

    content = {
        "Tecnologia": "A tecnologia está em constante evolução, trazendo avanços incríveis como inteligência artificial, computação quântica e conectividade global.",
        "Ciência": "A ciência continua a desvendar os mistérios do universo, desde a física de partículas até a biologia molecular, impactando diretamente nossa vida cotidiana.",
        "Viagens": "Viajar é uma das melhores formas de aprendizado. Conhecer novos lugares e culturas amplia nossa visão do mundo e nos conecta com diversas realidades.",
        "Literatura": "A literatura é um reflexo da sociedade, nos permitindo explorar a mente humana, passando por clássicos da literatura até novas tendências literárias contemporâneas.",
        "Música": "A música é uma linguagem universal que transcende barreiras culturais, com diferentes estilos capazes de tocar os corações das pessoas em qualquer parte do mundo.",
        "Filosofia": "A filosofia busca compreender a essência da vida, questões como moralidade, existência, liberdade e conhecimento são discutidas através dos tempos por grandes pensadores.",
        "Esportes": "O esporte é mais do que uma competição. Ele une pessoas, promove saúde física e mental e nos ensina importantes lições sobre perseverança e trabalho em equipe.",
        "Culinária": "A culinária é uma arte e ciência ao mesmo tempo, onde a combinação de sabores e texturas nos oferece uma experiência sensorial única, refletindo diferentes culturas."
    }

    topic = random.choice(topics)
    return f"Tópico: {topic}\nConteúdo: {content[topic]}\n"


def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("O caminho da pasta não existe!")
            return [], []

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        files_sorted = sorted(files)

        files_by_date = sorted(files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)

        return files_sorted, files_by_date

    except Exception as e:
        print(f"Erro ao organizar arquivos: {e}")
        return [], []


def display_files_in_window(files_sorted, files_by_date, folder_path):

    root = tk.Tk()
    root.title("Arquivos Organizados")

    root.geometry("600x675")

    label1 = tk.Label(root, text="Arquivos organizados alfabeticamente (A-Z):", font=("Arial", 14))
    label1.pack(pady=10)

    listbox1 = tk.Listbox(root, width=70, height=15)
    for file in files_sorted:
        listbox1.insert(tk.END, file)
    listbox1.pack(pady=10)

    label2 = tk.Label(root, text="Arquivos organizados por data de modificação:", font=("Arial", 14))
    label2.pack(pady=10)

    listbox2 = tk.Listbox(root, width=70, height=15)
    for file in files_by_date:
        mod_time = datetime.fromtimestamp(os.path.getmtime(os.path.join(folder_path, file)))
        listbox2.insert(tk.END, f"{file} - Última modificação: {mod_time}")
    listbox2.pack(pady=10)

    close_button = tk.Button(root, text="Fechar", command=root.quit)
    close_button.pack(pady=10)

    root.mainloop()


def main():
    # Abrir o diálogo de seleção de pasta
    folder_path = filedialog.askdirectory(title="Selecione a pasta para organizar os arquivos")

    if not folder_path:
        print("Nenhuma pasta selecionada!")
        return

    # Gerar conteúdo de IA
    ai_content = generate_ai_content()
    ai_filename = "conteudo_gerado_com_ia.txt"
    ai_file_path = os.path.join(folder_path, ai_filename)

    try:
        with open(ai_file_path, 'w') as ai_file:
            ai_file.write(ai_content)
        print(f"\nConteúdo gerado com IA foi salvo no arquivo: {ai_filename}")
    except Exception as e:
        print(f"Erro ao salvar o conteúdo gerado com IA: {e}")

    # Organizar os arquivos na pasta escolhida
    files_sorted, files_by_date = organize_files(folder_path)

    # Exibir arquivos na interface gráfica
    display_files_in_window(files_sorted, files_by_date, folder_path)


if __name__ == "__main__":
    main()
