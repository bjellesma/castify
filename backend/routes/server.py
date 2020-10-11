from flask import Blueprint, render_template

server_routes = Blueprint('server_routes', __name__)


@server_routes.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')
