from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

# Create your views here.
#-------------------------------------------------------------------------------
# Page Display Routines

def _showError(error):
    values = {'error':error}
    context = Context(values)
    return render_to_response('error.htpl', context)

def _showSearch(r):
    values = {}
    context = Context(values)
    context.update(csrf(r))
    return render_to_response('search.htpl', context)

def _showResults(r, results):
    values = {}
    context = Context(values)
    return render_to_response('results.htpl', context)

#-------------------------------------------------------------------------------
# Processing Routines

def _getResults():
    #ZookeeperInstance.objects.all()
    pass

#-------------------------------------------------------------------------------
# Page Handlers

def search(r):
    if r.method == 'POST':
        query = r.POST['searchquery']
        results=_getResults(query)
        return _showResults(results)
    else:
        return _showSearch(r)

