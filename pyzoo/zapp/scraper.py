from BeautifulSoup import BeautifulSoup
import urllib2
from threading import Thread

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
        table = soup.find(text='GSI.properties').parent.parent.parent
        def parseRow(r):
            if type(r).__name__=='Tag':
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
    for t in threads: t.start()
    for t in threads: t.join()
#    for t in threads: print str(t.properties)[0:64]
    allprops=[]
    for t in threads: allprops.append(t.properties)
    return allprops

if __name__=='__main__':
    getAllProperties(
        [('env1','http://lvststwsv02-01.us.gspt.net:1201/gsi-payment-service/version/index.html'),
         ('env2','http://lvststwsv01-01.us.gspt.net:1201/gsi-payment-service/version/index.html')]
    )
