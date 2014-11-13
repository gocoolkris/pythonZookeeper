from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from scraper import getAllProperties, urls
import re
# Create your views here.
#-------------------------------------------------------------------------------
# Page Display Routines

def _showError(error):
    values = {'error':error}
    context = Context(values)
    return render_to_response('error.htpl', context)

def _showSearch():
    values = {}
    context = Context(values)
    return render_to_response('search.htpl', context)

def _showResults(searchtype,searchquery,results):
    values = {
        'searchtype':searchtype,
        'searchquery':searchquery,
        'results':results
        }
    context = Context(values)
    return render_to_response('results.htpl', context)

#-------------------------------------------------------------------------------
# Processing Routines

# Returns list of tuples in the format:
# [ (Instance,Name,Value), ... ]
def _getResults(searchtype,searchquery):
    #ZookeeperInstance.objects.all()
    all_properties =  getAllProperties(urls)
    results = []
    if searchtype == 'text':
        for inst in all_properties:
            for tup in inst:
                print tup[1]
                if tup[1] == searchquery :
                    results.append(tup)
    else:
        searchquery.replace('*', '.*')
        pattern = re.compile(searchquery)
        for inst in all_properties:
            for tup in inst:
                if pattern.match(tup[1]):
                    results.append(tup)
    return results
    '''
    testval=[
        ("TST01","vantiv.connection.enabled","true"),
        ("TST02","vantiv.connection.enabled","false"),
        ("TST03","vantiv.connection.enabled","false"),
        ("DEV01","vantiv.connection.enabled","false"),
        ("DEV02","vantiv.connection.enabled","true"),
        ]
    return testval
    '''
#-------------------------------------------------------------------------------
# Page Handlers

def search(r):
    if 'q' in r.GET:
        query = r.GET['q']
        type = r.GET['t']
        results=_getResults(type,query)
        return _showResults(type,query,results)
    else:
        return _showSearch()

