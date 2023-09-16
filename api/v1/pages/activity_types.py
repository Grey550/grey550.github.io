#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Activity types"""
from models.activity_type import Activity_Type
from models import storage
from api.v1.pages import app_pages
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_pages.route('/activity_types', methods=['GET'], strict_slashes=False)
@swag_from('documentation/activity_types/all_activity_types.yml')
def get_activity_types():
    """
    Retrieves a list of all activity types
    """
    all_activity_types = storage.all(Activity_Type).values()
    list_activity_types = []
    for activity_type in all_activity_types:
        list_activity_types.append(activity_type.to_dict())
    return jsonify(list_activity_types)


@app_pages.route('/activity_types/<activity_type_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/activity_types/get_activity_type.yml', methods=['GET'])
def get_activity_types(activity_type_id):
    """ Retrieves an activity type """
    activity_type = storage.get(Activity_Type, activity_type_id)
    if not activity_type:
        abort(404)

    return jsonify(activity_type.to_dict())


@app_pages.route('/activity_types/<activity_type_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/activity_types/delete_activity_type.yml',
           methods=['DELETE'])
def delete_activity_types(activity_type_id):
    """
    Deletes an activity type Object
    """

    activity_type = storage.get(Activity_Type, activity_type_id)

    if not activity:
        abort(404)

    storage.delete(activity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_pages.route('/activity_types', methods=['POST'], strict_slashes=False)
@swag_from('documentation/activity_types/post_activity_type.yml', methods=['POST'])
def post_activity_type():
    """
    Creates an activity_type
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Activity_Type(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_pages.route('/activity_types/<activity_type_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/activity_types/put_activity_type.yml', methods=['PUT'])
def put_activity_type(activity_type_id):
    """
    Updates an activity_type
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    activity_type = storage.get(Activity_Type, activity_type_id)

    if not activity_type:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(activity_type, key, value)
    storage.save()
    return make_response(jsonify(activity_type.to_dict()), 200)
