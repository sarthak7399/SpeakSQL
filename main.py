import streamlit as st
import os
import sys

# Add the parent directory to the Python path to allow importing from speakSQL.py
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# --- Import the main chain initialization function ---
try:
    from speakSQL import get_few_shot_sql_chain
except ImportError as e:
    st.error(f"🚨 Setup Error: Could not load the core SpeakSQL logic. Details: {e}")
    st.info("💡 Please ensure 'speakSQL.py' is in the same directory and all its internal modules are correctly imported.")
    st.stop()

# --- Cache the SQL chain initialization for performance ---
@st.cache_resource
def load_chain_once():
    """Loads and caches the SQLDatabaseChain to run only once."""
    try:
        chain = get_few_shot_sql_chain()
        return chain
    except Exception as e:
        st.error(f"❌ Initialization Failed: Cannot connect to database or load AI model. Error: {e}")
        st.info("🔍 Double-check your `.env` file, database connection, and Google API key.")
        st.stop()

# --- Load the chain ---
sql_chain = load_chain_once()

# --- Streamlit App UI ---
st.set_page_config(page_title="SpeakSQL 🤖", layout="centered")

st.title("🗣️ SpeakSQL")
st.markdown("""
Unleash the power of AI to query your database with plain English!
Type your question below and hit 'Ask' or simply press **Enter**! 🚀
""")

# --- Use st.form to enable Enter key submission ---
with st.form(key='sql_query_form'):
    user_question = st.text_input("❓ Your Question:", placeholder="e.g., How many Nike t-shirts are in stock for size M and color blue?")
    submit_button = st.form_submit_button("Ask 💬")

# Check if the form was submitted (either by button click or Enter key)
if submit_button:
    if user_question:
        with st.spinner("Processing your request... ⏳"):
            try:
                response = sql_chain.invoke({"query": user_question})

                st.subheader("✅ Answer:")
                if isinstance(response, dict) and 'result' in response:
                    st.success(response['result'])
                else:
                    st.success(response)

                st.success("Query successful!")

            except Exception as e:
                error_message = str(e)
                st.error(f"💥 Query Failed: {error_message}")

                if "quota" in error_message.lower() or "resourceexhausted" in error_message.lower():
                    st.warning("⚠️ API Quota Exceeded! Please wait a while or consider upgrading your Google Gemini plan.")
                elif "mysql" in error_message.lower() or "database" in error_message.lower():
                    st.warning("⚠️ Database Error: Check your database connection details or the generated SQL query for issues.")
                else:
                    st.warning("🧐 An unexpected error occurred. Check the terminal for detailed logs.")
    else:
        st.warning("✍️ Please type your question before clicking 'Ask' or pressing Enter!")

st.markdown("---")
st.markdown("✨ Powered by Google Gemini, LangChain, and HuggingFace Embeddings.")