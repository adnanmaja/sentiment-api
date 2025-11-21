from flask import Blueprint, request, jsonify
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync, ObjectType
from .resolvers import query, resolve_datetime_field, resolve_post_analysis, resolve_post_user


bp = Blueprint('graphql', __name__)

type_defs = load_schema_from_path("src/api/graphql/schema.graphql")

user_type = ObjectType("User")
post_type = ObjectType("Post")
analysis_type = ObjectType("Analysis")

user_type.field("createdAt")(resolve_datetime_field)

post_type.field("createdAt")(resolve_datetime_field)
post_type.field("user")(resolve_post_user)

analysis_type.field("analyzedAt")(resolve_datetime_field)
analysis_type.field("post")(resolve_post_analysis)

schema = make_executable_schema(
        type_defs,
        query,
        user_type,
        post_type,
        analysis_type
    )

# GraphQL playground route (for testing)
@bp.route("/graphql", methods=["GET"])
def graphql_playground():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GraphQL Playground</title>
        <meta charset=utf-8/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/css/index.css"/>
        <link rel="icon" href="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/favicon.png"/>
    </head>
    <body>
        <div id="root"></div>
        <script src="https://cdn.jsdelivr.net/npm/graphql-playground-react/build/static/js/middleware.js"></script>
    </body>
    </html>
    """
    return html, 200

# GraphQL endpoint
@bp.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

