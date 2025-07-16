from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts import SemanticSimilarityExampleSelector # Assuming this is available from previous function

def setup_few_shot_prompt_template(example_selector: SemanticSimilarityExampleSelector):
    """
    Sets up and returns a FewShotPromptTemplate instance for SQL generation.

    Args:
        example_selector (SemanticSimilarityExampleSelector): The example selector
                                                            to use for picking few-shot examples.

    Returns:
        FewShotPromptTemplate: An initialized FewShotPromptTemplate object.
    """
    print("--- Defining Example Prompt Template ---")
    # Define a template for formatting each individual few-shot example.
    # It specifies how a single (Question, SQLQuery, SQLResult, Answer) tuple
    # should be presented within the overall prompt to the LLM.
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}"
    )
    print("Example prompt template defined.")

    print("--- Creating FewShotPromptTemplate Instance ---")
    # Define the prefix and suffix for the overall prompt.
    # These are standard components from LangChain's SQL chain prompts for MySQL.
    # `_mysql_prompt` typically sets up the context for MySQL SQL generation.
    # `PROMPT_SUFFIX` usually contains the placeholder for the user's new question.
    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector, # Uses the semantic similarity selector to pick examples.
        example_prompt=example_prompt,     # Defines how each selected example is formatted.
        prefix=_mysql_prompt,              # The introductory text before examples.
        suffix=PROMPT_SUFFIX,              # The concluding text after examples, containing the new question placeholder.
        input_variables=["input", "table_info", "top_k"], # Variables expected by the final prompt.
        # `input`: The user's new natural language question.
        # `table_info`: The database schema information.
        # `top_k`: (Optional) A parameter for top-k results in SQL.
    )
    print("FewShotPromptTemplate created.")
    return few_shot_prompt

# --- How you would use this function in your main script: ---

# Assuming `example_selector` is already initialized from `setup_vectorstore_and_selector`
# few_shot_prompt = setup_few_shot_prompt_template(example_selector)