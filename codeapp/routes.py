# pylint: disable=cyclic-import
"""
File that contains all the routes of the application.
This is equivalent to the "controller" part in a model-view-controller architecture.
In the final project, you will need to modify this file to implement your project.
"""
# built-in imports
import io

# external imports
from flask import Blueprint, jsonify, render_template
from flask.wrappers import Response as FlaskResponse
from matplotlib.figure import Figure
from werkzeug.wrappers.response import Response as WerkzeugResponse

from codeapp.models import Sales

# internal imports
from codeapp.utils import calculate_statistics, get_data_list, prepare_figure

# define the response type
Response = str | FlaskResponse | WerkzeugResponse

bp = Blueprint("bp", __name__, url_prefix="/")


################################### web page routes ####################################


@bp.get("/")  # root route
def home() -> Response:
    dataset: list[Sales] = get_data_list()
    counter: dict[str, float] = calculate_statistics(dataset)
    return render_template("home.html", counter=counter)


@bp.get("/image")
def image() -> Response:
    dataset: list[Sales] = get_data_list()
    counter: dict[str, float] = calculate_statistics(dataset)
    # creating the plot
    fig = Figure()
    fig.gca().bar(
        list(sorted(counter.keys())),
        [counter[x] for x in sorted(counter.keys())],
        color="skyblue",
        zorder=1,
    )

    fig.gca().set_xlabel("Item type")
    fig.gca().set_ylabel("Average profit")
    fig.gca().set_title("Average profit per Item type")
    ticks = list(sorted(counter.keys()))
    fig.gca().set_xticks(ticks)
    fig.gca().set_xticklabels(list(sorted(counter.keys())), rotation=90)
    fig.tight_layout()

    ################ START -  THIS PART MUST NOT BE CHANGED BY STUDENTS ################
    # create a string buffer to hold the final code for the plot
    output = io.StringIO()
    fig.savefig(output, format="svg")
    # output.seek(0)
    final_figure = prepare_figure(output.getvalue())
    return FlaskResponse(final_figure, mimetype="image/svg+xml")


@bp.get("/about")
def about() -> Response:
    return render_template("about.html")


################################## web service routes ##################################


@bp.get("/json-dataset")
def get_json_dataset() -> Response:
    dataset: list[Sales] = get_data_list()
    return jsonify(dataset)


@bp.get("/json-stats")
def get_json_stats() -> Response:
    dataset: list[Sales] = get_data_list()
    counter: dict[str, float] = calculate_statistics(dataset)
    return jsonify(counter)
