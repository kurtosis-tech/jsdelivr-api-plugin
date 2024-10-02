import copy


def create_flow(service_specs, deployment_specs, flow_uuid):

    modified_deployment_specs = []

    for deployment_spec in deployment_specs:
        modified_deployment_spec = copy.deepcopy(deployment_spec)
        modified_deployment_spec['template']['spec']['containers'][0]["image"] = "kurtosistech/redis-proxy-overlay:latest"

        modified_deployment_specs.append(modified_deployment_spec)

    return {
        "deployment_specs": modified_deployment_specs,
        "config_map": {}
    }

def delete_flow(config_map, flow_uuid):
    pass
