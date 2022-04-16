from djangorestframework_camel_case.render import CamelCaseJSONRenderer


class CustomCamelCaseJSONRenderer(CamelCaseJSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Restructure render `data`.
        """

        status_code = str(renderer_context['response'].status_code)

        if status_code.startswith('2'):
            response_dict = {'status': 'success', 'data': data, 'message': None}
        else:
            response_dict = {
                'status': 'failure', 'data': None, 
                'message': data.get('detail') or data, 
            }

        return super(CustomCamelCaseJSONRenderer, self).render(
            response_dict, accepted_media_type, renderer_context
        )
