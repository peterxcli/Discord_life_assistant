from enum import Flag
import torch
import os

corpus_name = "cornell movie-dialogs corpus"
corpus = os.path.join("cmds\cmdsBase\chatBase\data", corpus_name)

# Define path to new file
datafile = os.path.join(corpus, "formatted_movie_lines.txt")

save_dir = os.path.join("cmds\cmdsBase\chatBase\data", "save")

# Default word tokens
PAD_token = 0  # Used for padding short sentences
SOS_token = 1  # Start-of-sentence token
EOS_token = 2  # End-of-sentence token


MAX_LENGTH = 15  # Maximum sentence length to consider

MIN_COUNT = 1    # Minimum word count threshold for trimming

# USE_CUDA = False
USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")

# Configure models
model_name = 'cb_model'
attn_model = 'dot'
#attn_model = 'general'
#attn_model = 'concat'
hidden_size = 700
encoder_n_layers = 2
decoder_n_layers = 2
dropout = 0.1
batch_size = 64

checkpoint_iter = 60000 #load pre-train model's current iter

# Configure training/optimization
clip = 50.0
teacher_forcing_ratio = 1.0
learning_rate = 0.0001
decoder_learning_ratio = 2.0
n_iteration = 80000
print_every = 10
save_every = 5000











