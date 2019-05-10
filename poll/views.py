from django.shortcuts import render, redirect
from .models import Human
from django.views.generic import View 
import re
from django.contrib import messages

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
   test_ip = 360
   people = Human.objects.all()
   half_list = len(people)/2

   def get(self, request):
      zipped_list = zip(self.people[::2], self.people[1::2])
      user_ip = re.sub('[,:.]','',get_client_ip(request))
      person = Human.objects.get(id=28)
      count_votes = len(person.votes.all(user_ip))
      print(user_ip)
      return render(request, 'poll/home.html', context={
         'zipped_list':zipped_list,
         'count_votes':count_votes,
         'half_list':self.half_list,
      })
   
   def post(self, request):
      check_values = request.POST.getlist('person[]')
      user_ip = re.sub('[.]','',get_client_ip(request))
      try:
         if len(check_values) == self.half_list:
            for kek in check_values:
               qwerty = Human.objects.get(id=int(kek))
               qwerty.votes.up(user_ip)
            return redirect('home_url')
         else:
            messages.success(request, f'Вы проголосовали неверное количество раз. Перезагрузите страницу')
            return redirect('home_url')
      except:
         return redirect('home_url')

def leaderboard(request):
   people = Human.objects.all()
   number_1 = Human.objects.filter().order_by('-vote_score')[0]
   number_2 = Human.objects.filter().order_by('-vote_score')[1]
   number_3 = Human.objects.filter().order_by('-vote_score')[2]
   return render(request, 'poll/leaderboard.html', context={
      'number_1':number_1,
      'number_2':number_2,
      'number_3':number_3
   })

