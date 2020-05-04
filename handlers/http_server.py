"""
This module was created to handle HTTP Requests in Proxy Server project.
"""

from http.server import BaseHTTPRequestHandler

# pylint: disable=super-init-not-called
class ReverseProxy(BaseHTTPRequestHandler):
    """
This is a child from BaseHTTPRequestHandler class. It receives an extra parameter
calles config which is the YAML configuration that was passed by parameter.
It creates variables to be used in its do_GET and do_POST jobs.
The do_GET and do_POST jobs handle the rules informed by the YAML file.
"""
    def __init__(self, config):
        self.hostname = config['main']['hostname']
        self.port = config['main']['port']
        self.redirect_to_https = config['main']['redirect-to-https']

    def __call__(self, *args):
        super().__init__(*args)

    # pylint: disable=invalid-name
    def do_GET(self):
        """
This method handles the rules that were informed in the YAML configuration file.
        """
        # not working yet
        location = 'http://%s:%d' % (self.hostname, self.port)
        response = 302

        if self.redirect_to_https is True:
            location = 'https://%s:%d' % (self.hostname, self.port)


        self.send_response(response)
        self.send_header('Location', location)
        self.end_headers()
