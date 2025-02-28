# -*- coding: utf-8 -*-
"""MedicalSummary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FmamGu_jB5gRoB2OjH67-Xh3t1gUBQzd
"""

import torch
from transformers import AutoModelForCausalLM, BioGptTokenizer, Trainer, TrainingArguments, T5Tokenizer, T5ForConditionalGeneration
from datasets import load_dataset, Dataset
import pandas as pd
import sacremoses
import re

# Load tokenizer and model
model_name = "t5-small"  # Options: "t5-small", "t5-base", "microsoft/biogpt"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Load MIMIC-IV Dataset (Ensure you have access)
data = pd.read_csv("mimic_iv_summarization_dataset.csv")

# Data Cleaning & Preprocessing
def clean_text(text):
    text = re.sub(r'[^a-zA-Z0-9., ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data['text'] = data['text'].apply(clean_text)
data['summary'] = data['summary'].apply(clean_text)

dataset = Dataset.from_pandas(data[['text', 'summary']])

def preprocess_function(examples):
    # Tokenize input text
    model_inputs = tokenizer(
        examples["text"],
        padding="max_length",
        truncation=True,
        max_length=512
    )

    # Tokenize labels
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(
            examples["summary"],
            padding="max_length",
            truncation=True,
            max_length=128
        )

    # Ensure no empty labels
    if "input_ids" in labels:
        labels["input_ids"] = [
            [(token if token != tokenizer.pad_token_id else -100) for token in label]
            for label in labels["input_ids"]
        ]

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# ✅ Step 1: Split dataset
dataset_split = dataset.train_test_split(test_size=0.1)
train_dataset = dataset_split["train"]
eval_dataset = dataset_split["test"]

# ✅ Step 2: Apply preprocessing
train_dataset = train_dataset.map(preprocess_function, batched=True)
eval_dataset = eval_dataset.map(preprocess_function, batched=True)

# ✅ Step 3: Optimized Training Arguments
training_args = TrainingArguments(
    output_dir="./summarization_model",
    evaluation_strategy="epoch",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    save_total_limit=2,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs"
)


# ✅ Step 4: Trainer with Early Stopping
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
)

## a37747e6c4e4712dcb83dcc03e713268a43b0db9

# ✅ Step 5: Train Model
trainer.train()


# ✅ Save Model and Tokenizer LOCALLY
model_save_path = "medical_summary_model" 
model.save_pretrained(model_save_path)
tokenizer.save_pretrained(model_save_path)
print(f"✅ Model and tokenizer saved to {model_save_path}")


