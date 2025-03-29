import datetime
from libs.readjson import readjson
from libs.conifg import ProjectConfigPath
def log(text,mode='INFO'):
    if str.upper(mode) == 'INFO' or str.upper(mode) == 'WARN':
        prefix = f"{readjson(ProjectConfigPath,'RootName')} {datetime.datetime.now()}] [{mode}]"
        print(f'{prefix} {text}')