from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Human
from .forms import HumanForm
from django.views.generic import View 
import re

def get_client_ip(request):
   """get the client ip from the request
   """
   remote_address = request.META.get('REMOTE_ADDR')
   # set the default value of the ip to be the REMOTE_ADDR if available
   # else None
   ip = remote_address
   # try to get the first non-proxy ip (not a private ip) from the
   # HTTP_X_FORWARDED_FOR
   x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
   if x_forwarded_for:
      proxies = x_forwarded_for.split(',')
      # remove the private ips from the beginning
      while (len(proxies) > 0 and
               proxies[0].startswith(PRIVATE_IPS_PREFIX)):
         proxies.pop(0)
      # take the first ip which is not a private one (of a proxy)
      if len(proxies) > 0:
         ip = proxies[0]

   return ip


class Poll(View):
   def get(self, request):
      people = Human.objects.all()
      votes_list = len(people)/2
      group_a = people[::2]
      group_b = people[1::2]
      zipped_list = zip(group_a,group_b)

      user_ip = re.sub('[,:.]','',get_client_ip(request))
      print()
      print(user_ip)
      print()
      print()
   

      ara = Human.objects.get(id=16)
      wmara = ara.votes.all(454)

      count_votes = len(wmara)

      print(count_votes)
      print(ara.votes.all(454))
      print()
      print(votes_list)




      #rr = Human.objects.get(id=8)
      #print(rr.votes.exists(50))
      return render(request, 'poll/home.html', context={
         'zipped_list':zipped_list,
         'count_votes':count_votes,
         'votes_list':votes_list,
      })
   
   def post(self, request):
      check_values1 = request.POST.getlist('person1[]')
      check_values2 = request.POST.getlist('person2[]')
      obwi = check_values1 + check_values2
      user_ip = re.sub('[.]','',get_client_ip(request))
      print(obwi)
      try:
         for kek in obwi:
            qwerty = Human.objects.get(id=int(kek))
            qwerty.votes.up(454)
         return redirect('home_url')
      except:
         return redirect('home_url')