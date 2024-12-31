import os


class Config:
    # General configuration
    DEBUG = os.getenv('DEBUG', 'True') == 'True'

    # OpenAI API Key
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_api_key_here')

    # Azure settings
    AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING',
                                                'your_azure_storage_connection_string_here')

    # Other configurations can be added as needed