# COMP0034 Coursework 2 README

# **URL to my GitHub repository**
### **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12** 
<br/>

# **SET-UP INSTRUCTIONS**
1. First create a new terminal, then create, setup and activate a virtual environment.
2. In the terminal run the code: `pip install -e to install` all the packages and dependencies from setup.py. 
3. In the terminal, run the code: `pip install -r requirements.txt` to install dependencies/required libraries.
4. Now to run the flask app, it can be run in 3 configuration modes:  
   - Base Configuration (Config) Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.Config')" run`
   - Development Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.DevelopmentConfig')" run `
   - Testing Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.TestConfig')" run` 

<br/>

# **GITHUB ACTIONS URL to my continuous integration**
### Github Actions link: **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/actions**  
### Workflow .yml file link: **https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/actions/runs/4660814109/workflow**
- The continuous integration workflow runs tests using `pytest`, with coverage using `pytest-cov`.  
- It also uses the linters: `flake8` and `pydocstyle`

# **Linters**
- ### The linters used was `flake8` for code and comments quality and `pydocstyle` for docstrings quality.  

- ### Linting evidence can be seen overtime from the various workflows in github actions continuous integration.  

# **TESTING FURTHER EVIDENCE**
### Below is two links to screenshots showing the successful tests and their filepaths:  

### For terminal output of all 25 tests:
- Link to evidence image: https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/blob/main/Testing_Success_evidence_terminal_output_2023-04-12_time_215710.png  

If link doesn't work locate the screenshot in file path:
- `ucl-comp0035/comp0034-cw2-i-DenverD12/Testing_Success_evidence_terminal_output_2023-04-12_time_215710.png  ` 
### For filepaths and all test names showing success in the Testing section:  
- Link to evidence 2 image: https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12/blob/main/Testing_success_evidence_with_filepaths_2023-04-12_time-220722.png   

If link doesn't work locate the screenshot in file path:
- `ucl-comp0035/comp0034-cw2-i-DenverD12/blob/main/Testing_success_evidence_with_filepaths_2023-04-12_time-220722.png   `  
