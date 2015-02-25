from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

SUCCESS_STRING = "Success"
FAILED_STRING = "Failed"


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def get_response_data(error_message, response_data):

    if error_message == "":
        response_code = SUCCESS_STRING
    else:
        response_code = FAILED_STRING

    content = {'responseCode': response_code, 'data': response_data, 'errorMessage': error_message}
    return content