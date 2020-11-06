import os
import json

try:
    from argopy.utilities import isAPIconnected, list_available_data_src
    do_save = True
except ModuleNotFoundError:
    do_save = False
    print("argopy could not be loaded properly.\n We failed to check web API status !")


def save_api_status(out_dir: str = '.'):
    colors = {'up': 'green', 'down': 'red'}
    flist = []
    for api, mod in list_available_data_src().items():
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
                flist.append(outfile)

            # Create text file with status:
            outfile = os.path.join(out_dir, '%s.txt' % api.upper())
            with open(outfile, 'w') as f:
                f.write(status.upper())

    return flist

def save_unknown_status(out_dir: str = '.'):
    # This is a dirty trick when we couldn't load argopy
    colors = {'unknown': 'black'}
    flist = []
    for api in ['erddap', 'argovis']:
        label = "Data source '%s'" % api
        status = 'unknown'
        print(label)

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
            flist.append(outfile)

        # Create text file with status:
        outfile = os.path.join(out_dir, '%s.txt' % api.upper())
        with open(outfile, 'w') as f:
            f.write(status.upper())

    return flist


if __name__ == '__main__':
    print("do_save:", do_save)
    if do_save:
        save_api_status('.')
    else:
        save_unknown_status('.')
