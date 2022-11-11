import jinja2
from jinja2 import Template, BaseLoader
import json
from pprint import pprint
from collections.abc import Iterable

# text = """Hello, original delimiters {{ name }}.
# new delimiters: <% name | default(123) %>
# new delimiters: <% name2 | default(123) %>"""

mapping_dict = {
    "id": 22254250,
    "account": {
        "login": "{{request.path.[1]}}",
        "id": 97319229,
        "node_id": "O_kgDOBcz5PQ",
        "avatar_url": "https://avatars.githubusercontent.com/u/97319229?v=4",
        "gravatar_id": "<% .account_g_id %>",
        "site_admin": "<% .account_site_admin %>"
    },
    "html_url": "https://github.com/organizations/{{request.path.[1]}}/settings/installations/22254250",
    "app_id": "<% .app_id | int %>",  # 164671
    "app_slug": "<% .app_slug %>",   # sdet-test-github-app
    "target_id": 97319229,
    "target_type": "Organization",
    "events": "<% .events  %>",
    "events1": "<% .events | list %>",
    "created_at": "{{now}}",
    "updated_at": "{{now}}",
    "suspended_by": None,
    "suspended_at": None
}


dict_to_json = json.dumps(mapping_dict)
custom_tem = jinja2.Template(
    dict_to_json, variable_start_string="<% .", variable_end_string="%>")
# jinja_env = jinja2.Environment(loader=BaseLoader, trim_blocks=True, variable_start_string='<%', variable_end_string='%>')
# template = jinja_env.from_string(text)

# data = {
#     "name": "sarah",
# }

render_data = {
    "account_g_id": 12321,
    "account_site_admin": False,
    "app_id": 164671,
    "app_slug": "sdet-test-github-app",
    "events": ["auth", "audit"]
}


# pprint(custom_tem.render(render_data))
result = json.loads(custom_tem.render(render_data))
pprint(result)
pprint(type(result))


# pprint(eval(result['events1']))
# pprint(type(eval(result['events1'])))
# pprint(eval(result['account']['site_admin']))
# pprint(type(eval(result['account']['site_admin'])))


# def eval_dict(data: dict):

#     for k, v in data.items():
#         # print(v)
#         if isinstance(v, dict):
#             return eval_dict(v)
#         elif isinstance(v, int):
#             continue
#         else:
#             try:
#                 data[k] = eval(v)
#             except:
#                 continue


# pprint(eval_dict(result))
