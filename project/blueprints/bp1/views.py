def json_serialise_user(user):

    return {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name
        'created_at': user.added_at.isoformat()
    }
    