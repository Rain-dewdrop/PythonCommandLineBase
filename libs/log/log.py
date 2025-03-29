import datetime
from libs.conifg import RootName
def log(text,mode='INFO'):
    if str.upper(mode) == 'INFO' or str.upper(mode) == 'WARN':
        print(f'{RootName} {datetime.datetime.now()}] [{str.upper(mode)}] {text}')
