from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from langchain_community.vectorstores import Chroma
from langchain.prompts import SemanticSimilarityExampleSelector

def initialize_huggingface_embeddings(model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
    """
    Initializes and returns a HuggingFaceEmbeddings model.

    Args:
        model_name (str): The name of the SentenceTransformer model to load.

    Returns:
        HuggingFaceEmbeddings: An initialized HuggingFaceEmbeddings object.
                                Exits the program if the model cannot be loaded.
    """
    print(f"--- Initializing HuggingFace Embedding Model: '{model_name}' ---")
    try:
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        print(f"HuggingFace Embedding Model '{model_name}' loaded successfully.")
        return embeddings
    except Exception as e:
        print(f"Error loading HuggingFace embedding model: {e}")
        print("Please ensure 'langchain-huggingface' is installed: pip install -U langchain-huggingface")
        print("Exiting program as embeddings are critical for functionality.")
        exit()


def setup_vectorstore_and_selector(few_shot_examples: list, embeddings: HuggingFaceEmbeddings, k_examples: int = 2):
    """
    Sets up the Chroma vector store and SemanticSimilarityExampleSelector.

    Args:
        few_shot_examples (list): A list of dictionaries, where each dict is a few-shot example.
        embeddings (HuggingFaceEmbeddings): An initialized HuggingFaceEmbeddings object.
        k_examples (int): The number of most similar examples to retrieve using the selector.

    Returns:
        SemanticSimilarityExampleSelector: An initialized example selector.
    """
    print("--- Creating Chroma Vector Store for Few-Shot Examples ---")
    # Prepare the text data for vectorization.
    # It concatenates all string values from each dictionary in few_shot_examples
    # into a single string for each example. This combined string will be embedded.
    to_vectorize = ["".join(example.values()) for example in few_shot_examples]

    # Create a Chroma vector store from the prepared text data.
    # - `to_vectorize`: The list of strings to be embedded and stored.
    # - `embedding`: The embedding model (HuggingFaceEmbeddings instance) used to convert text to vectors.
    # - `metadatas`: A list of dictionaries (your original few_shot_examples)
    #                that will be associated with each embedded text.
    #                This allows you to retrieve the original question, SQL query, etc.,
    #                when a similar query is made.
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shot_examples)
    print("Chroma vector store created.")

    print(f"--- Setting up Semantic Similarity Example Selector (k={k_examples}) ---")
    # Initialize the example selector.
    # - `vectorstore`: The Chroma vector store containing your embedded few-shot examples.
    # - `k`: The number of most similar examples to retrieve.
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=k_examples
    )
    print("Example selector initialized.")
    return example_selector

# The commented-out usage examples below should also be at the top level (no indentation)
# --- How you would use these functions in your main script: ---

# 1. Initialize embeddings
# embeddings = initialize_huggingface_embeddings()

# 2. Load few-shot examples (assuming load_few_shot_examples is defined elsewhere or few_shot_examples is directly available)
# few_shot_examples = load_few_shot_examples() # Or directly use your 'few_shots' list if it's in scope

# 3. Setup vector store and example selector
# example_selector = setup_vectorstore_and_selector(few_shot_examples, embeddings, k_examples=2)