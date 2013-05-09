from {{ project_name }}.settings import NEWRELIC_ENV
import os

# Initialize New Relic Agent.
import newrelic.agent
newrelic.agent.initialize(
	os.path.join(os.path.dirname(os.path.abspath(__file__)), 'newrelic.ini'),
	NEWRELIC_ENV)

# Wrap WSGI application.
from {{ project_name }}.conf.wsgi import application
application = newrelic.agent.wsgi_application()(application)
