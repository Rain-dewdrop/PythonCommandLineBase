import datetime
from libs.conifg import ProjectConfigPath,RootName
def log(text,mode='INFO'):
    if str.upper(mode) == 'INFO' or str.upper(mode) == 'WARN':
        prefix = f"{RootName} {datetime.datetime.now()}] [{str.upper(mode)}]"
        print(f'{prefix} {text}')