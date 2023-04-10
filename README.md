# COMP0034 Coursework 2 README

<br/>

# **Set-up Instructions**
1. First create a new terminal, then create, setup and activate a virtual environment.
2. In the terminal run the code: `pip install -e to install` all the packages and dependencies from setup.py. 
3. In the terminal, run the code: `pip install -r requirements.txt` to install dependencies/required libraries.
4. Now to run the flask app, it can be run in 3 configuration modes:  
   - Base Configuration (Config) Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.Config')" run`
   - Development Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.DevelopmentConfig')" run `
   - Testing Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.TestConfig')" run`

# **URL to my GitHub repository**
### **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12**  

<br/>

# **URL to my continuous integration using Github Actions**
### Github Actions link: **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/actions**  
### Workflow .yml file link: **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/actions/runs/4660814109/workflow**
- The continuous integration workflow runs tests using `pytest`, with coverage using `pytest-cov`.  
- It also uses the linters: `flake8` and `pydocstyle`

# **Linters**
### The linters used was `flake8` for code and comments quality and `pydocstyle` for docstrings quality.