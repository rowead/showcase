# Showcase
Digital Label and environmental monitoring of a gallery showcase using a raspberry pi, touchscreen and a DHT11 sensor.

Sensor logs are written to disk and then shipped to a centralised datastore for monitoring and dashboarding
(bleeding edge elasticsearch and kibana 6.0.0-alpha2 docker containers running on a laptop, with logstash
installed on the raspberry pi).

The "Showcase" polls an API for it's details including location and a list of items that it contains.
The item details include accession numbers and department. Dashboarding will enable aggregations
and drilldowns based on any of these details eg. Show me all of History's items in the Fremantle
branch over the last year.

Likewise the label will be generated from the same or a similar API endpoint with both the label
and Showcase information coming out of a museum ECMS.
 
## Road to MVP
Fundamentals of logging, shipping and dashboarding are in place. Tweaks and improvements to come.


Starting with Raspbian Linux distro, this must be turned into or replaced with a solid kiosk solution.


Fill out faked API endpoint with label information and create HTML5 based label.

## Notes
init.sh was created to document the extra steps to set up logstash on a raspberry pi, after the work was done
it hasn't been tested.