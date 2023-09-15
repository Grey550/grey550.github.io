#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Place - Activity """
from models.place import Place
from models.activity import Activity
from models import storage
from api.v1.pages import app_pages
from os import environ
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_pages.route('places/<place_id>/activities', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/place_activity/get_places_activities.yml',
           methods=['GET'])
def get_place_activities(place_id):
    """
    Retrieves the list of all Activity objects of a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    if environ.get('ZKHP_TYPE_STORAGE') == "db":
        activities = [activity.to_dict() for activity in place.activities]
    else:
        activities = [storage.get(Activity, activity_id).to_dict()
                     for activity_id in place.activity_ids]

    return jsonify(activities)


@app_pages.route('/places/<place_id>/activities/<activity_id>',
                 methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/place_activity/delete_place_activities.yml',
           methods=['DELETE'])
def delete_place_activity(place_id, activity_id):
    """
    Deletes a Activity object of a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    activity = storage.get(Activity, activity_id)

    if not activity:
        abort(404)

    if environ.get('ZKHP_TYPE_STORAGE') == "db":
        if activity not in place.activities:
            abort(404)
        place.activities.remove(activity)
    else:
        if activity_id not in place.activity_ids:
            abort(404)
        place.activity_ids.remove(activity_id)

    storage.save()
    return make_response(jsonify({}), 200)


@app_pages.route('/places/<place_id>/activities/<activity_id>', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/place_activity/post_place_activities.yml',
           methods=['POST'])
def post_place_activity(place_id, activity_id):
    """
    Link a Activity object to a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    activity = storage.get(Activity, activity_id)

    if not activity:
        abort(404)

    if environ.get('ZKHP_TYPE_STORAGE') == "db":
        if activity in place.activities:
            return make_response(jsonify(activity.to_dict()), 200)
        else:
            place.activities.append(activity)
    else:
        if activity_id in place.activity_ids:
            return make_response(jsonify(activity.to_dict()), 200)
        else:
            place.activity_ids.append(activity_id)

    storage.save()
    return make_response(jsonify(activity.to_dict()), 201)
