# alimentar_base.py
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from app.ai.retriever import get_knowledge_base


def main():
    knowledge_base = get_knowledge_base()
    folder = "knowledge"

    # 1. Procura dinamicamente por qualquer .txt na pasta (e ignora os chunks já criados)
    arquivos = [
        f
        for f in os.listdir(folder)
        if f.endswith(".txt") and not f.startswith("chunk_")
    ]

    if not arquivos:
        print("✨ Nenhum arquivo novo para processar em 'knowledge'.")
        return

    # 2. Processa cada arquivo encontrado de forma independente
    for arquivo in arquivos:
        caminho_original = os.path.join(folder, arquivo)
        nome_base = os.path.splitext(arquivo)[0]  # Ex: "catecismo" ou "biblia"

        print(f"\n📖 Lendo arquivo dinamicamente: {arquivo}")

        with open(caminho_original, "r", encoding="utf-8") as f:
            texto = f.read()

        # 3. Lógica inteligente para não cortar parágrafos ao meio
        paragrafos = texto.split("\n")
        blocos = []
        bloco_atual = []
        tamanho_atual = 0

        for p in paragrafos:
            if tamanho_atual + len(p) > 3000 and bloco_atual:
                blocos.append("\n".join(bloco_atual))
                bloco_atual = [p]
                tamanho_atual = len(p)
            else:
                bloco_atual.append(p)
                tamanho_atual += len(p)

        if bloco_atual:
            blocos.append("\n".join(bloco_atual))

        total = len(blocos)
        print(f"Dividido em {total} blocos sem quebrar parágrafos.")

        # 4. Grava os blocos e envia para o banco com o contador funcional
        for n, bloco in enumerate(blocos, 1):
            # O nome do chunk agora muda de acordo com o arquivo original automaticamente
            nome_chunk = f"{folder}/chunk_{nome_base}_{n}.txt"

            with open(nome_chunk, "w", encoding="utf-8") as f_temp:
                f_temp.write(bloco)

            print(f"[{n}/{total}] Vetorizando: {nome_chunk}...")

            # O skip_if_exists garante que o Ollama pule os que já foram feitos antes
            knowledge_base.insert(path=nome_chunk, skip_if_exists=True)

    print("\n🏆 Sucesso! Todos os arquivos da pasta foram processados.")


if __name__ == "__main__":
    main()