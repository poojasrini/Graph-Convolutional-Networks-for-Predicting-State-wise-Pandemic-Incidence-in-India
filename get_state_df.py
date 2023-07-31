import sys
import pandas as pd
import numpy as np

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd

TESTDATA = StringIO("""Rank,State or union territory,Population,National Share (%),Decadal growth(2001–2012),Rural population,Percent rural,Urban population,Percent urban,Area[16],Density[a],Sex ratio
1,Uttar Pradesh,"199,812,341",16.51%,20.2%,"155,317,278",77.73%,"44,495,063",22.27%,"240,928 km2 (93,023 sq mi)","828/km2 (2,140/sq mi)",912
2,Maharashtra,"112,374,333",9.28%,20.0%,"61,556,074",54.78%,"50,818,259",45.22%,"307,713 km2 (118,809 sq mi)",365/km2 (950/sq mi),929
3,Bihar,"104,099,452",8.6%,25.4%,"92,341,436",88.71%,"11,758,016",11.29%,"94,163 km2 (36,357 sq mi)","1,102/km2 (2,850/sq mi)",918
4,West Bengal,"91,276,115",7.54%,13.8%,"62,183,113",68.13%,"29,093,002",31.87%,"88,752 km2 (34,267 sq mi)","1,029/km2 (2,670/sq mi)",953
5,Madhya Pradesh,"72,626,809",6%,16.3%,"52,557,404",72.37%,"20,069,405",27.63%,"308,245 km2 (119,014 sq mi)",236/km2 (610/sq mi),931
6,Tamil Nadu,"72,147,030",5.96%,15.6%,"37,229,590",51.6%,"34,917,440",48.4%,"130,051 km2 (50,213 sq mi)","555/km2 (1,440/sq mi)",996
7,Rajasthan,"68,548,437",5.66%,21.3%,"51,500,352",75.13%,"17,048,085",24.87%,"342,239 km2 (132,139 sq mi)",201/km2 (520/sq mi),928
8,Karnataka,"61,095,297",5.05%,15.6%,"37,469,335",61.33%,"23,625,962",38.67%,"191,791 km2 (74,051 sq mi)",319/km2 (830/sq mi),973
9,Gujarat,"60,439,692",4.99%,19.3%,"34,694,609",57.4%,"25,745,083",42.6%,"196,024 km2 (75,685 sq mi)",308/km2 (800/sq mi),919
10,Andhra Pradesh,"49,577,103[b]",4.1%,11.0%,"34,966,693",70.53%,"14,610,410",29.47%,"162,968 km2 (62,922 sq mi)",303/km2 (780/sq mi),993
11,Odisha,"41,974,219",3.47%,14.0%,"34,970,562",83.31%,"7,003,656",16.69%,"155,707 km2 (60,119 sq mi)",269/km2 (700/sq mi),979
12,Telangana,"35,003,674",2.89%,13.58%,"21,395,009",61.12%,"13,608,665",38.88%,"112,077 km2 (43,273 sq mi)",312/km2 (810/sq mi),988
13,Kerala,"33,406,061",2.76%,4.9%,"17,471,135",52.3%,"15,934,926",47.7%,"38,863 km2 (15,005 sq mi)","859/km2 (2,220/sq mi)","1,084"
14,Jharkhand,"32,988,134",2.73%,22.4%,"25,055,073",75.95%,"7,933,061",24.05%,"79,714 km2 (30,778 sq mi)","414/km2 (1,070/sq mi)",948
15,Assam,"31,205,576",2.58%,17.7%,"26,807,034",85.90%,"4,398,542",14.10%,"78,438 km2 (30,285 sq mi)","398/km2 (1,030/sq mi)",958
16,Punjab,"27,743,338",2.29%,13.89%,"17,344,192",62.52%,"10,399,146",37.48%,"50,362 km2 (19,445 sq mi)","551/km2 (1,430/sq mi)",895
17,Chhattisgarh,"25,545,198",2.11%,22.6%,"19,607,961",76.76%,"5,937,237",23.24%,"135,191 km2 (52,198 sq mi)",189/km2 (490/sq mi),991
18,Haryana,"25,351,462",2.09%,19.9%,"16,509,359",65.12%,"8,842,103",34.88%,"44,212 km2 (17,070 sq mi)","573/km2 (1,480/sq mi)",879
UT1,NCT of Delhi,"16,787,941",1.39%,21.2%,"419,042",2.5%,"16,368,899",97.5%,"1,484 km2 (573 sq mi)","11,297/km2 (29,260/sq mi)",868
UT2,Jammu and Kashmir,"12,267,032",1.01%,23.6%,"9,064,220",73.89%,"3,202,812",26.11%,"42,241 km2 (16,309 sq mi)[c]",297/km2 (770/sq mi),890
19,Uttarakhand,"10,086,292",0.83%,18.8%,"7,036,954",69.77%,"3,049,338",30.23%,"53,483 km2 (20,650 sq mi)",189/km2 (490/sq mi),963
20,Himachal Pradesh,"6,864,602",0.57%,12.9%,"6,176,050",89.97%,"688,552",10.03%,"55,673 km2 (21,495 sq mi)",123/km2 (320/sq mi),972
21,Tripura,"3,673,917",0.3%,14.8%,"2,712,464",73.83%,"961,453",26.17%,"10,486 km2 (4,049 sq mi)",350/km2 (910/sq mi),960
22,Meghalaya,"2,966,889",0.25%,27.9%,"2,371,439",79.93%,"595,450",20.07%,"22,429 km2 (8,660 sq mi)",132/km2 (340/sq mi),989
23,Manipur,"2,570,390",0.21%,18.6%,"1,793,875",69.79%,"776,515",30.21%,"22,327 km2 (8,621 sq mi)",122/km2 (320/sq mi),992
24,Nagaland,"1,978,502",0.16%,−0.6%,"1,407,536",71.14%,"570,966",28.86%,"16,579 km2 (6,401 sq mi)",119/km2 (310/sq mi),931
25,Goa,"1,458,545",0.12%,8.2%,"551,731",37.83%,"906,814",62.17%,"3,702 km2 (1,429 sq mi)","394/km2 (1,020/sq mi)",973
26,Arunachal Pradesh,"1,383,727",0.11%,26.0%,"1,066,358",77.06%,"317,369",22.94%,"83,743 km2 (32,333 sq mi)",17/km2 (44/sq mi),938
UT3,Puducherry,"1,247,953",0.1%,28.1%,"395,200",31.67%,"852,753",68.33%,479 km2 (185 sq mi),"2,598/km2 (6,730/sq mi)","1,037"
27,Mizoram,"1,097,206",0.09%,23.5%,"525,435",47.89%,"571,771",52.11%,"21,081 km2 (8,139 sq mi)",52/km2 (130/sq mi),976
UT4,Chandigarh,"1,055,450",0.09%,17.2%,"28,991",2.75%,"1,026,459",97.25%,114 km2 (44 sq mi),"9,252/km2 (23,960/sq mi)",818
28,Sikkim,"610,577",0.05%,12.9%,"456,999",74.85%,"153,578",25.15%,"7,096 km2 (2,740 sq mi)",86/km2 (220/sq mi),890
UT5,Dadra and Nagar Haveli and Daman and Diu,"585,764",0.05%,55.1%,"243,510",41.57%,"342,254",58.43%,603 km2 (233 sq mi),"970/km2 (2,500/sq mi)",711
UT6,Andaman and Nicobar Islands,"380,581",0.03%,6.9%,"237,093",62.3%,"143,488",37.7%,"8,249 km2 (3,185 sq mi)",46/km2 (120/sq mi),876
UT7,Ladakh,"274,000",0.02%,17.8%,"43,840",16%,"230,160",84%,"96,701 km2 (37,336 sq mi)[e]",2.8/km2 (7.3/sq mi),853
UT8,Lakshadweep,"64,473",0.01%,6.3%,"14,141",21.93%,"50,332",78.07%,32 km2 (12 sq mi),"2,013/km2 (5,210/sq mi)",946
Total,India,"1,210,569,573",100%,17.7%,"833,463,448",68.84%,"377,106,125",31.16%,"3,287,240 km2 (1,269,210 sq mi)[f]",382/km2 (990/sq mi),940""")

for_vals = [4745181, 5528704, 1093141, 1656145, 
       327958, 6866327, 1605560, 608754, 595607, 280356, 
       115128, 323326, 1189771, 176043, 26878, 1101343,
       6817, 48046, 2983436, 57920, 152273, 382876, 154405, 25813, 
       13608, 5577, 937113, 7825, 149919, 2249, 44132, 133388, 7369, 38652]

df = pd.read_csv(TESTDATA, sep=",")

df = df.drop([33, 35, 36]).reset_index(drop=True)
df['Density[a]'] = df['Density[a]'].str.split('/').apply(lambda ls: ls[0]).str.replace(',', '').apply(lambda val: np.float64(val))
df['Percent urban'] = df['Percent urban'].str.replace('%', '').astype(np.float32)
df['Percent rural'] = df['Percent rural'].str.replace('%', '').astype(np.float32)
df['National Share (%)'] = df['National Share (%)'].str.replace('%', '').astype(np.float32)
df['Foreign Visits'] = for_vals

df['Health Index'] = [29.16,64.53,32.42,58.25,38.69,60.5,43.23,61.77,
63.72,65.31,36.35,59.42,74.65,53.67,50.02,63.41,53.97,54.08,60.73,62.92,
39.61,63.1,46.38,55.95,60.59,38.51,51.9,46.07,31.87,74.98,67.08,50.5,60.73,53.76]

df.to_csv('./data/state_data.csv', index=False)