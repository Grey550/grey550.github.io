#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Activities"""
from models.activity import Activity
from models import storage
from api.v1.pages import app_pages
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_pages.route('/activities', methods=['GET'], strict_slashes=False)
@swag_from('documentation/activity/all_activities.yml')
def get_activities():
    """
    Retrieves a list of all activities
    """
    all_activities = storage.all(Activity).values()
    list_activities = []
    for activity in all_activities:
        list_activities.append(activity.to_dict())
    return jsonify(list_activities)


@app_pages.route('/activities/<activity_id>/', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/activity/get_activity.yml', methods=['GET'])
def get_activity(activity_id):
    """ Retrieves an activity """
    activity = storage.get(Activity, activity_id)
    if not activity:
        abort(404)

    return jsonify(activity.to_dict())


@app_pages.route('/activities/<activity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/activity/delete_activity.yml', methods=['DELETE'])
def delete_activity(activity_id):
    """
    Deletes an activity  Object
    """

    activity = storage.get(Activity, activity_id)

    if not activity:
        abort(404)

    storage.delete(activity)
    storage.save()

    return make_response(jsonify({}), 200)


@app_pages.route('/activities', methods=['POST'], strict_slashes=False)
@swag_from('documentation/activity/post_activity.yml', methods=['POST'])
def post_activity():
    """
    Creates an activity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Activity(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_pages.route('/activities/<activity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/activity/put_activity.yml', methods=['PUT'])
def put_activity(activity_id):
    """
    Updates an activity
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    activity = storage.get(Activity, activity_id)

    if not activity:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(activity, key, value)
    storage.save()
    return make_response(jsonify(activity.to_dict()), 200)
