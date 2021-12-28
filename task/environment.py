import os
import pathlib


def get_voice_login_details():
    dot_env = get_path_to_dot_env()
    if not os.path.exists(dot_env):
        print(f'path not exist : {dot_env}')
        exit()
    project_name = get_project_name()
    login_details = dict()
    with open(dot_env, 'r') as de:
        de_lines = de.readlines()
        for de_line in de_lines:
            # find the project specific line
            if project_name in de_line:
                details = de_line.split(';')[1].split(' ')
                for detail in details:
                    k = detail.split('=')[0].strip('\n')
                    v = detail.split('=')[1].strip('\n')
                    login_details.update({k: v})
                break
    if not login_details:
        print(f'no login details found for this project name')
        exit()
    return login_details


def get_project_name():
    cwd = pathlib.Path(os.getcwd())
    return cwd.name


def get_path_to_dot_env():
    home = os.getenv('HOME')
    return pathlib.Path(home, '.env')
