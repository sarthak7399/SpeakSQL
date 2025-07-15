from langchain_google_genai import ChatGoogleGenerativeAI
from Modules.loadDatabase import initialize_database
from Modules.loadSQLChain import initialize_sql_database_chain
from Modules.loadEmbeddings import initialize_huggingface_embeddings, setup_vectorstore_and_selector
from Modules.loadFewShots import load_few_shot_examples
from Modules.loadVariables import load_environment_variables
from Modules.setupPromptTemplate import setup_few_shot_prompt_template # New import for Decimal type handling

# Load environment variables for Google Generative AI
env_vars = load_environment_variables()

GOOGLE_API_KEY = env_vars.get('GOOGLE_API_KEY')

# Initialize Google Generative AI LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=GOOGLE_API_KEY) 

# Load environment variables for database
db_user = env_vars.get('db_user')
db_password = env_vars.get('db_password')
db_host = env_vars.get('db_host')
db_port = env_vars.get('db_port')
db_name = env_vars.get('db_name')
# Initialize MySQL Database
db, database_schema = initialize_database(db_user, db_password, db_host, db_port, db_name, wanna_print=False)

# Initialize few-shot examples and HuggingFace embeddings
few_shot_examples = load_few_shot_examples()

# Initialize the embeddings
embeddings = initialize_huggingface_embeddings()

# Setup vector store and example selector
example_selector = setup_vectorstore_and_selector(few_shot_examples, embeddings, k_examples=2)

# Setup few-shot prompt
few_shot_prompt = setup_few_shot_prompt_template(example_selector)

# Initialize SQLDatabaseChain
sql_chain = initialize_sql_database_chain(llm, db, few_shot_prompt, verbose=True)


q1 = "How many tshirts do we have left for Nike in small size and red colour?"
response1 = sql_chain.invoke(q1)
print(response1)
