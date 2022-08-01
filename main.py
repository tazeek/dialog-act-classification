from distutils.command.config import config
import os

from dailydialog.Loader import Loader

def prepare_config() -> dict:

    config = {}
    config['current_path'] = os.path.abspath(os.getcwd())

    return config


if __name__ == '__main__':
    
    # Load the dataset
    # Get the dataframe correctly
    # Should be:
    # - Label: inform, question, etc
    # - Utterance: full sentence
    dd_loader = Loader(config['current_path'])

    # Prepare the language model
    # Choice of: XLNet, BERT, ConceptNet, RoBERTa

    # Pre-process the data

    # Create a ML model

    # Portion out the dataset into: train, valid, test

    # Train the model