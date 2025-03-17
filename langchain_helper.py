from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os

# Use Mistral AI API Key
from secret_key import mistral_api_key  

os.environ['OPENAI_API_KEY'] = mistral_api_key  # Mistral uses OpenAI-compatible API

# Configure Chat Model with Mistral API
llm = ChatOpenAI(
    model="mistral-small-latest",  # Choose an appropriate model: mistral-small, mistral-medium, etc.
    temperature=0.7,
    openai_api_base="https://api.mistral.ai/v1"  # Set Mistral API Base URL
)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1: Restaurant Name
    prompt_template_name = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in naming restaurants."),
        ("human", "I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.")
    ])

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = ChatPromptTemplate.from_messages([
        ("system", "You are an expert chef."),
        ("human", "Suggest some popular menu items for {restaurant_name}. Return them as a comma-separated list.")
    ])

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential Chain Execution
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
