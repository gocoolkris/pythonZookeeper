from BeautifulSoup import BeautifulSoup
import urllib2
from threading import Thread
import datetime

class LoaderThread(Thread):

    def __init__(self, iname, url):
        self.url = url
        self.iname = iname
        self.properties=[]
        super(LoaderThread, self).__init__()

    def run(self):
        self.properties = self._loadInstanceProperties(self.url)

    def _parsePaymentsPage(self, htmldata):

        soup = BeautifulSoup(htmldata)
        table = [None]
        gsi_prop_name = soup.find(text='NAME')
        gsi_prop_value = soup.find(text='VALUE')
        if gsi_prop_name.parent.parent.parent == gsi_prop_value.parent.parent.parent:
            table = gsi_prop_name.parent.parent.parent

        def parseRow(r):
            if type(r).__name__ == 'Tag':
                return (self.iname, r.contents[1].text, r.contents[3].text)
            else: return None
        contentlist = map(parseRow,table)
        return filter(lambda x: x != None,contentlist)

    def _loadInstanceProperties(self, url):
        htmldata = urllib2.urlopen(url).read()
        return self._parsePaymentsPage(htmldata)

# Takes a list of URLs for the payments pages
# Returns all properties from all URLs
def getAllProperties(urls):
    threads=[]
    for (name, url) in urls: threads.append(LoaderThread(name, url))
    for t in range(len(threads)):
        threads[t].start()
    for t in range(len(threads)):
        threads[t].join()
#    for t in threads: print str(t.properties)[0:64]
    allprops=[]
    for t in threads: allprops.append(t.properties)
    return allprops


urls = [('DEV01_1','http://lvsdevwsv01-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('DEV01_2','http://lvsdevwsv01-02.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('DEV02_1','http://lvsdevwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('DEV02_2','http://lvsdevwsv02-02.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('DEV04_1','http://lvsdevwsv04-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('DEV04_2','http://lvsdevwsv04-02.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('TST01_1','http://lvststwsv01-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('TST01_2','http://lvststwsv01-02.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('TST02_1','http://lvststwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
        ('TST02_2','http://lvststwsv02-02.us.gspt.net:1201/gsi-payment-service/version/index.html')
        ]

'''
lvsdevwsv01-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv02-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv03-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv03-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv04-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv04-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv05-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv05-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv06-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsdevwsv06-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv01-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv01-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv02-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv03-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv03-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv04-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv04-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv05-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv05-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv06-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvststwsv06-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsprewsv05-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsprewsv05-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsprewsv06-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsprewsv06-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv01-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv01-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv02-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv03-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv03-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv04-01.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsuatwsv04-02.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv01.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv02.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv03.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv04.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv01-1.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv01-2.us.gspt.net:1201/gsi-payment-service/version/index.html
lvsldtwsv01-3.us.gspt.net:1201/gsi-payment-service/version/index.html
'''
if __name__=='__main__':
    getAllProperties(urls)
