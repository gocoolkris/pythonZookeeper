__author__ = 'gokul'

from zoo_connector import ZooConnector

class ZooReader(object):

    def __init__(self,  host, port):

        self.root = "/"
        self.shared = "SHARED"
        self.gsi_pmt_svc = "/ENVIRONMENT/NA/LVS/gsi-payment-service"
        self.connection = ZooConnector(host, port)


    def path_to_gsi(self, env):
        return  self.root + env + self.gsi_pmt_svc


    def get_children(self, root):
        children = self.connection.client.get_children(path=root)
        return [child.decode("utf-8") for child in children]

    def node_exists(self, path):
        return self.connection.client.exists(path)

    def query(self, query_string):

        if not self.connection.is_connected():
            self.connection.reconnect()

        envs = self.get_children(self.root)
        print envs
        valid_paths_gsi = [self.path_to_gsi(env) for env in envs if(self.connection.client.exists(self.path_to_gsi(env)))]
        print valid_paths_gsi

        version_paths = []
        for gsi_path in valid_paths_gsi:
            children = self.get_children(gsi_path)
            version_paths.extend([gsi_path + "/" + child for child in children])

        print version_paths
        ## finally
        self.connection.disconnect()


    def get_all_possible_paths(self, path):

        if self.node_exists(path):
            children = self.get_children(path)
            child_paths = [path + "/" + child for child in children]
            print child_paths
            end_paths = []
            for child_path in child_paths:
                all_possible_paths = self.get_all_possible_paths(child_path)
                if all_possible_paths:
                    end_paths.extend(all_possible_paths)
            print end_paths
            return end_paths
        return list()


zr = ZooReader('lvststcfgsvc-vip.us.gspt.net', '2181')
#zr.query("chasepaymentech.backup.connection.enabled")
print zr.get_all_possible_paths("/TST01/ENVIRONMENT/NA/LVS/gsi-payment-service/2.26.1")