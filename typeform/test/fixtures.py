FORM_RESPONSE_200 = {
  'http_status': 200,
  'stats': {
    'responses': {
      'showing': 1,
      'total': 13,
      'completed': 7
    }
  },
  'questions': [
    {
      'id': 'email_id',
      'question': 'What is your email address?',
      'field_id': 1234
    },
    {
      'id': 'list_id_choice',
      'question': 'What do you think of this client?',
      'field_id': 56789
    },
  ],
  'responses': [
    {
      'completed': '1',
      'token': 'test_response_token',
      'metadata': {
        'browser': 'touch',
        'platform': 'mobile',
        'date_land': '2017-02-20 22:22:43',
        'date_submit': '2017-02-20 22:50:33',
        'user_agent': 'User-Agent',
        'referer': 'https://underdog.typeform.com/to/test_form_id',
        'network_id': 'abcdef'
      },
      'hidden': [],
      'answers': {
        'email_id': 'test-user@underdog.io',
        'list_id_choice': 'It is awesome!',
      }
    }
  ]
}

FORM_RESPONSE_200_EMPTY = {
  'http_status': 200,
  'stats': {
    'responses': {
      'showing': 0,
      'total': 13,
      'completed': 7
    }
  },
  'questions': [
    {
      'id': 'email_id',
      'question': 'What is your email address?',
      'field_id': 1234
    },
    {
      'id': 'list_id_choice',
      'question': 'What do you think of this client?',
      'field_id': 56789
    },
  ],
  'responses': []
}

FORM_RESPONSE_404 = {
    'message': 'typeform with uid test_form_id was not found',
    'status': 404
}

FORM_RESPONSE_400 = {
    'message': 'invalid request',
    'status': 400
}

FORM_RESPONSE_403 = {
    'message': 'please provide a valid api key',
    'status': 403
}

FORM_RESPONSE_429 = {
    'message': 'rate limit exceeded',
    'status': 429
}
