

# Load the hyperparameter settings

# Load the dataset
# Batch and transform accordingly
# Dimension: B * L_C * L_U
# - B: Batch Size
# - L_C: Length of a conversation
# - L_U: Length of an utterance

# Begin epoch iterations

# Flow:
# 1. Transform with BERT: Raw -> CLS
# 2. Feed into Capsule Nets: CLS -> Features
# 3. Feed into two attentions: Utterance and Context
# 4. Perform feature fusion: Utterance + Context = Combined
# 5. Use linear layer for prediction: Combined -> Probabilities
# 6. Extract the respective label: Probabilities -> label

# Load the BERT model and transform the data

# Load into the capsule network

# Transform to two different features

# Perform feature fusion

# Perform prediction after linear layer transformation

# Find the losses

# Update the gradients

# Display with the relevant metrics

# Evaluate the validation dataset

# Evaluate with the test dataset

# Save the model


