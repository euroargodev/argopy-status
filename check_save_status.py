import os
import json
from argopy.utils import isAPIconnected, list_available_data_src


COLORS = {'up': 'green', 'down': 'red', 'unknown': 'black'}


def save_to_json(label, message, color, outfile):
    # Create json file with full results for a shieldio badge
    data = {}
    data['schemaVersion'] = 1
    data['label'] = label
    data['message'] = message
    data['color'] = color
    with open(outfile, 'w') as f:
        json.dump(data, f)


def save_to_txt(status, outfile):
    # Create text file with status
    with open(outfile, 'w') as f:
        f.write(status.upper())


def check_this_api(out_dir, api_name, mod):
    print("\nChecking status for '%s'" % api_name)

    if hasattr(mod, 'api_server_check'):
        print(mod.api_server_check)

        label = "Data source '%s'" % api_name
        status = 'down'
        if isAPIconnected(src=api_name, data=1):
            status = 'up'

        print("status='%s'" % status)

        outfile = os.path.join(out_dir, 'argopy_api_status_%s.json' % api_name)
        save_to_json(label, status, COLORS[status], outfile)

        outfile = os.path.join(out_dir, '%s.txt' % api_name.upper())
        save_to_txt(status, outfile)

    else:
        raise ValueError("Can't get status for this fetcher !")


def skip_this_api(out_dir, api_name):
    label = "Data source '%s'" % api_name
    status = 'unknown'

    outfile = os.path.join(out_dir, 'argopy_api_status_%s.json' % api_name)
    save_to_json(label, status, COLORS[status], outfile)

    outfile = os.path.join(out_dir, '%s.txt' % api_name.upper())
    save_to_txt(status, outfile)


def save_api_status(out_dir: str = '.'):
    api_expected = ['erddap', 'argovis', 'gdac']
    api_available = list_available_data_src()
    for api_name in api_expected:
        if api_name in api_available:
            check_this_api(out_dir, api_name, api_available[api_name])
        else:
            skip_this_api(out_dir, api_name)


if __name__ == '__main__':
    save_api_status('.')
