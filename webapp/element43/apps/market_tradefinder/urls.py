from django.conf.urls import patterns, url

urlpatterns = patterns('apps.market_station.views',
    #
    # Trading URLs
    #

    # System or Region Search / Live Search
    url(r'^trading/search/$', 'station.search', name='trading_search'),
    url(r'^trading/live_search/$', 'station.live_search', name='trading_live_search'),

    # Trading group browser panel
    url(r'^trading/station/(?P<station_id>[0-9]+)/import/browse/panel/(?P<group_id>[0-9]+)/$', 'station.panel', name='import_panel'),

    # Import AJAX
    url(r'^trading/station/(?P<station_id>[0-9]+)/import/system/(?P<system_id>[0-9]+)/$', 'station.import_system', name='import_system'),
    url(r'^trading/station/(?P<station_id>[0-9]+)/import/region/(?P<region_id>[0-9]+)/$', 'station.import_region', name='import_region'),

    # Station Info
    url(r'^trading/station/(?P<station_id>[0-9]+)/$', 'station.station', name='station'),

    # Station ranking
    url(r'^trading/station/ranking/$', 'station.ranking', name='station_ranking'),
)