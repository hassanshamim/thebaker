from ask import alexa

FOODSTUFFS = {
    'rice': {
        "descriptors": [('white, brown'), ('long', 'short', 'medium'), ('cooked', 'uncooked')]
    },
    'sugar': {
        "descriptors": [('white', 'brown'), ('powdered', 'cane')]
    }
}


def lambda_handler(request, context=None):
    metadata = {}
    app_id = 'amzn1.echo-sdk-ams.app.a563fd76-b63a-43bd-9d92-9af0bbe27e14'
    if not request.session['application']['applicationId'] == app_id:
        return alexa.create_response('yeah nice try.')

    return alexa.route_request(request, metadata)


@alexa.intent_handler('GetFoodType')
def food_lookup(request):
    return alexa.create_response(message='GetFoodType has been called')


@alexa.default_handler
def default(request):
    return alexa.create_response(message='default handler')


@alexa.request_handler("LaunchRequest")
def launch_request_handler(request):
    return alexa.create_response(message="This was a Launch Request")


@alexa.request_handler("SessionEndedRequest")
def session_ended_request_handler(request):
    # Your service cannot send back a response to a SessionEndedRequest.
    # Oh well :(
    pass


@alexa.intent_handler('AMAZON.CancelIntent')
def cancel(request):
    return alexa.create_response(message='CancelIntent has been called', end_session=True)


@alexa.intent_handler('AMAZON.StopIntent')
def stop(request):
    return alexa.create_response(message='StopIntent has been called', end_session=True)


@alexa.intent_handler('AMAZON.HelpIntent')
def help(request):
    return alexa.create_response(message='HelpIntent has been called', end_session=True)
