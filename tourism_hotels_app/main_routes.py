from flask import render_template, Blueprint, abort
from tourism_hotels_app.utilities import get_countries, get_country

# Define the Blueprint
main_bp = Blueprint("main", __name__)


# @main_bp.errorhandler(500)
# def internal_server_error(e):
#     """Custom error message for Internal Server Error status code 500"""
#     return render_template("500.html"), 500


# @main_bp.errorhandler(404)
# def page_not_found(e):
#     """Custom error message for Not Found error with status code 404"""
#     return render_template("404.html"), 404


@main_bp.route("/")
def index():
    """Returns the home page"""
    response = get_countries()
    return render_template("index.html", country_list=response)


@main_bp.route("/display_country/<Country_Name>")
def display_country(Country_Name):
    """Returns the country detail page"""
    current_country = get_country(Country_Name)
    if current_country:
        return render_template("event.html", country=current_country)
    else:
        abort(404)
