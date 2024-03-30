

# Load hyperparameters

# Load the dialog act trained model

# Load the dataset
# Batch and transform accordingly
# Dimension: B * L_C * L_U
# - B: Batch Size
# - L_C: Length of a conversation
# - L_U: Length of an utterance

# Begin epoch iterations

# Flow:
# 1. Transform with BERT: Raw -> CLS
# 2. Separate to two parts: Dialog Act + Emotions
# 3a. Extract the emotion features: CLS -> F_E
# 3b. Extract the dialog act features: CLS -> F_D 
# 4. Combine together: F_E + F_D -> Combined
# 5. Use linear layer for prediction: Combined -> Probabilities
# 6. Extract the respective label: Probabilities -> Label

# Load the BERT model and transform the data

# Extract the dialog act features from the pre-trained model

# Extract the emotion-based features

# Perform feature fusion

# Use linear layer for prediction

# Perform prediction after linear layer transformation

# Find the losses

# Update the gradients

# Display with the relevant metrics

# Evaluate the validation dataset

# Evaluate with the test dataset

# Save the model
