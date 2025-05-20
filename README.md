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
