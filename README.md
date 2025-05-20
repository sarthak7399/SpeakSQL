# 🔹 `Ask2SQL`

---

## 🧾 About 
Convert natural language questions into SQL queries using GenAI. Powered by Mistral via Ollama, HuggingFace models, and Streamlit UI, backed by ChromaDB and MySQL.

---

## 📘 Description
**Ask2SQL** is an intelligent GenAI-powered tool that takes basic user questions like *“Show top 5 customers by sales”* or *“What were the total t-shirt sales last week?”* and converts them into valid SQL queries.

This version is tailored for a **small retail t-shirt store**, helping store managers and staff analyse their business without needing SQL knowledge. From tracking inventory levels to viewing best-selling designs, Ask2SQL provides instant answers.

The app leverages **Mistral 7B (running locally via Ollama)** or **HuggingFace Transformers** for natural language understanding, **ChromaDB** for storing schema embeddings and contextual memory, and **MySQL** as the backend database storing retail sales data. The frontend is built using **Streamlit** for a lightweight and responsive user interface.

It is ideal for small business owners, sales analysts, or support staff to interact with their data effortlessly using plain English.

---

## ⚙️ Setup Instructions

### 🔧 1. Create a Virtual Environment
```bash
python3 -m venv SpeakSQLenv
source SpeakSQLenv/bin/activate   # On Linux/Mac
SpeakSQLenv\Scripts\activate      # On Windows
deactivate # To deactivate the virtual environment
```

### 📦 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🗄️ 3. Install MySQL on Linux (Ubuntu/WSL)
```bash
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql
sudo mysql_secure_installation
```
✅ Create a MySQL database and table manually or via SQL script from path '''../Database/create_db.sql'''. Make sure to note DB name, user, password, host, and port.

### 🔐 4. Setup .env File
Please refer to .env.example. After putting the keys, please remove .example from the file name.

### 🤖 5. Install & Setup Ollama with Mistral
🧱 Install Ollama (One-time)
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

⬇️ Pull Mistral Model (approx 4.1 GB)
```bash
ollama pull mistral
```
Ollama will serve Mistral locally at http://localhost:11434

### 🧪 6. Running the Jupyter Notebook Code
Activate your virtual environment before starting Jupyter, and run the below command.
```bash
jupyter-notebook
```

### 📝 Points to be noted

1. Ensure MySQL service is running before executing queries.
2. Ideal for Linux/WSL setups. For Windows, WSL is recommended.