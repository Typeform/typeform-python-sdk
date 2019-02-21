# typeform

[![PyPI version](https://badge.fury.io/py/typeform.svg)](https://badge.fury.io/py/typeform) [![Build Status](https://travis-ci.org/MichaelSolati/typeform-python-sdk.svg?branch=master)](https://travis-ci.org/MichaelSolati/typeform-python-sdk)

Python Client wrapper for [Typeform API](https://developer.typeform.com/)

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
  - [Initialize](#initialize)
- [Reference](#reference)
  - [Create Client](#typeformapi_key)
  - [Forms](#forms)

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

Each one of them encapsulates the operations related to it (like listing, updating, deleting the resource).

### Forms

### `forms.create(data={})`

Creates a form. Returns `dict` of created form. [See docs](https://developer.typeform.com/create/reference/create-form/).

```python
forms = Typeform('<api_key>').forms
forms.create({ 'title': 'Hello World' })
```

#### `forms.delete('Form ID')`

Deletes the form with the given form_id and all of the form's responses. Return a `str` based on success of deletion, `OK` on success, otherwise an error message. [See docs](https://developer.typeform.com/create/reference/delete-form/).

```python
forms = Typeform('<api_key>').forms
forms.delete('abc123') # OK
```

#### `forms.get('Form ID')`

Retrieves a form by the given form_id. Includes any theme and images attached to the form as references. [See docs](https://developer.typeform.com/create/reference/retrieve-form/).

```python
forms = Typeform('<api_key>').forms
forms.get('abc123')
```

#### `forms.list()`

Retrieves a list of JSON descriptions for all forms in your Typeform account (public and private). Forms are listed in reverse-chronological order based on the last date they were modified. [See docs](https://developer.typeform.com/create/reference/retrieve-form/).

```python
forms = Typeform('<api_key>').forms
forms.list()
```

#### `forms.update('Form ID', data={}, patch=False)`

Updates an existing form. Defaults to `put`. `put` will return the modified form as a `dict` object. `patch` will return a `str` based on success of change, `OK` on success, otherwise an error message. [See `put` docs](https://developer.typeform.com/create/reference/update-form/) or [`patch` docs](https://developer.typeform.com/create/reference/update-form-patch/).

#### `forms.messages.get('Form ID')`

Retrieves the customizable messages for a form (specified by form_id) using the form's specified language. You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden. [See docs](https://developer.typeform.com/create/reference/retrieve-custom-form-messages/).

```python
forms = Typeform('<api_key>').forms
forms.messages.get('abc123')
```

#### `forms.messages.update('Form ID', data={})`

Specifies new values for the customizable messages in a form (specified by form_id). You can format messages with bold (*bold*) and italic (_italic_) text. HTML tags are forbidden. Return a `str` based on success of change, `OK` on success, otherwise an error message. [See docs](https://developer.typeform.com/create/reference/update-custom-messages/).

```python
forms = Typeform('<api_key>').forms
forms.messages.update('abc123', {
    'label.buttonHint.default': 'New Button Hint'
})
```
