import geocoder
# Declare destinations list here.
destinations = ['Space Needle',
'Crater Lake',
'Golden Gate Bridge',
'Yosemite National Park',
'Las Vegas, Nevada',
'Grand Canyon National Park',
'Aspen, Colorado',
'Mount Rushmore',
'Yellowstone National Park',
'Sandpoint, Idaho',
'Banff National Park',
'Capilano Suspension Bridge']

for point in destinations:

#   Get the lat-long coordinates from `geocoder.arcgis`.
 g = geocoder.arcgis(point)
 #   Print out the place name and the coordinates.
# latlng is a tuple with a length of 2.
 print(point, 'is located at','{0:.4f}'.format(g.latlng[0]),'{0:.4f}'.format(g.latlng[1]))
