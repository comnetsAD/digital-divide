#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from geopy.geocoders import Nominatim
import sys
import random
import numpy as np
import math
from matplotlib.lines import Line2D
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
import matplotlib.image as mpimg


loc_flag = {"Addis Ababa,Ethiopia":"ETH","Warsaw,Poland":"POL","Tokyo,Japan":"JPN","Ulaanbaatar,Mongolia":"MNG","Bremen,Germany":"DEU","Cairo,Egypt":"EGY","Lahore,Pakistan":"PAK","Zilina,Slovakia":"SVK","Moscow,Russia":"RUS","Ufa,Russia":"RUS","Dubai,UAE":"are","Accra,Ghana":"gha","Bishkek,Kyrgyzstan":"kgz","Seoul,South Korea":"kor","Copenhagen,Denmark":"dnk","Houston,United States":"usa","Helsinki,Finland":"fin","Arkhangelsk,Russia":"RUS","Hanoi,Vietnam":"vnm","Manama,Bahrain":"bhr","Kuwait,Kuwait":"kwt","London,United Kingdom":"gbr","Mumbai,India":"ind","Beijing,China":"chn","Shenzhen,China":"chn","Spain":"esp","Tenerife,Spain":"esp","Fiji":"fji","Havana,Cuba":"cub","Islamabad,Pakistan":"pak","Sarvar,Hungary":"hun","Riyadh,Saudi Arabia":"sau","Riga,Latvia":"lva","Oslo,Norway":"nor","Skopje,Macedonia":"mkd","Gaggio Montano,Italy":"ita","Sarajevo,Bosnia and Herzegovina":"bih","Kingston,Jamaica":"jam","Zenica,Bosnia and Herzegovina":"bih","Sydney,Australia":"aus","Mombasa,Kenya":"ken","Manila,Philippines":"phl","Guadalajara,Mexico":"mex","Caracas,Venezuela":"ven","Quetzaltenango,Guatemala":"gtm","Lima,Peru":"per","Dar es Salaam,Tanzania":"tza","Rabat,Morocco":"mar","Namangan,Uzbekistan":"uzb","Monterrey,Mexico":"mex","Buenos Aires,Argentina":"arg","Bogota,Colombia":"col","Penang,Malaysia":"mys","Tainan,Taiwan":"twn","Kremenchuk,Ukraine":"ukr","United States":"usa","Cebu City,Philippines":"phl","Kathmandu,Nepal":"npl","Bhaktapur,Nepal":"npl","Salvador,Brazil":"bra","Tegucigalpa,Honduras":"hnd","Incheon,South Korea":"kor","Kumasi,Ghana":"gha","Port-Harcourt,Nigeria":"nga","Arusha,Tanzania":"tza","Vancouver,Canada":"can","Kiev,Ukraine":"ukr","La Paz & Tarija,Bolivia":"bol","Singapore,Singapore":"sgp","Kinshasa,Democratic Republic of Congo":"cod","Washington,United States":"usa","Nur-Sultan,Kazakhstan":"kaz","Tirana,Albania":"alb","Zaporizhzhya,Ukraine":"ukr","Coimbatore,India":"ind","New York,United States":"usa","Riyadh,Saudi Arabia":"sau"}

loc_coord = {"Tokyo,Japan":[139.2394179,36.5748441,1],"Riga,Latvia":[24.1051846,56.9493977,1],"Hanoi,Vietnam":[105.8544441,21.0294498,-1],"Sydney,Australia":[151.2164539,-33.8548157,1],"Kuwait,Kuwait":[45.4979476,29.2733964,-1],"Warsaw,Poland":[19.134422,52.215933,1],"Skopje,Macedonia":[22.4316495,41.9960924,1],"Mumbai,India":[72.8353355,18.9387711,-1],"Ufa,Russia":[55.947727,54.726288,1],"Houston,United States":[-95.3676974,29.7589382,1],"Fiji":[179.0122737,-18.1239696,-1],"Caracas,Venezuela":[-66.9146017,10.506098,-1],"Beijing,China":[116.3912757,39.906217,-1],"Manama,Bahrain":[50.5822436,26.2235041,-1],"Addis Ababa,Ethiopia":[38.75,9.0,-1],"Seoul,South Korea":[126.939210804,37.56498255,1],"London,United Kingdom":[-2.1276474,51.5073219,1],"Bremen,Germany":[9.2071646,53.0758196,1],"Ulaanbaatar,Mongolia":[106.9177016,47.9184676,-1],"Sarvar,Hungary":[16.9342165,47.2517426,1],"Vancouver,Canada":[-123.1139529,49.2608724,1],"Lahore,Pakistan":[74.3141775,31.5656079,-1],"Gaggio Montano,Italy":[12.674297,42.6384261,1],"Zenica,Bosnia and Herzegovina":[19.0080954,44.200713,1],"Zilina,Slovakia":[18.7260535114,49.22055575,1],"Cairo,Egypt":[31.243666,30.048819,-1],"Islamabad,Pakistan":[73.0651511,33.6938118,-1],"Dubai,UAE":[55.1713,25.0657,-1],"Helsinki,Finland":[24.9425769,60.1674098,1],"Havana,Cuba":[-82.3589631,23.135305,-1],"Accra,Ghana":[-0.2057437,5.5600141,-1],"Arkhangelsk,Russia":[40.537121,64.543022,1],"Kingston,Jamaica":[-76.7928128,17.9712148,-1],"Zaporizhzhya,Ukraine":[35.1182867,47.8507859,1],"Monterrey,Mexico":[-100.3152586,25.6802019,-1],"Copenhagen,Denmark":[12.5700724,55.6867243,1],"Tenerife,Spain":[-16.6214471211,28.2935785,1],"Moscow,Russia":[37.3273304,55.4792046,1],"Kumasi,Ghana":[-1.6230404,6.698081,-1],"Arusha,Tanzania":[36.7085848185,-3.427534,-1],"Cebu City,Philippines":[123.8931107,10.3095549,-1],"Namangan,Uzbekistan":[71.2611952,41.0036287,-1],"Bogota,Colombia":[-74.0760439,4.59808,-1],"Tegucigalpa,Honduras":[-87.2012631,14.0931919,-1],"Sarajevo,Bosnia and Herzegovina":[18.3866868,43.8519774,1],"Tainan,Taiwan":[120.184982,22.9912348,1],"Bhaktapur,Nepal":[85.320244,27.708796,-1],"Kiev,Ukraine":[30.5241361,50.4500336,1],"Incheon,South Korea":[126.7052,37.456,1],"Rabat,Morocco":[-6.834543,34.022405,-1],"Kathmandu,Nepal":[85.320244,27.708796,-1],"Nur-Sultan,Kazakhstan":[71.4388595155,51.15092055,-1],"Coimbatore,India":[76.9628425,11.0018115,-1],"New York,United States":[-74.0060,40.7128,1],"Riyadh,Saudi Arabia":[42.3528328,25.6242618,-1],"Bishkek,Kyrgyzstan":[74.6070455,42.8765753,-1]}

loc_text = {"Vancouver,Canada":[-145,49.2608724],"Houston,United States":[-139,29.7589382],"New York,United States":[-133,40.7128],"Washington,United States":[-127,36.740236,1],"Tenerife,Spain":[-65,28.2935785,1],"Spain":[-59,39.3262345,1],"London,United Kingdom":[-53,51.5073219,1],"Gaggio Montano,Italy":[-47,42.6384261,1],"Tirana,Albania":[-41,41.31588575,1],"Sarajevo,Bosnia and Herzegovina":[-35,43.8519774,1],"Zenica,Bosnia and Herzegovina":[-29,44.200713,1],"Sarvar,Hungary":[-23,47.2517426,1],"Bremen,Germany":[-17,53.0758196,1],"Zilina,Slovakia":[-11,49.22055575,1],"Copenhagen,Denmark":[-5,55.6867243,1],"Warsaw,Poland":[1,1],"Oslo,Norway":[7,59.9133301,1],"Riga,Latvia":[13,56.9493977,1],"Helsinki,Finland":[19,60.1674098,1],"Skopje,Macedonia":[25,41.9960924,1],"Kiev,Ukraine":[31,50.4500336,1],"Moscow,Russia":[37,55.4792046,1],"Arkhangelsk,Russia":[43,64.543022,1],"Kremenchuk,Ukraine":[49,49.09285285,1],"Zaporizhzhya,Ukraine":[55,47.8507859,1],"Ufa,Russia":[61,54.726288,1],"Singapore,Singapore":[110,1.357107,1],"Shenzhen,China":[116,22.555454,1],"Tainan,Taiwan":[122,22.9912348,1],"Seoul,South Korea":[128,37.56498255,1],"Incheon,South Korea":[134,37.456,1],"Tokyo,Japan":[140,36.5748441,1],"Sydney,Australia":[185,-33.8548157,1],"Monterrey,Mexico":[-145,25.6802019,-1],"Guadalajara,Mexico":[-139,20.6720375,-1],"Quetzaltenango,Guatemala":[-133,14.7360257,-1],"Havana,Cuba":[-127,23.135305,-1],"Tegucigalpa,Honduras":[-121,14.0931919,-1],"Kingston,Jamaica":[-115,17.9712148,-1],"Bogota,Colombia":[-95,4.59808,-1],"Caracas,Venezuela":[-89,10.506098,-1],"Lima,Peru":[-83,-12.0621065,-1],"La Paz & Tarija,Bolivia":[-77,-21.5329252,-1],"Salvador,Brazil":[-71,-12.9822499,-1],"Buenos Aires,Argentina":[-65,-34.6075682,-1],"Rabat,Morocco":[-29,34.022405,-1],"Kumasi,Ghana":[-23,6.698081,-1],"Accra,Ghana":[-17,5.5600141,-1],"Cairo,Egypt":[-11,30.048819,-1],"Port-Harcourt,Nigeria":[-5,4.7676576,-1],"Kinshasa,Democratic Republic of Congo":[1,-4.3217055,-1],"Addis Ababa,Ethiopia":[7,9.0,-1],"Arusha,Tanzania":[13,-3.427534,-1],"Mombasa,Kenya":[19,-4.0390146,-1],"Dar es Salaam,Tanzania":[25,-6.8160837,-1],"Riyadh,Saudi Arabia":[50,25.6242618,-1],"Kuwait,Kuwait":[56,29.2733964,-1],"Manama,Bahrain":[62,26.2235041,-1],"Dubai,UAE":[68,25.0657,-1],"Mumbai,India":[93,18.9387711,-1],"Lahore,Pakistan":[99,31.5656079,-1],"Islamabad,Pakistan":[105,33.6938118,-1],"Kathmandu,Nepal":[111,27.708796,-1],"Bhaktapur,Nepal":[117,27.708796,-1],"Namangan,Uzbekistan":[123,41.0036287,-1],"Bishkek,Kyrgyzstan":[129,42.8765753,-1],"Hanoi,Vietnam":[135,21.0294498,-1],"Nur-Sultan,Kazakhstan":[141,51.15092055,-1],"Cebu City,Philippines":[147,10.3095549,-1],"Manila,Philippines":[153,14.5906216,-1],"Beijing,China":[159,39.906217,-1],"Ulaanbaatar,Mongolia":[165,47.9184676,-1],"Fiji":[185,-18.1239696,-1]}

pageloadtime = {"Tokyo,Japan":14.58,"Riga,Latvia":13.69,"Hanoi,Vietnam":11.77,"Sydney,Australia":16.23,"Kuwait,Kuwait":16.79,"Warsaw,Poland":15.55,"Skopje,Macedonia":14.49,"Mumbai,India":20.61,"Ufa,Russia":47.06,"Houston,United States":16.21,"Fiji":20.5,"Caracas,Venezuela":26.17,"Beijing,China":32.93,"Manama,Bahrain":18.57,"Addis Ababa,Ethiopia":34.9,"Seoul,South Korea":19.43,"London,United Kingdom":15.42,"Bremen,Germany":14.79,"Ulaanbaatar,Mongolia":16.54,"Sarvar,Hungary":22.04,"Vancouver,Canada":14.16,"Lahore,Pakistan":20.89,"Gaggio Montano,Italy":12.36,"Zenica,Bosnia and Herzegovina":13.18,"Zilina,Slovakia":23.37,"Cairo,Egypt":19.2,"Islamabad,Pakistan":18.28,"Dubai,UAE":15.41,"Helsinki,Finland":13.25,"Havana,Cuba":18.76,"Accra,Ghana":34.7,"Arkhangelsk,Russia":17.24,"Kingston,Jamaica":25.57,"Zaporizhzhya,Ukraine":14.62,"Monterrey,Mexico":21.4,"Copenhagen,Denmark":12.64,"Tenerife,Spain":15.71,"Moscow,Russia":17.27,"Kumasi,Ghana":20.4,"Arusha,Tanzania":18.21,"Cebu City,Philippines":25.88,"Namangan,Uzbekistan":21.18,"Bogota,Colombia":17.22,"Tegucigalpa,Honduras":19.7,"Sarajevo,Bosnia and Herzegovina":14.87,"Tainan,Taiwan":16.52,"Bhaktapur,Nepal":15.11,"Kiev,Ukraine":17.36,"Incheon,South Korea":14.14,"Rabat,Morocco":15.03,"Kathmandu,Nepal":20.86,"Nur-Sultan,Kazakhstan":29.25,"Coimbatore,India":30.26,"New York,United States":16.61,"Riyadh,Saudi Arabia":17.85,"Bishkek,Kyrgyzstan":15.94}

costPerGB_GDP = {"Riga,Latvia": 3.1214123,"Spain": 0.8462224765,"Tokyo,Japan": 2.060041174,"Hanoi,Vietnam": 2.616403199,"Sydney,Australia": 0.384112204,"Kuwait,Kuwait": 0.183502531,"Warsaw,Poland": 1.14140307,"Skopje,Macedonia": 5.34716968,"Mumbai,India": 2.57312585,"Ufa,Russia": 5.907099377,"Houston,United States": 1.0,"Fiji": 3.30121391,"Caracas,Venezuela": 21.12617155,"Beijing,China": 3.121412318,"Shenzhen,China": 3.121412318,"Manama,Bahrain": 1.523604695,"Addis Ababa,Ethiopia": 45.54829514,"Seoul,South Korea": 1.142486984,"London,United Kingdom": 1.280952335,"Bremen,Germany": 1.877936724,"Ulaanbaatar,Mongolia": 1.709029665,"Sarvar,Hungary": 5.368685684,"Vancouver,Canada": 3.358269832,"Lahore,Pakistan": 7.84242205,"Gaggio Montano,Italy": 0.581943433,"Zenica,Bosnia and Herzegovina": 3.28752574,"Zilina,Slovakia": 1.853466712,"Cairo,Egypt": 1.943919444,"Islamabad,Pakistan": 7.84242205,"Bishkek,Kyrgyzstan": 0.6965984,"Dubai,UAE": 3.338816013,"Helsinki,Finland": 0.074241938,"Havana,Cuba": 52.03267922,"Accra,Ghana": 8.032621157,"Arkhangelsk,Russia": 5.907099377,"Kingston,Jamaica": 20.61495396,"Copenhagen,Denmark": 0.398043763,"Tenerife,Spain": 0.846222488,"Moscow,Russia": 5.907099377,"Monterrey,Mexico": 6.020536876,"Guadalajara,Mexico": 6.020536876,"Zaporizhzhya,Ukraine": 2.35230309,"Kumasi,Ghana": 8.032621157,"Cebu City,Philippines": 9.087522682,"Manila,Philippines": 9.087522682,"Bogota,Colombia": 16.59313675,"Namangan,Uzbekistan": 13.07077772,"Tegucigalpa,Honduras": 25.79121918,"Arusha,Tanzania": 13.06813526,"Sarajevo,Bosnia and Herzegovina": 3.28752574,"Tainan,Taiwan": 1.435521552,"Bhaktapur,Nepal": 4.199460505,"Kiev,Ukraine": 2.35230309,"Incheon,South Korea": 1.142486984,"Rabat,Morocco": 6.329556662,"Kathmandu,Nepal": 4.199460505,"Nur-Sultan,Kazakhstan": 0.937186765,"Coimbatore,India": 2.57312585,"New York,United States": 1.0,"Riyadh,Saudi Arabia": 0.155815643}

costPerGB_PPP = {"Riga,Latvia": 2.166064982,"Spain": 0.910384068,"Tokyo,Japan": 1.740530688,"Hanoi,Vietnam": 1.365457547,"Sydney,Australia": 0.392413342,"Kuwait,Kuwait": 0.326203209,"Warsaw,Poland": 1.71009772,"Skopje,Macedonia": 4.737221997,"Mumbai,India": 1.429965586,"Ufa,Russia": 11.11507653,"Houston,United States": 0.910384068,"Fiji": 2.15010142,"Caracas,Venezuela": 32.06470695,"Beijing,China": 1.782011092,"Shenzhen,China": 1.782011092,"Manama,Bahrain": 2.794117647,"Addis Ababa,Ethiopia": 9.616290019,"Seoul,South Korea": 1.214332492,"London,United Kingdom": 1.282051282,"Bremen,Germany": 2.388818297,"Ulaanbaatar,Mongolia": 1.49798178,"Sarvar,Hungary": 8.029204014,"Vancouver,Canada": 3.690753691,"Lahore,Pakistan": 3.963790563,"Gaggio Montano,Italy": 0.599739244,"Zenica,Bosnia and Herzegovina": 2.327365729,"Zilina,Slovakia": 1.95164076,"Cairo,Egypt": 2.303403756,"Islamabad,Pakistan": 3.963790563,"Bishkek,Kyrgyzstan": 0.328808135,"Dubai,UAE": 6.349206349,"Helsinki,Finland": 0.078794902,"Havana,Cuba": 43.33333333,"Accra,Ghana": 3.158195317,"Arkhangelsk,Russia": 11.11507653,"Kingston,Jamaica": 9.056284805,"Copenhagen,Denmark": 0.400456216,"Tenerife,Spain": 0.910384068,"Moscow,Russia": 11.11507653,"Monterrey,Mexico": 5.576513538,"Guadalajara,Mexico": 5.576513538,"Zaporizhzhya,Ukraine": 2.629174993,"Kumasi,Ghana": 3.158195317,"Cebu City,Philippines": 4.4428402,"Manila,Philippines": 4.4428402,"Bogota,Colombia": 14.77002473,"Namangan,Uzbekistan": 11.60614212,"Tegucigalpa,Honduras": 7.329089399,"Arusha,Tanzania": 4.4428402,"Sarajevo,Bosnia and Herzegovina": 2.327365729,"Tainan,Taiwan": 2.878057597,"Bhaktapur,Nepal": 1.203421492,"Kiev,Ukraine": 2.629174993,"Incheon,South Korea": 1.214332492,"Rabat,Morocco": 2.234910277,"Kathmandu,Nepal": 1.203421492,"Nur-Sultan,Kazakhstan": 1.84994771,"Coimbatore,India": 1.429965586,"New York,United States": 0.910384068,"Riyadh,Saudi Arabia": 0.348027842}

costPerGB_Direct = {"Sydney,Australia":0.43,"Manama,Bahrain":1.5,"Sarajevo,Bosnia and Herzegovina":1.09,"Zenica,Bosnia and Herzegovina":1.09,"Vancouver,Canada":3.62,"Beijing,China":1.1,"Shenzhen,China":1.1,"Bogota,Colombia":5.45,"Havana,Cuba":13.0,"Copenhagen,Denmark":0.5,"Cairo,Egypt":0.5,"Addis Ababa,Ethiopia":2.21,"Fiji":1.0,"Helsinki,Finland":0.08,"Bremen,Germany":2.21,"Kumasi,Ghana":0.9506606606999999,"Accra,Ghana":0.9506606606999999,"Tegucigalpa,Honduras":3.23,"Sarvar,Hungary":3.83,"Coimbatore,India":0.38,"New Delhi,India":0.38,"Bhubaneswar,India":0.38,"Mumbai,India":0.38,"Gaggio Montano,Italy":0.54,"Kingston,Jamaica":4.4,"Tokyo,Japan":1.87,"Nur-Sultan,Kazakhstan":0.54,"Kuwait,Kuwait":0.2,"Bishkek,Kyrgyzstan":0.08,"Skopje,Macedonia":2.0,"Guadalajara,Mexico":2.58,"Monterrey,Mexico":2.58,"Ulaanbaatar,Mongolia":0.46,"Rabat,Morocco":1.04,"Kathmandu,Nepal":0.3137037037,"Bhaktapur,Nepal":0.3137037037,"Peshawar,Pakistan":0.8041666667,"Lahore,Pakistan":0.8041666667,"Islamabad,Pakistan":0.8041666667,"Cebu City,Philippines":1.77,"Manila,Philippines":1.77,"Warsaw,Poland":0.82,"Ufa,Russia":3.619050562,"Arkhangelsk,Russia":3.619050562,"Moscow,Russia":3.619050562,"Riyadh,Saudi Arabia":0.16,"Zilina,Slovakia":1.33,"Incheon,South Korea":1.032125984,"Seoul,South Korea":1.032125984,"Tenerife,Spain":0.75,"Tainan,Taiwan":1.66,"Dar es Salaam,Tanzania":0.76,"Arusha,Tanzania":0.76,"Dubai,UAE":4.9,"Kiev,Ukraine":0.6588732394,"Kremenchuk,Ukraine":0.6588732394,"Zaporizhzhya,Ukraine":0.6588732394,"London,United Kingdom":1.31,"Houston,United States":1.370588235,"Washington,United States":1.370588235,"New York,United States":1.370588235,"Namangan,Uzbekistan":2.0,"Caracas,Venezuela":5.5,"Hanoi,Vietnam":0.46,"Riga,Latvia":1.38}

colors = ['#ffffff','#a50026','#d73027','#f46d43','#fdae61','#fee08b','#d9ef8b','#a6d96a','#66bd63','#1a9850','#006837'][::-1]

COST_MAP = {
	"GDP":costPerGB_GDP,
	"PPP":costPerGB_PPP,
	"Direct":costPerGB_Direct,
}

labels = {
			"GDP":["0.07$", "4.2$", "13.1$", "25.8$", "   52$"],
			"PPP":["0.08$", "1.28$", "3.69$", "14.8$", "   43$"],
			"Direct":["0.08$", "1,77$", "3.61$", "5.45$", "   13$"]
		}


if len(sys.argv) == 1 or sys.argv[1] not in COST_MAP:
	sys.exit("Error: you need to define the cost function (GDP,PPP, or Direct)")

b = np.asarray(list(pageloadtime.values()))
limits = []
for i in range(10,100,10):
	limits.append(np.percentile(b,i))


fig, ax = plt.subplots(figsize=(9*10,11*10))

m = Basemap(resolution='c',
            projection='merc',
            lat_0=0, lon_0=0,
            llcrnrlon=-168, llcrnrlat=-56.9, urcrnrlon=190, urcrnrlat=74.8)

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#A9A9A9',lake_color='#46bcec')
m.drawmapboundary(color='white', 
                  linewidth=0.0, 
                  fill_color='white')
m.drawcoastlines(linewidth=1,color='#A9A9A9')
m.fillcontinents('#E8E8E8', 
                 lake_color='white')

locator = Nominatim(user_agent="myGeocoder")

for l in pageloadtime: 
	location = loc_coord[l]
	x, y = m(location[0], location[1])

	if l not in pageloadtime:
		color_index = 10

	else:
		color_index = 9
		for i in range(len(limits)):
			if pageloadtime[l] <= limits[i]:
				color_index = i
				break

	if l not in COST_MAP[sys.argv[1]]:
		COST_MAP[sys.argv[1]][l] = -1

	if "Direct" in sys.argv[1]:
		cost = 3*COST_MAP[sys.argv[1]][l] # increasing the size of the circles
	else:	
		cost = COST_MAP[sys.argv[1]][l]

	radius = math.sqrt(cost/math.pi)*100

	if l in pageloadtime:
		if pageloadtime[l] > 0:
			m.plot(x,y,'o', markersize=radius, color=colors[color_index], alpha=0.8, markeredgecolor="#000000", mew=0.5)
		else:
			print (l , pageloadtime[l])
	else:
		m.plot(x,y,'o', markersize=2, color="#000000", alpha=0.8)
		pageloadtime[l] = -1

	if l in loc_text:
		tx, ty = m(loc_text[l][0], loc_text[l][1])
		if loc_text[l][0] < 25:
			if location[2] > 0:
				angle = "angle,angleA=-90,angleB=-45"
			else:
				angle = "angle,angleA=-90,angleB=45"
		else:
			if location[2] > 0:
				angle = "angle,angleA=-90,angleB=45"
			else:
				angle = "angle,angleA=-90,angleB=-45"
	else:
		tx, ty = x, y
		angle = "angle3,angleA=-45,angleB=-90"

	if location[2] < 0:
		if pageloadtime[l] > 0:
			ax.annotate("{0}    ".format(l.split(",")[0]), xy=(x,y), xytext=(tx, -95728),rotation = 90,
            arrowprops=dict(arrowstyle="->", lw=0.2,
                            connectionstyle=angle), va = "top", ha="left", size=60)

			if loc_flag[l] != "":
				arr_lena = mpimg.imread('./flags/{0}.png'.format(loc_flag[l]))
				imagebox = OffsetImage(arr_lena, zoom=0.1)
				ab = AnnotationBbox(imagebox, (tx+210000, 0),pad=0.05)
				ax.add_artist(ab)
	else:
		if pageloadtime[l] > 0:
			ax.annotate("    {0}".format(l.split(",")[0]), xy=(x,y), xytext=(tx, 20695728),rotation = 90,
            arrowprops=dict(arrowstyle="->", lw=0.2,
                            connectionstyle=angle), va = "bottom", ha="left", size=60)

			if loc_flag[l] != "":
				arr_lena = mpimg.imread('./flags/{0}.png'.format(loc_flag[l]))
				imagebox = OffsetImage(arr_lena, zoom=0.1)
				ab = AnnotationBbox(imagebox, (tx+210000, 20567000),pad=0.05)
				ax.add_artist(ab)

x, y = m(location[0], location[1])

custom_lines = [Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[0], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[1], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[2], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[3], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[4], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[5], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[6], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[7], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[8], color="none", markeredgewidth=0.1),Line2D([0], [0], marker='o', markersize=60, markerfacecolor=colors[9], color="none", markeredgewidth=0.1)]

l0 = plt.scatter([],[], s=500, edgecolors='k', color="#E8E8E8")
l1 = plt.scatter([],[], s=15000, edgecolors='k', color="#E8E8E8")
l2 = plt.scatter([],[], s=36000, edgecolors='k', color="#E8E8E8")
l3 = plt.scatter([],[], s=80000, edgecolors='k', color="#E8E8E8")
l4 = plt.scatter([],[], s=160000, edgecolors='k', color="#E8E8E8")

leg = plt.legend([l0, l1, l2, l3, l4], labels[sys.argv[1]], ncol=1, frameon=True, fontsize=60, handlelength=6, handleheight=8, loc = 8, scatterpoints = 1, bbox_to_anchor=(-0.03, -0.1))

for t in leg.get_texts(): 
    t.set_position((0,110))

leg.set_title('Cost per Gigabyte (USD)',prop={'size':60})
leg.get_title().set_position((0, 0))
leg.get_frame().set_linewidth(10)

# print limits
leg2 = []
leg2 = ["<= {0:.2f} s".format(limits[0])]
old = limits[0]
for i in limits[1:]:
	leg2.append("{0:.2f} - {1:.2f} s".format(old, i))
	old = i
leg2.append("> {0:.2f} s".format(i))
b = ax.legend(custom_lines, leg2, loc='center right', bbox_to_anchor=(0.055, 0.9), fontsize=60, title="",handlelength=4)
b.set_title('Page load time (s)\n',prop={'size':60})
b.get_frame().set_linewidth(10)

ax.add_artist(leg)
ax.add_artist(b)

bbox_props = dict(boxstyle="larrow,pad=0.5", fc="w", ec="k", lw=2)

plt.gcf().text(0.05, 0.715, "a", fontsize=110, weight='bold')
plt.savefig(f"figures/map_{sys.argv[1]}.pdf")