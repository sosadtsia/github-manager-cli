import yaml

with open('labeler.yaml', 'r') as stream:
    data = yaml.safe_load(stream)

def get_labels(lables):
    """

    """
    labels_keys = list(data.get(environment, {}).keys())
    return env_keys

if DEV == True:
    print(get_keys("DEV"))
elif PROD == True:
    print(get_keys("PROD"))
