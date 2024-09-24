import copy


def create_flow(service_specs: list, deployment_specs: list, flow_uuid, api_key):
    modified_deployment_specs = []

    for deployment_spec in deployment_specs:
        modified_deployment_spec = copy.deepcopy(deployment_spec)
        container = modified_deployment_spec['template']['spec']['containers'][0]

        # Add environment variables
        container['env'] = container.get('env', []) + [
            {'name': 'JSDELIVRAPIKEY', 'value': 'dev'},
            {'name': 'FOO', 'value': 'BAR'},
        ]

        modified_deployment_spec['template']['spec']['containers'][0] = container
        modified_deployment_specs.append(modified_deployment_spec)


    return {
        "deployment_specs": modified_deployment_specs,
        "config_map": {
        }
    }


def delete_flow(config_map, flow_uuid):
    return
