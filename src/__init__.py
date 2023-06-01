from flask import Flask
# import os

from src.blueprints import register_blueprints
from src.containers import Container


# Application Factory
def create_app():
    app = Flask(__name__)

    # Fetching configuration from config.py
    # config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    # app.config.from_object(config_type)

    # Dependency injection container
    container = Container()
    app.container = container

    # Register Blueprints
    register_blueprints(app)

    # Register error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    pass

# from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
# from langchain import OpenAI
# import os


# os.environ['OPENAI_API_KEY'] = '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'

# # num_output: Number of outputs for the LLM
# num_outputs=100

# llm_predictor = LLMPredictor(
#   llm= OpenAI(
#     temperature=0,
#     model_name='text-davinci-002',
#     max_tokens=num_outputs
#   )
# )

# service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# documents = SimpleDirectoryReader('data').load_data()
# index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

# response = index.query('Give me a step by step guide on how can I showcase my work?')

# print(response)
# index = GPTSimpleVectorIndex.load_from_disk('index.json')
