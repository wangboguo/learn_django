from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World!")

def time_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  new_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
  assert False
  html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, new_time)
  return HttpResponse(html)

