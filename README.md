# ✝️ IA_Catequista

Um chatbot de inteligência artificial projetado para atuar como um **catequista virtual católico**, ensinando o Evangelho de forma clara, acolhedora e fiel à doutrina da Igreja.

---

## 🧠 Sobre o Projeto

O **IA_Catequista** é um assistente conversacional baseado em IA que responde perguntas sobre fé, espiritualidade e ensinamentos da Igreja Católica.

Seu principal objetivo é:

* 📖 Explicar o Evangelho de forma simples e acessível
* 💬 Acolher dúvidas espirituais com empatia
* 🧑‍🏫 Ensinar doutrina católica com fidelidade
* 🙏 Incentivar reflexão e crescimento espiritual

---

## ⚙️ Tecnologias Utilizadas

* **Python**
* **Ollama** → execução local de modelos de linguagem (LLM)
* **Agno Framework** → criação de agentes inteligentes
* **ChromaDB** → banco de dados vetorial
* **Embeddings via Ollama**

---

## 🧩 Arquitetura

O sistema é composto por três pilares principais:

### 1. 🤖 Agente Inteligente

Responsável por interpretar perguntas e gerar respostas com base em um prompt altamente estruturado.

### 2. 📚 Base de Conhecimento (RAG)

* Documentos armazenados na pasta `knowledge/`
* Indexados em um banco vetorial (ChromaDB)
* Recuperados dinamicamente para enriquecer respostas

### 3. 🧠 Modelo de Linguagem

* Executado localmente via Ollama
* Modelo configurado: `granite4-UNCENSORED`

---

## ✨ Diferenciais

* 💬 **Tom pastoral e acolhedor**
* 📖 **Fidelidade à doutrina católica**
* 🧠 **Uso de RAG (Retrieval-Augmented Generation)**
* 🔒 **Execução local (mais privacidade)**
* 🎓 **Foco educacional e espiritual**

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

* Python 3.10+
* Ollama instalado

Instale o Ollama:
👉 https://ollama.com

---

### 2. Instalar dependências

```bash
pip install agno chromadb
```

---

### 3. Baixar os modelos necessários

```bash
ollama pull embeddinggemma
ollama pull jayeshpandit2480/granite4-UNCENSORED
```

---

### 4. Preparar a base de conhecimento

Crie a pasta:

```bash
mkdir knowledge
```

Adicione arquivos com conteúdo religioso (ex: textos bíblicos, catecismo, estudos, etc.)

---

### 5. Executar

```bash
python main.py
```

---

### 💬 Uso

* O programa inicia com uma apresentação automática
* Digite suas perguntas no terminal
* Para sair, digite:

```bash
bye
```

---

## 🧪 Exemplo de Interação

```text
-> O que é pecado?
"O pecado é tudo aquilo que nos afasta do amor de Deus..."
```

---

## 📁 Estrutura do Projeto

```bash
IA_Catequista/
├── main.py
├── knowledge/
│   ├── documentos.txt
```

---

## ⚠️ Limitações

* Interface apenas via terminal (CLI)
* Dependência de configuração manual do Ollama
* Sem validação automática das fontes religiosas
* Sem autenticação ou persistência de usuários

---

## 🔧 Melhorias Futuras

* 🌐 Interface web (Streamlit ou React)
* 📱 Aplicação mobile
* 🔎 Melhor curadoria da base de conhecimento
* 🧾 Logs de conversas
* 🌍 Suporte a múltiplos idiomas
* ✝️ Expansão para outros conteúdos teológicos

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/minha-feature`)
3. Commit suas alterações
4. Abra um Pull Request

---

## 📜 Licença

Este projeto ainda não possui uma licença definida.

---

## 🙏 Observação

Este projeto tem finalidade **educacional e espiritual**.
As respostas devem ser interpretadas como apoio à reflexão e não substituem orientação pastoral oficial.

---

## ❤️ Autor

Desenvolvido por [@dvsalvaya](https://github.com/dvsalvaya)
