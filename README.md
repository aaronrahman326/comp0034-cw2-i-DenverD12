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
# **ADDITIONAL INSTRUCTIONS WHEN MARKING**   
- ### **Please note, I did not have time to implement a delete file, therefore I provided a backup of the database in the folder called `MOVE_backup_of_database_when_marking`.**  
- ### **So when you use POSTMAN to test the `PATCH` and `POST` routes, after each one/iteration is tested, `delete` the main version of the database `tourism_hotels.db` in folder `tourism_hotels_app/data` first. Then make sure to `COPY` the same named database from the `MOVE_backup_of_database_when_marking` folder to the main data folder each time.**
- ### **Do the same as above if you are doing pytest testing for each function, if individually. Essentially, any test that updates or inputs data to mock a country added or if anything is added to database, after that test, delete the database in data and copy and paste the backup. Thank you.**

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
