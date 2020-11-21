import os

from notebook.auth import passwd
from pathlib import Path

c = get_config()
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = [
    'configurable-http-proxy', '--redirect-port', '80']


# get password from '.alias'
BASE_DIR = Path(__file__).resolve().parent.parent
fn = BASE_DIR / 'envfile'
with open(fn, mode='r') as f:
    alias = f.read()
alias = alias.split('\n')
alias = {_.split('=')[0]: _.split('=')[1] for _ in alias}
print(alias)
password = passwd(alias['password'])


# jn root
c.NotebookApp.notebook_dir = alias['jnrootdir']

# heroku url
c.NotebookApp.allow_origin = alias['heroku_app']+'.herokuapp.com'

# jn password
c.NotebookApp.password = password
