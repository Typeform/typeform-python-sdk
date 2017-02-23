typeform
========

API Client for [TypeForm](https://typeform.com/).


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

   # Fetch a specific response
   response = form.get_response('<response_token>')
