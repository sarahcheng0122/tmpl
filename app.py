import json

from liquid import Template, Environment

mapping_dict = {
    "id": 22254250,
    "account": {
        "login": "{{request.path.[1]}}",
        "gravatar_id": "<< account_g_id >>",
        "site_admin": "<< account_site_admin >>"
    },
    "html_url": "https://github.com/organizations/{{request.path.[1]}}/settings/installations/22254250",
    "app_id": "<< app_id | default: 11111 >>",  # 164671
    "app_slug": "<< app_slug | default: 'hahaha' >>",   # sdet-test-github-app
    "events": "<< events  >>",
    "events1": "[<< events | join: ',' >>]",
    "object_flag": "<% if env_flag == 0 %><<nprod>><% elsif env_flag == 1 %><<prod>><% endif %>",
    "created_at": "{{now}}",
    "suspended_at": None
}


data = {
    "account_g_id": 12321,
    "account_site_admin": False,
    "app_id": 164671,
    "app_slug": "sdet",
    "events": ["auth", "audit"],
    "env_flag": 1
}


env = Environment(statement_start_string="<<", statement_end_string=">>",
                  tag_start_string="<%", tag_end_string="%>", globals={"nprod": "key0", "prod": "key1"})

dict_to_json = json.dumps(mapping_dict)
tmpl = env.from_string(dict_to_json)

result = json.loads(tmpl.render(data))
print(result)
