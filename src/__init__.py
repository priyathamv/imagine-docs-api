import json
from enum import Enum

from flask import Flask
from flask_cors import CORS

from src.blueprint import register_blueprints
from src.containers import Container
from src.exception import global_exception_handler


# Application Factory
def create_app():
    app = Flask(__name__)

    # Enabling CORS for all routes
    CORS(app)

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
    @app.errorhandler(Exception)
    def error_handler(error):
        return global_exception_handler(error)

# from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader, LLMPredictor, ServiceContext
# from langchain import OpenAI
# import os


# os.environ['OPENAI_API_KEY'] = ''

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
