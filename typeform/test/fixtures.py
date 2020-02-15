import os

# Don't use your own account for this, this will delete pretty much everything you have!
TOKEN = os.environ.get('TYPEFORM_TOKEN')

# Tests will be scoped to this workspace.
WORKSPACE = 'https://api.typeform.com/workspaces/[YOUR WORKSPACE ID]'
WORKSPACE_ID = WORKSPACE.split('/')[-1]

if not TOKEN or '[YOUR WORKSPACE ID]' in WORKSPACE:
    raise Exception("You need to setup TOKEN and WORKSPACE in fixtures.py")