import os
import json
from argopy.utilities import isAPIconnected, list_available_data_src


def check_this_api(out_dir, colors, api, mod):
    if hasattr(mod, 'api_server_check'):
        label = "Data source '%s'" % api
        status = 'down'
        if isAPIconnected(src=api, data=1):
            status = 'up'

        # Create json file with full results for badge:
        color = colors[status]
        message = status
        data = {}
        data['schemaVersion'] = 1
        data['label'] = label
        data['message'] = message
        data['color'] = color
        outfile = os.path.join(out_dir, 'argopy_api_status_%s.json' % api)
        with open(outfile, 'w') as f:
            json.dump(data, f)

        # Create text file with status:
        outfile = os.path.join(out_dir, '%s.txt' % api.upper())
        with open(outfile, 'w') as f:
            f.write(status.upper())


def skip_this_api(out_dir, colors, api):
    label = "Data source '%s'" % api
    status = 'unknown'

    # Create json file with full results for badge:
    color = colors[status]
    message = status
    data = {}
    data['schemaVersion'] = 1
    data['label'] = label
    data['message'] = message
    data['color'] = color
    outfile = os.path.join(out_dir, 'argopy_api_status_%s.json' % api)
    with open(outfile, 'w') as f:
        json.dump(data, f)

    # Create text file with status:
    outfile = os.path.join(out_dir, '%s.txt' % api.upper())
    with open(outfile, 'w') as f:
        f.write(status.upper())


def save_api_status(out_dir: str = '.'):
    colors = {'up': 'green', 'down': 'red', 'unknown': 'black'}
    api_expected = ['erddap', 'argovis']
    api_available = list_available_data_src()
    for api in api_expected:
        if api in api_available:
            check_this_api(out_dir, colors, api, api_available[api])
        else:
            skip_this_api(out_dir, colors, api)


if __name__ == '__main__':
    save_api_status('.')
