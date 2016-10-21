import requests
import urllib

class RESTClient:
    """
    Class to handle all REST API Calls
    """

    def __init__(self):
        """
        Initiate Client with the base url of the API and the
        version information.

        Parameters:
            base_url - (str) The API Base URL
            versioninfo - (str) The version component to add to base_url
        """

        #self.base_url = base_url
        #self.version_info = version_info
        self.http_functions = {
            'GET'   : self.get,
            'POST'  : self.post,
            'PUT'   : self.put,
            'DELETE'  : self.delete,
        }

    def http_request(self, url_component, request_type, params, is_json= False):
        """
        Make the API Call according to the URL component
        provided and the request type.

        Parameters:
            urlcomponent - (str) The API component to call
            reqType - (str) The HTTP Request type (GET/POST/HEAD/PUT/DELE)
            params - (dict) The parameters to pass in the http call
        """
        call_url = url_component

        if request_type not in self.http_functions:
            return {
                'http_status'   : 0,
                'error_string'  : 'Invalid HTTP method',
                'data'          : [],
                'error_info'    : 'Invalid HTTP method used, must be of type \
                GET/POST/PUT',
            }
        return self.http_functions[request_type](call_url, params)

    def get(self, call_url, params):
        """
        Make a GET request on the API.

        Parameters:
            call_url    - (str) The API URL to call
            params      - (dict) Parameters to  place in the call
        """
        print call_url
        print params
        try:
            response = requests.get(call_url, params=params)
        except requests.exceptions.RequestException as e:
            return {
                'http_status'   : 0,
                'error_string'  : 'An unkown error occured',
                'data'          : [],
                'error_info'    : str(e),
            }

        content = response.json()

        return {
            'http_status'   : response.status_code,
            'error_string'  : '',
            'data'          : content,
            'error_info'     : '',
        }

    def post(self, call_url, params):
        """
        Make a POST request on the API.

        Parameters:
            call_url    - (str) The API URL to call
            params      - (dict) Parameters to  place in the call
        """

        try:
            response = requests.post(call_url, data=params)
        except requests.exceptions.RequestException as e:
            return {
                'http_status'   : 0,
                'error_string'  : 'An unkown error occured',
                'data'          : [],
                'error_info'    : str(e),
            }

        content = response.json()

        return {
            'http_status'   : response.status_code,
            'error_string'  : '',
            'data'          : content,
            'error_info'     : '',
        }

    def put(self, call_url, params):
        """
        Make a PUT request on the API.

        Parameters:
            call_url    - (str) The API URL to call
            params      - (dict) Parameters to  place in the call
        """

        try:
            response = requests.put(call_url, data=params)
        except requests.exceptions.RequestException as e:
            return {
                'http_status'   : 0,
                'error_string'  : 'An unkown error occured',
                'data'          : [],
                'error_info'    : str(e),
            }

        content = response.json()

        return {
            'http_status'   : response.status_code,
            'error_string'  : '',
            'data'          : content,
            'error_info'     : '',
        }

    def delete(self, call_url, params = {}):
        """
        Make a DELETE request on the API.

        Parameters:
            call_url    - (str) The API URL to call
            params      - (dict) Parameters to  place in the call
        """

        try:
            response = requests.get(call_url)
        except requests.exceptions.RequestException as e:
            return {
                'http_status'   : 0,
                'error_string'  : 'An unkown error occured',
                'data'          : [],
                'error_info'    : str(e),
            }

        content = response.json()

        return {
            'http_status'   : response.status_code,
            'error_string'  : '',
            'data'          : content,
            'error_info'     : '',
        }







