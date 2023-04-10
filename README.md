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
**https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12**