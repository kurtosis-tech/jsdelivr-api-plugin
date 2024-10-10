import copy


def create_flow(service_specs: list, pod_specs: list, flow_uuid, api_key):
    modified_pod_specs = []

    for pod_spec in pod_specs:
        modified_pod_spec = copy.deepcopy(pod_spec)
        containers = modified_pod_spec.get('containers', [])

        # Check if there are containers
        if containers:
            container = containers[0]
            # Add environment variables
            env_vars = container.get('env', [])

            for env in env_vars:
                if env.get("name") == "JSDELIVRAPIKEY":
                    env["value"] = api_key

            container['env'] = env_vars

            modified_pod_spec['containers'][0] = container

        modified_pod_specs.append(modified_pod_spec)

    return {
        "pod_specs": modified_pod_specs,
        "config_map": {}
    }


def delete_flow(config_map, flow_uuid):
    return
