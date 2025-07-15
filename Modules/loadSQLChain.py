from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_community.utilities import SQLDatabase
from langchain.prompts import FewShotPromptTemplate

def initialize_sql_database_chain(
    llm: ChatGoogleGenerativeAI,
    db: SQLDatabase,
    few_shot_prompt: FewShotPromptTemplate,
    verbose: bool = False
):
    """
    Initializes and returns an SQLDatabaseChain instance.

    Args:
        llm (ChatGoogleGenerativeAI): The initialized LangChain-compatible Gemini LLM.
        db (SQLDatabase): The initialized SQLDatabase object.
        few_shot_prompt (FewShotPromptTemplate): The configured FewShotPromptTemplate.
        verbose (bool): If True, the chain's intermediate steps will be printed for debugging.

    Returns:
        SQLDatabaseChain: An initialized SQLDatabaseChain object.
    """
    print(f"--- Initializing SQLDatabaseChain (verbose={verbose}) ---")
    # Create the chain using your LLM, database connection, and the few-shot prompt.
    # Setting verbose=True is great for debugging, as it shows you the intermediate steps.
    sql_chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        verbose=verbose,
        prompt=few_shot_prompt
    )
    print("SQLDatabaseChain initialized.")
    return sql_chain

# --- How you would use this function in your main script: ---

# Assuming llm, db, and few_shot_prompt are already initialized from previous functions:
# llm = ChatGoogleGenerativeAI(...)
# db = SQLDatabase(...)
# few_shot_prompt = setup_few_shot_prompt_template(...)

# sql_chain = initialize_sql_database_chain(llm, db, few_shot_prompt, verbose=True)

