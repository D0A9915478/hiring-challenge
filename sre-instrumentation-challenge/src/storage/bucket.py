from typing import Dict
from flask import Blueprint, jsonify, request, Response
from flask.typing import ResponseReturnValue
from middleware import setup_metrics
import prometheus_client

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

bucket_blueprint = Blueprint("zones", __name__)
setup_metrics(bucket_blueprint)

data: Dict[str, bytes] = {}


@bucket_blueprint.route("/buckets/<id>")
def get_bucket(id: str) -> ResponseReturnValue:
    if id in data.keys():
        return data.get(id), 200, {"Content-Type": "application/octet-stream"}

    return jsonify({"error": "not found"}), 404, {"Content-Type": "application/json"}


@bucket_blueprint.route("/buckets/<id>", methods=["PUT"])
def put_bucket(id: str) -> ResponseReturnValue:
    data[id] = request.get_data()

    return "", 200


@bucket_blueprint.route("/buckets/<id>", methods=["DELETE"])
def delete_bucket(id: str) -> ResponseReturnValue:
    if id in data.keys():
        data.pop(id, None)
        return "", 500

    return jsonify({"error": "bad request"}), 400, {"Content-Type": "application/json"}

@bucket_blueprint.route("/metrics/")
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)