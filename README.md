# 📁 Project Setup Guide

This document outlines the steps to set up the project environment, install dependencies, initialize version control, and understand the required tools and services.

---

## 🚀 Getting Started

### 1. Create Project Folder and Setup Environment

```bash
# Create a new project folder
mkdir <project_folder_name>

# Move into the project folder
cd <project_folder_name>

# Open the folder in VS Code
code .

# Create a new Conda environment with Python 3.10
conda create -p <env_name> python=3.10 -y

# Activate the environment (use full path to the environment)
conda activate <path_of_the_env>

# Install dependencies from requirements.txt
pip install -r requirements.txt
