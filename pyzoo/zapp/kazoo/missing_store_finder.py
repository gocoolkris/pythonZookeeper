__author__ = 'gokul'

from zoo_connector import ZooConnector


class StoreFinder(object):


    def __init__(self, inputDict):

        self.target_env = inputDict['env_to_consolidate']
        self.source_envs = inputDict['data_source_envs']
        self.connection = ZooConnector(inputDict['host'], inputDict['port'])


    def get_children(self, root):
        children = self.connection.client.get_children(path=root)
        return [child.decode("utf-8") for child in children]

    def get_stores_in_source(self):
        paths = ["/" + env + "/MAPPINGS/OBJECTS/GSI STORES" for env in self.source_envs]
        stores = []
        for path in paths:
            if self.connection.client.exists(path):
                stores.extend(self.get_children(path))
        return list(set(stores))


    def get_stores_in_target(self):
        stores = []
        path = "/" + self.target_env + "/MAPPINGS/OBJECTS/GSI STORES"
        if self.connection.client.exists(path):

            stores.extend(self.get_children(path))
        return stores

    def missing_stores(self):

        source_stores = self.get_stores_in_source()
        target_stores = self.get_stores_in_target()
        missing_stores = []
        for store in source_stores:
            if store not in target_stores:
                missing_stores.append(store)

        return missing_stores

sf = StoreFinder({'host' : 'lvststcfgsvc-vip.us.gspt.net', 'port' : '2181', 'env_to_consolidate' : 'UAT01', 'data_source_envs': ['UAT04', 'UAT05', 'UAT06']})
print sf.missing_stores()
