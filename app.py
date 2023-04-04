import strawberry
from Models import Query
from strawberry.asgi import GraphQL
from strawberry.flask import graphiql

from flask import Flask, jsonify, request, render_template
from strawberry.flask.views import GraphQLView
# from strawberry.flask.views import AsyncGraphQLView

app = Flask(__name__, template_folder='Templates')

schema = strawberry.Schema(query=Query)

@app.route("/graphql", methods=["POST"])
def graphql():
    
    query = request.form.get('query')

    result = schema.execute_sync(query=query)

    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, host='0.0.0.0', debug=True)