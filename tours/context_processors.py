from tours import data


def base_departures(request):
    return {
        'departures': data.departures,
    }
