from django.shortcuts import redirect
import user_agents


def root_redirect(request):
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = user_agents.parse(user_agent_string)

    if user_agent.is_mobile:
        schema_view = 'doc:schema-redoc'
    else:
        schema_view = 'doc:schema-swagger-ui'

    return redirect(schema_view, permanent=True)
