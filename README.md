# COMP0034 Coursework 2 README

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 

<br/>

# **Set-up Instructions**
1. First create a new terminal, then create, setup and activate a virtual environment.
2. In the terminal run the code: `pip install -e to install` all the packages and dependencies from setup.py. 
3. If the dependencies do not work for any reason, in the terminal, run the code: `pip install -r requirements.txt` to install dependencies/required libraries.
4. Now to run the flask app, it can be run in 3 configuration modes:  
   - Base Configuration (Config) Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.Config')" run`
   - Development Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.DevelopmentConfig')" run `
   - Testing Config Mode: Run the code: `flask --app "tourism_hotels_app:create_app('tourism_hotels_app.config.TestConfig')" run`

# **URL to my GitHub repository**
**https://github.com/ucl-comp0035/comp0034-cw2-i-DenverD12**