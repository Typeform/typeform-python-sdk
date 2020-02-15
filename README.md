# typeform

[![PyPI version](https://badge.fury.io/py/typeform.svg)](https://badge.fury.io/py/typeform) [![Build Status](https://travis-ci.org/MichaelSolati/typeform-python-sdk.svg?branch=master)](https://travis-ci.org/MichaelSolati/typeform-python-sdk) [![Coverage Status](https://coveralls.io/repos/github/MichaelSolati/typeform-python-sdk/badge.svg?branch=master)](https://coveralls.io/github/MichaelSolati/typeform-python-sdk?branch=master)

Python Client wrapper for [Typeform API](https://developer.typeform.com/)

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initialize](#initialize)
- [Reference](#reference)
  - [Create Client](#typeformapi_key)
  - [Forms](#forms)
  - [Responses](#responses)
- [Tests](#tests

## Installation

``` bash
pip install typeform
```

## Usage

### Initialize

1 - Import client library

``` python
  from typeform import Typeform
```

2 - Create an instance with your personal token

``` python
  typeform = Typeform('<api_key>')
```

3 - Use any of the methods available in the [reference](#reference)

``` python
  # will retrieve all forms
  forms: dict = typeform.forms.list()
```

## Reference

### `Typeform('<api_key>')`

- Creates a new instance of Typeform's Python client
- Returns an instance with the methods described below

``` python
  typeform = Typeform('<api_key>')
```

Client returns the following properties:

- `forms`
- `responses`

Each one of them encapsulates the operations related to it (like listing, updating, deleting the resource).

### Forms

#### `forms.create(data: dict = {})`

Creates a form. Returns `dict` of created form. [See docs](https://developer.typeform.com/create/reference/create-form/).

```python
forms = Typeform('<api_key>').forms
result: dict = forms.create({ 'title': 'Hello World' })
```

#### `forms.delete(uid: str)`

Deletes the form with the given form_id and all of the form's responses. Returns a `str` based on success of deletion, `OK` on success, otherwise an error message. [See docs](https://developer.typeform.com/create/reference/delete-form/).

```python
forms = Typeform('<api_key>').forms
result: str = forms.delete('abc123')
```

#### `forms.get(uid: str)`

Retrieves a form by the given form_id. Includes any theme and images attached to the form as references. [See docs](https://developer.typeform.com/create/reference/retrieve-form/).

```python
forms = Typeform('<api_key>').forms
result: dict = forms.get('abc123')
```

#### `forms.list(page: int = None, pageSize: int = None, search: str = None, workspaceId: str = None)`

Retrieves a list of JSON descriptions for all forms in your Typeform account (public and private). Forms are listed in reverse-chronological order based on the last date they were modified. [See docs](https://developer.typeform.com/create/reference/retrieve-form/).

```python
forms = Typeform('<api_key>').forms
result: dict = forms.list()
```

#### `forms.update(uid: str, patch: bool = False, data: dict = {})`

Updates an existing form. Defaults to `put`. `put` will return the modified form as a `dict` object. `patch` will Returns a `str` based on success of change, `OK` on success, otherwise an error message. [See `put` docs](https://developer.typeform.com/create/reference/update-form/) or [`patch` docs](https://developer.typeform.com/create/reference/update-form-patch/).

```python
forms = Typeform('<api_key>').forms
result: dict = forms.update('abc123', { 'title': 'Hello World, Again' })
result: str = forms.update('abc123', { 'title': 'Hello World, Again' }, patch=True)
```

#### `forms.messages.get(uid: str)`

Retrieves the customizable messages for a form (specified by form_id) using the form's specified language. You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden. [See docs](https://developer.typeform.com/create/reference/retrieve-custom-form-messages/).

```python
forms = Typeform('<api_key>').forms
result: dict = forms.messages.get('abc123')
```

#### `forms.messages.update(uid: str, data={})`

Specifies new values for the customizable messages in a form (specified by form_id). You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden. Returns a `str` based on success of change, `OK` on success, otherwise an error message. [See docs](https://developer.typeform.com/create/reference/update-custom-messages/).

```python
forms = Typeform('<api_key>').forms
result: str = forms.messages.update('abc123', {
  'label.buttonHint.default': 'New Button Hint'
})
```

### Responses

#### `responses.list(uid: str, pageSize: int = None, since: str = None, until: str = None, after: str = None, before: str = None, includedResponseIds: str = None, completed: bool = None, sort: str = None, query: str = None, fields: List[str] = None)`

Returns form responses and date and time of form landing and submission. [See docs](https://developer.typeform.com/responses/reference/retrieve-responses/).

```python
responses = Typeform('<api_key>').responses
result: dict = responses.list('abc123')
```

#### `responses.delete(uid: str, includedTokens: Union[str, List[str]])`

Delete responses to a form. You must specify the `included_tokens` parameter. Returns a `str` based on success of deletion, `OK` on success, otherwise an error message. [See docs](https://developer.typeform.com/responses/reference/delete-responses/).

```python
responses = Typeform('<api_key>').responses
result: str = responses.delete('abc123' 'token1')
result: str = responses.delete('abc123' ['token2', 'token3'])
```

## Tests

⚠️⚠️⚠️⚠️⚠️ Don't use your own token to run tests, use a demo account with only few forms
