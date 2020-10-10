import random

from django.http import Http404
from django.shortcuts import render

from tours import data
from django.views import View


class MainView(View):
    def get(self, request):
        random_tours = random.sample(data.tours.items(), 6)
        return render(request, 'tours/index.html', context={'title': data.title,
                                                            'subtitle': data.subtitle,
                                                            'description': data.description,
                                                            'random_tours': random_tours
                                                            })


class DepartureView(View):
    def get(self, request, departure):
        if departure not in data.departures:
            raise Http404
        else:
            sorted_tours = {}
            for i, j in data.tours.items():
                if j['departure'] == departure:
                    sorted_tours[i] = j
            prices = []
            nights = []
            for i in sorted_tours.values():
                prices.append(i['price'])
                nights.append(i['nights'])
            return render(request, 'tours/departure.html', context={'departure': departure,
                                                                    'current_departure': data.departures[departure],
                                                                    'sorted_tours': sorted_tours,
                                                                    'title': data.title,
                                                                    'min_price': min(prices),
                                                                    'max_price': max(prices),
                                                                    'min_nights': min(nights),
                                                                    'max_nights': max(nights),
                                                                    'tours_amount': len(sorted_tours)
                                                                    })


class TourView(View):
    def get(self, request, tour_id):
        if tour_id not in data.tours:
            raise Http404
        else:
            return render(request, 'tours/tour.html', context={'title': data.tours[tour_id]['title'],
                                                               'stars': data.tours[tour_id]['stars'],
                                                               'country': data.tours[tour_id]['country'],
                                                               'nights': data.tours[tour_id]['nights'],
                                                               'picture': data.tours[tour_id]['picture'],
                                                               'description': data.tours[tour_id]['description'],
                                                               'price': data.tours[tour_id]['price'],
                                                               'tour_departure':
                                                                   data.departures[data.tours[tour_id]['departure']]
                                                               })
