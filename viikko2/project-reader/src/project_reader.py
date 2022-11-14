from urllib import request
from project import Project
import tomli


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        content_dict = tomli.loads(content)
        name = content_dict["tool"]["poetry"]["name"]
        description = content_dict["tool"]["poetry"]["description"]
        dependencies = list(content_dict["tool"]["poetry"]["dependencies"].keys())
        dev_dependencies = list(content_dict["tool"]["poetry"]["dev-dependencies"].keys())
        
        return Project(name, description, dependencies, dev_dependencies)

