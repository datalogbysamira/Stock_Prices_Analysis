# ==========================================
3. Stock Prices Analysis Project Structure  
# ==========================================

# Create project root
mkdir Stock_Prices_Analysis

# Move into project
cd Stock_Prices_Analysis

# ==========================================
# Create folders
# ==========================================

mkdir data
mkdir data\raw
mkdir data\cleaned
mkdir data\processed

mkdir docs

mkdir reports
mkdir reports\figures
mkdir reports\tables

mkdir scripts
mkdir scripts\level_1
mkdir scripts\level_2
mkdir scripts\level_3
mkdir scripts\utils

mkdir outputs

# ==========================================
# Root files
# ==========================================

New-Item README.md -ItemType File
New-Item requirements.txt -ItemType File
New-Item LICENSE -ItemType File
New-Item .gitignore -ItemType File
New-Item config.py -ItemType File

# ==========================================
# Documentation
# ==========================================

New-Item docs\project_requirements.md -ItemType File
New-Item docs\data_schema.md -ItemType File
New-Item docs\kpi_table.md -ItemType File
New-Item docs\analysis_summary.md -ItemType File
New-Item docs\notes.md -ItemType File

# ==========================================
# Reports
# ==========================================

New-Item reports\final_report.md -ItemType File

# ==========================================
# Level 1 Scripts
# ==========================================

New-Item scripts\level_1\01_data_cleaning.py -ItemType File
New-Item scripts\level_1\02_eda.py -ItemType File
New-Item scripts\level_1\03_visualization.py -ItemType File

# ==========================================
# Level 2 Scripts
# ==========================================

New-Item scripts\level_2\04_regression.py -ItemType File

# ==========================================
# Level 3 Scripts
# ==========================================

New-Item scripts\level_3\05_dashboard.py -ItemType File

# ==========================================
# Utility Modules (Reusable)
# ==========================================

New-Item scripts\utils\__init__.py -ItemType File
New-Item scripts\utils\helpers.py -ItemType File
New-Item scripts\utils\plotting.py -ItemType File
New-Item scripts\utils\validation.py -ItemType File

# ==========================================
# Output Placeholders
# ==========================================

New-Item outputs\cleaned_dataset.csv -ItemType File
New-Item outputs\predictions.csv -ItemType File
New-Item outputs\metrics.json -ItemType File

Write-Host ""
Write-Host "========================================="
Write-Host " Stock_Prices_Analysis Project Created "
Write-Host "========================================="


# ==========================================
4. Set up the development environment 
# ==========================================

# Create a Virtual Environment
python -m venv .venv
# Activate it 
.venv\Scripts\activate
# Upgrade pip
python -m pip install --upgrade pip
# Libraries needed
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels jupyter openpyxl pyarrow
# Freeze Requirements
pip freeze > requirements.txt

# Python virtual environment folder .venv, add this to your .gitignore

# Virtual environments
.venv/
venv/
env/
ENV/

# Python cache
__pycache__/
*.py[cod]

# Jupyter Notebook
.ipynb_checkpoints/

# Environment variables / secrets
.env

# VS Code
.vscode/

# Python distribution
build/
dist/
*.egg-info/

# OS files
.DS_Store
Thumbs.db


# ==========================================
5. GitHub repository creation
# ==========================================

# Initialize the Git Repository
git init
# Check Repository Status
git status
# Create .gitignore
# Check Ignored Files
git status
# Stage All Files
git add .
# Create the First Commit
git commit -m "Initial project structure and environment setup"
# Create GitHub Repository
# Connect Local Repository to GitHub
git remote add origin https://github.com/datalogbysamira/HousePredictionAnalytics.git

git remote -v

# Push the Project
git branch -M main

git push -u origin main



