import os
import json
from argopy.utilities import isAPIconnected, list_available_data_src


def save_api_status(out_dir: str = '.'):
    colors = {'up': 'green', 'down': 'red'}
    flist = []
    for api, mod in list_available_data_src().items():
        if hasattr(mod, 'api_server_check'):
            label = "API status: %s" % api
            status = 'down'
            if isAPIconnected(src=api, data=1):
                status = 'up'
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
            with open(api.upper(), 'w') as f:
                f.write(status.upper())
            os.environ[api.upper()] = status.upper()
    return flist

if __name__ == '__main__':
    save_api_status('.')
