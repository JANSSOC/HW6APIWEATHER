{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# WeatherPy\n",
    "----\n",
    "\n",
    "### Analysis\n",
    "* As expected, the weather becomes significantly warmer as one approaches the equator (0 Deg. Latitude). More interestingly, however, is the fact that the southern hemisphere tends to be warmer this time of year than the northern hemisphere. This may be due to the tilt of the earth.\n",
    "* There is no strong relationship between latitude and cloudiness. However, it is interesting to see that a strong band of cities sits at 0, 80, and 100% cloudiness.\n",
    "* There is no strong relationship between latitude and wind speed. However, in northern hemispheres there is a flurry of cities with over 20 mph of wind.\n",
    "\n",
    "---\n",
    "\n",
    "#### Note\n",
    "* Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Dependencies and Setup\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "import time\n",
    "import json \n",
    "import openweathermapy.core as owm\n",
    "\n",
    "# Import API key\n",
    "from api_keys import api_key\n",
    "\n",
    "# Incorporated citipy to determine city based on latitude and longitude\n",
    "from citipy import citipy\n",
    "\n",
    "# Output File (CSV)\n",
    "output_data_file = \"output_data/cities.csv\"\n",
    "\n",
    "# Range of latitudes and longitudes\n",
    "lat_range = (-90, 90)\n",
    "lng_range = (-180, 180)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate Cities List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "609"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# List for holding lat_lngs and cities\n",
    "lat_lngs = []\n",
    "cities = []\n",
    "\n",
    "# Create a set of random lat and lng combinations\n",
    "lats = np.random.uniform(low=-90.000, high=90.000, size=1500)\n",
    "lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)\n",
    "lat_lngs = zip(lats, lngs)\n",
    "\n",
    "# Identify nearest city for each lat, lng combination\n",
    "for lat_lng in lat_lngs:\n",
    "    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name\n",
    "    \n",
    "    # If the city is unique, then add it to a our cities list\n",
    "    if city not in cities:\n",
    "        cities.append(city)\n",
    "\n",
    "# Print the city count to confirm sufficient count\n",
    "len(cities)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Perform API Calls\n",
    "* Perform a weather check on each city using a series of successive API calls.\n",
    "* Include a print log of each city as it'sbeing processed (with the city number and city name).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Begining Data Retrival\n",
      "Processing Record 0 city: mataura\n",
      "Processing Record 1 city: dargaville\n",
      "Processing Record 2 city: derbent\n",
      "Processing Record 3 city: deputatskiy\n",
      "Processing Record 4 city: tasiilaq\n",
      "Processing Record 5 city: puerto ayora\n",
      "Processing Record 6 city: bredasdorp\n",
      "Processing Record 7 city: rorvik\n",
      "City not found. Skipping...\n",
      "Processing Record 9 city: hermanus\n",
      "City not found. Skipping...\n",
      "Processing Record 11 city: ushuaia\n",
      "Processing Record 12 city: punta arenas\n",
      "Processing Record 13 city: chokurdakh\n",
      "Processing Record 14 city: hithadhoo\n",
      "Processing Record 15 city: newport\n",
      "Processing Record 16 city: coihaique\n",
      "Processing Record 17 city: saint-augustin\n",
      "City not found. Skipping...\n",
      "Processing Record 19 city: lata\n",
      "Processing Record 20 city: new norfolk\n",
      "Processing Record 21 city: jamestown\n",
      "Processing Record 22 city: narsaq\n",
      "Processing Record 23 city: albany\n",
      "Processing Record 24 city: nanortalik\n",
      "Processing Record 25 city: rikitea\n",
      "Processing Record 26 city: cape town\n",
      "Processing Record 27 city: avesta\n",
      "Processing Record 28 city: souillac\n",
      "Processing Record 29 city: aklavik\n",
      "Processing Record 30 city: dingle\n",
      "Processing Record 31 city: bluff\n",
      "Processing Record 32 city: new glasgow\n",
      "Processing Record 33 city: madimba\n",
      "Processing Record 34 city: letlhakane\n",
      "Processing Record 35 city: avarua\n",
      "Processing Record 36 city: bella union\n",
      "Processing Record 37 city: hobart\n",
      "Processing Record 38 city: kapaa\n",
      "Processing Record 39 city: atuona\n",
      "Processing Record 40 city: kalabo\n",
      "Processing Record 41 city: pasni\n",
      "Processing Record 42 city: tuktoyaktuk\n",
      "Processing Record 43 city: mae ramat\n",
      "Processing Record 44 city: komsomolskiy\n",
      "City not found. Skipping...\n",
      "Processing Record 46 city: labuhan\n",
      "Processing Record 47 city: mount gambier\n",
      "Processing Record 48 city: makakilo city\n",
      "City not found. Skipping...\n",
      "Processing Record 50 city: barrow\n",
      "Processing Record 51 city: talcahuano\n",
      "Processing Record 52 city: lagoa\n",
      "City not found. Skipping...\n",
      "Processing Record 54 city: pevek\n"
     ]
    }
   ],
   "source": [
    "settings = {\"units\": \"imperial\", \"appid\": api_key}\n",
    "current_weather_list = []\n",
    "city =[]\n",
    "date = time.process_time\n",
    "print('Begining Data Retrival')\n",
    "for x in range(len(cities)):\n",
    "    try:\n",
    "        current_weather = owm.get_current(cities[x], **settings)\n",
    "        print(f\"Processing Record {x} city: {cities[x]}\")\n",
    "        current_weather_list.append(current_weather)\n",
    "        city.append(cities[x])\n",
    "        \n",
    "    except:\n",
    "        print(\"City not found. Skipping...\")     \n",
    "    time.sleep(.02) \n",
    "print('Data Retrival Complete') "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "summary = [\"name\",\"coord.lat\",\"coord.lon\",\"main.temp\", \"wind.speed\",\"main.humidity\", \"clouds.all\",\"sys.country\",\"dt\",\"main.temp_max\"]\n",
    "\n",
    "# Create a Pandas DataFrame with the results\n",
    "data = [response(*summary) for response in current_weather_list]\n",
    "\n",
    "weather_data = pd.DataFrame(data, index=city)\n",
    "column_names = [\"City\",\"Latitude\",\"Longitude\",\"Temperature\",\"Wind Speed (mph)\" , \"Humidity (%)\",\"Cloudiness (%)\",\"Country\",\"Date\",\"Max Temperature (F)\"]\n",
    "weather_data = pd.DataFrame(data, columns=column_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_data.to_csv(\"Cities_Weather.csv\")\n",
    "weather_data.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Convert Raw Data to DataFrame\n",
    "* Export the city data into a .csv.\n",
    "* Display the DataFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "weather_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Plotting the Data\n",
    "* Use proper labeling of the plots using plot titles (including date of analysis) and axes labels.\n",
    "* Save the plotted figures as .pngs."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Temperature Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l_x = weather_data.iloc[:,1]\n",
    "t_y = weather_data.iloc[:,9]\n",
    "plt.scatter(l_x, t_y, marker=\"o\", facecolors=\"steelblue\", edgecolors=\"black\",alpha=0.75)\n",
    "plt.xlabel(l_x.name)\n",
    "plt.grid(which='major',axis='both')\n",
    "plt.ylabel(t_y.name)\n",
    "plt.title(f\"City Latitude vs. {t_y.name[:-3]}(1/12/2019)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Humidity Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l_x = weather_data.iloc[:,1]\n",
    "t_y = weather_data.iloc[:,5]\n",
    "plt.scatter(l_x, t_y, marker=\"o\", facecolors=\"steelblue\", edgecolors=\"black\",alpha=0.75)\n",
    "plt.xlabel(l_x.name)\n",
    "plt.grid(which='major',axis='both')\n",
    "plt.ylabel(t_y.name)\n",
    "plt.title(f\"City {l_x.name} vs. {t_y.name[:-3]}(1/12/2019)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Cloudiness Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l_x = weather_data.iloc[:,1]\n",
    "t_y = weather_data.iloc[:,6]\n",
    "plt.scatter(l_x, t_y, marker=\"o\", facecolors=\"steelblue\", edgecolors=\"black\",alpha=0.75)\n",
    "plt.xlabel(l_x.name)\n",
    "plt.grid(which='major',axis='both')\n",
    "plt.ylabel(t_y.name)\n",
    "plt.title(f\"City {l_x.name} vs. {t_y.name[:-3]}(1/12/2019)\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Latitude vs. Wind Speed Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l_x = weather_data.iloc[:,1]\n",
    "t_y = weather_data.iloc[:,4]\n",
    "plt.scatter(l_x, t_y, marker=\"o\", facecolors=\"steelblue\", edgecolors=\"black\",alpha=0.75)\n",
    "plt.xlabel(l_x.name)\n",
    "plt.grid(which='major',axis='both')\n",
    "plt.ylabel(t_y.name)\n",
    "plt.title(f\"City {l_x.name} vs. {t_y.name[:-5]}(1/12/2019)\")"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
