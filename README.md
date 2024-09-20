# POS Tagging using HMM and CRF with the Brown Dataset

This repository demonstrates how to perform Part-of-Speech (POS) tagging using Hidden Markov Models (HMM) and Conditional Random Fields (CRF) based on the Brown dataset. The project includes the implementation of both models, evaluation metrics, and a Streamlit application to visualize tagging results.

## Table of Contents
1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
   - [Training HMM](#training-hmm)
   - [Training CRF](#training-crf)
   - [Evaluation](#evaluation)
5. [Evaluation Metrics](#evaluation-metrics)
6. [Streamlit Application](#streamlit-application)

## Introduction

POS tagging is the process of assigning a part of speech to each word in a sentence. This project implements two popular approaches for POS tagging:

- **Hidden Markov Model (HMM)**: A probabilistic model that relies on the Markov assumption and the chain rule of probability.
- **Conditional Random Field (CRF)**: A discriminative model that allows for flexible feature engineering, useful for POS tagging.

The Brown dataset is used as the corpus for training and testing these models.

## Requirements

The following Python packages are required for running the project:

- Python 3.8+
- `nltk`
- `numpy`
- `sklearn-crfsuite`
- `scikit-learn`
- `Streamlit`
- `matplotlib`

You can install the required packages by running:
```bash
pip install -r requirements.txt
