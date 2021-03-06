"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6
For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(device_location, work_location, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': {
            'deviceLocation' : device_location,
            'workLocation' : work_location
        },
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    card_title = "Welcome"
    speech_output = "Welcome to Toll Free Seattle. " \
                    "Please tell me your work location by saying, " \
                    "my work location is Microsoft Building 35"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your work location by saying, " \
                    "my work location is Microsoft Building 35."
    should_end_session = False
    return build_response("none", "none", build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying Toll Free Seattle. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response("none", "none", build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def set_work_location_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    should_end_session = False
    work_location = session['attributes']['workLocation']
    device_location = session['attributes']['deviceLocation']

    if 'WorkLocation' in intent['slots']:
        work_location = intent['slots']['WorkLocation']['value']
        speech_output = "I now know your work location is " + \
                        work_location + \
                        ". You can ask me your commute by saying, " \
                        "what's my commute?"
        reprompt_text = "You can ask me your commute by saying, " \
                        "what's my commute?"
    else:
        speech_output = "I'm not sure what your work location is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your work location is. " \
                        "You can tell me your work location by saying, " \
                        "my work location is Microsoft Building 35."
    return build_response(device_location, work_location, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def create_work_location_attributes(work_location):
    return {"workLocation": work_location}

def get_work_location_from_session(intent, session):
    reprompt_text = None

    work_location = session['attributes']['workLocation']
    device_location = session['attributes']['deviceLocation']
    if session.get('attributes', {}) and "workLocation" in session.get('attributes', {}):
        work_location = session['attributes']['workLocation']
        speech_output = "Your location is " + work_location + \
                        "."
        should_end_session = False
    else:
        speech_output = "I'm not sure what your work location is. " \
                        "You can say, my work location is Microsoft Building 35."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(device_location, work_location, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def set_device_location_in_session(intent, session):
    """ Sets the device location in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    should_end_session = False

    work_location = session['attributes']['workLocation']
    device_location = session['attributes']['deviceLocation']
    if 'DeviceLocation' in intent['slots']:
        device_location = intent['slots']['DeviceLocation']['value']
        speech_output = "I now know your device location is " + \
                        device_location + \
                        ". You can ask me your commute by saying, " \
                        "what's my commute?"
        reprompt_text = "You can ask me your commute by saying, " \
                        "what's my commute?"
    else:
        speech_output = "I'm not sure what your device location is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your device location is. " \
                        "You can tell me your device location by saying, " \
                        "my work location is 1234 Rainbow Ave Seattle, WA 12345."
    return build_response(device_location, work_location, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def create_device_location_attributes(device_location):
    return {"deviceLocation": device_location}

def get_device_location_from_session(intent, session):
    reprompt_text = None

    work_location = session['attributes']['workLocation']
    device_location = session['attributes']['deviceLocation']
    if session.get('attributes', {}) and "deviceLocation" in session.get('attributes', {}):
        device_location = session['attributes']['deviceLocation']
        speech_output = "Your device location is " + device_location + \
                        "."
        should_end_session = False
    else:
        speech_output = "I'm not sure what your device location is. " \
                        "You can say, my device location is 1234 Rainbow Ave Seattle, WA 12345."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(device_location, work_location, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_commute_response(intent, session)
    reprompt_text = None

    work_location = session['attributes']['workLocation']
    device_location = session['attributes']['deviceLocation']
    should_end_session = True

    #try to get the device location with the API and reset the device_location var if you can

    #use google maps API to calc time for both routes and miles

    #store the toll stuff, query time, return actual toll

    #calculate which one is better

    #make sure to set speech_output to the result otherwise the method will fail

    return build_response(device_location, work_location, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

        
# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "GetDeviceLocation":
        return get_device_location_from_session(intent, session)
    elif intent_name == "GetWorkLocation":
        return get_work_location_from_session(intent, session)
    elif intent_name == "MyDeviceLocationIs":
        return set_device_location_in_session(intent, session)
    elif intent_name == "MyWorkLocationIs":
        return set_work_location_in_session(intent, session)
    elif intent_name == "WhatIsMyCommute":
        return get_commute_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    
    if (event['session']['application']['applicationId'] !=
             "amzn1.ask.skill.54f5f11f-8c4d-401e-8777-264d22fdfd2f"):
         raise ValueError("Invalid Application ID")
     """

    if event['session']['new']:
        event['session']['attributes'] = {}
        on_session_started( {'requestId': event['request']['requestId'] }, event['session'])
    if event['request']['type'] == 'IntentRequest':
        return on_intent(event['request'], event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    if event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])