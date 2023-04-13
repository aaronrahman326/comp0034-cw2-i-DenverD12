"""File for basic html front-end routes, NOTE: NOT required as individual."""
from flask import render_template, Blueprint, abort
from tourism_hotels_app.utilities import get_countries, get_country


# Define the Blueprint for basic html front-end
html_display_bp = Blueprint("main", __name__)


@html_display_bp.route("/")
def index():
    """
    HTTP GET request route that returns home page html template.

    Args:
        None
    Returns:
        Returns the home page with a list of available countries.
    """
    response = get_countries()
    return render_template("index.html", country_list=response)


@html_display_bp.route("/display_country/<Country_Name>")
def display_country(Country_Name):
    """
    HTTP GET request route that returns jinja html template of each country.

    Args:
        Country_Name: Name of a specific country entered as URI
        or from choosing a country from the home page.
    Returns:
        Returns details page with a basic summary of each country.
    """
    current_country = get_country(Country_Name)
    if current_country:
        return render_template(
            "country_summary_display.html",
            country=current_country
        )
    else:
        abort(404)
