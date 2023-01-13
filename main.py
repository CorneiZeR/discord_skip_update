import json
import os

FILE_PATH = '/opt/discord/resources/build_info.json'


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_json(path: str, data: dict) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


if __name__ == '__main__':
    file_dict = read_json(FILE_PATH)

    if not (current_version := file_dict.get('version')):
        raise KeyError('Here is wrong file, or missing "version" argument, stopping script...')

    # calculating new version
    new_version = current_version.split('.')
    new_version = '.'.join(new_version[:-1] + [str(int(new_version[-1]) + 1)])

    # printing to console
    print(f'Current version: {current_version}')
    print(f'New version (auto) : {new_version}')

    # confirmation new version
    manual_version = input('Is it right? (enter / manual version) : ').split()

    # making copy data
    new_file_dict = dict(file_dict)
    new_file_dict['version'] = new_version if not manual_version else manual_version

    # making copy file
    copied_data_path = f'{FILE_PATH}.old'
    write_json(copied_data_path, file_dict)

    # writing new file
    write_json(FILE_PATH, new_file_dict)

    # confirming that its works
    if input('Is that work? (y/n) : ').lower().strip() == 'n':
        print('Returning old file back...')
        write_json(FILE_PATH, file_dict)

    # remove temp file
    os.remove(copied_data_path)
