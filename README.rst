typeform
========

API Client for `TypeForm <https://typeform.com>`_.

At the time of writing this client TypeForm only has a data access API for fetching responses to a given form.


Getting Started
---------------
Install the module with: ``pip install typeform``

.. code:: python

   import typeform

   form = typeform.Form(api_key='<api_key>', form_id='<form_id>')

   # Fetch all responses to the form with default options
   responses = form.get_responses()

   # Fetch responses with specific options
   responses = form.get_responses(limit=10, since=1487863154)

   # Print '<question>: <answer>' for all responses to this form
   for response in responses:
       for answer in response.answers:
           print '{question}: {answer}'.format(question=answer.question, answer=answer.answer)

   # Fetch a specific response
   response = form.get_response('<response_token>')
