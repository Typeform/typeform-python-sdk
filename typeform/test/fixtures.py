import os

# Set to True to use mocked requests.
# A False here will make the test suite hit the real API. Set TOKEN and WORKSPACE below to make it work.
MOCK = True

TOKEN = os.environ.get('TYPEFORM_TOKEN')

# Tests will be scoped to this workspace.
WORKSPACE = 'https://api.typeform.com/workspaces/hn3dNa'
WORKSPACE_ID = WORKSPACE.split('/')[-1]

if MOCK and (not TOKEN or '[YOUR WORKSPACE ID]' in WORKSPACE):
    raise Exception("You need to setup TOKEN and WORKSPACE in fixtures.py")