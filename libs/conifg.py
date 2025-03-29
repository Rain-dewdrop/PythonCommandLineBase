from pathlib import Path
from libs.readjson import readjson
import os
RootPath = Path(__file__).resolve().parent.parent
ProjectConfigPath = os.path.join(RootPath, 'ProjectConfig.json')
RootName = readjson(ProjectConfigPath,'RootName')
Version = readjson(ProjectConfigPath,'Version')
VersionType = readjson(ProjectConfigPath,'VersionType')
Author = readjson(ProjectConfigPath,'Author')
GitHubUrl = readjson(ProjectConfigPath,'GitHubUrl')
BiliBiliUrl = readjson(ProjectConfigPath,'BiliBiliUrl')