import urllib

from bs4 import BeautifulSoup
import requests
import webbrowser
import re

searchterms = [
"abingdon+herald",
"accrington+observer",
"northumberland+gazette",
"alton+herald",
"andover+advertiser",
"pulmans+weekly+news",
"view+from+axminster",
"bucks+herald",
"banbury+guardian",
"the+barnsley+chronicle",
"the+independent",
"north+west+evening+mail",
"basildon+yellow+advertiser",
"basingstoke+gazette",
"basingstoke+observer",
"bedfordshire+on+sunday",
"bicester+advertiser",
"bicester+review",
"birmingham+post",
"sports+argus",
"sunday+mercury",
"blackpool+gazette",
"bolton+news",
"bootle+champion",
"boston+standard",
"boston+target",
"bourne+local",
"stamford+mercury",
"bracknell+news",
"bracknell+midweek",
"bracknell+standard",
"the+bradfordian",
"telegraph+and+argus",
"brentwood+gazette",
"bridlington+free+press",
"the+bridport+news",
"brighouse+echo",
"bristol+evening+post",
"bristol+observer",
"bromsgrove+standard",
"burnley+express",
"burton+mail",
"bury+times",
"bury+free+press",
"buxton+advertiser",
"cambridge+evening+news",
"canterbury+times",
"kentish+gazette",
"news+and+star",
"cumberland+news",
"cumbrian+gazette",
"bucks+examiner",
"cheshunt",
"chester+and+district+standard",
"chester+chronicle",
"chester+evening+leader",
"chester+mail",
"chew+valley+gazette",
"chichester+observer",
"chorley+citizen",
"chorley+guardian",
"essex+county+standard",
"congleton+chronicle",
"cotswold+journal",
"coventry+advertiser",
"coventry+observer",
"coventry+telegraph",
"crawley+news",
"crawley+observer",
"crewe+chronicle",
"crewe+guardian",
"south+cheshire+mail",
"croydon+advertiser",
"croydon+guardian",
"croydon+post",
"daventry+express",
"derby+evening+telegraph",
"derby+express",
"derby+trader",
"dewsbury+reporter",
"diss+express",
"doncaster+free+press",
"droitwich+standard",
"dudley+news",
"express+and+star",
"durham+times",
"eastbourne+gazette",
"eastbourne+herald",
"evesham+journal",
"express+and+echo",
"exmouth+journal",
"farnborough+news",
"star+courier",
"faversham+news",
"faversham+times",
"fleetwood+weekly+news",
"formby+visitor",
"gainsborough+standard",
"garstang+courier",
"glossop+advertiser",
"glossop+chronicle",
"glossop+gazette",
"gloucester+citizen",
"gloucestershire+echo",
"stroud+life",
"goole+times",
"grantham+journal",
"grimsby+telegraph",
"surrey+advertiser",
"halifax+evening+courier",
"harlow+scene",
"harlow+star",
"harrogate+advertiser",
"hartlepool+mail",
"hastings+independent+press",
"hebden+bridge+times",
"hemel+hempstead+gazette",
"herald+express",
"henley+standard",
"hereford+times",
"hertfordshire+mercury",
"hertfordshire+mercury",
"watford+observer",
"welwyn+hatfield+times",
"heywood+advertiser",
"hexham+courant",
"holme+valley+express",
"midweek+herald",
"view+from+honiton",
"hucknall+and+bulwell+dispatch",
"colne+valley+chronicle",
"huddersfield+daily+examiner",
"huddersfield+weekly+news",
"ilkley+gazette",
"sheerness+times+guardian",
"sheppey+gazette",
"isle+of+wight+county+press",
"wight+insight",
"keighley+news",
"westmorland+gazette",
"hull+daily+mail",
"kingston+guardian",
"surrey+comet",
"knutsford+guardian",
"lancaster+guardian",
"langport+leveller",
"leeds+express",
"yorkshire+evening+post",
"yorkshire+post",
"the+yorkshire+reporter",
"leek+post+and+times",
"your+leek+paper",
"leicester+mercury",
"leicester+advertiser",
"leigh+journal",
"leigh+reporter",
"leyland+guardian",
"lichfield+mercury",
"liverpool+daily+post",
"liverpool+echo",
"mersey+reporter",
"bexley+mercury",
"bexley+times",
"brixton+bugle",
"camden+gazette",
"camden+new+journal",
"croydon+advertiser",
"croydon+guardian",
"croydon+post",
"ealing+gazette",
"ealing+leader",
"ealing+informer",
"east+london+advertiser",
"enfield+advertiser",
"enfield+gazette",
"evening+standard",
"hackney+gazette",
"hampstead+and+highgate+express",
"haringey+advertiser",
"harrow+informer",
"harrow+leader",
"havering+yellow+advertiser",
"hounslow+borough+chronicle",
"ilford+recorder",
"islington+gazette",
"kilburn+times",
"kingston+guardian",
"london+lite",
"the+londoner",
"muswell+hill+journal",
"newham+recorder",
"richmond+and+twickenham+times",
"romford+and+havering+post",
"south+london+press",
"staines+informer",
"staines+leader",
"surrey+comet",
"surrey+herald",
"surrey+mirror+advertiser",
"sutton+guardian",
"uxbridge+gazette",
"waltham+forest+news",
"wanstead+and+woodford+guardian",
"loughborough+echo",
"loughborough+mail",
"loughborough+trader+xtra",
"loughton+guardian",
"luton+on+sunday",
"view+from+lyme+regis",
"the+macclesfield+express",
"the+macclesfield+times",
"maidenhead+advertiser",
"malvern+gazette",
"manchester+evening+news",
"market+drayton+advertiser",
"harborough+mail",
"market+rasen+mail",
"middleton+guardian",
"onemk",
"west+somerset+free+press",
"newbury+weekly+news",
"evening+chronicle",
"sunday+sun",
"newtownabbey+times",
"northampton+mercury",
"northwich+guardian",
"north+yorkshire+news",
"norwich+evening+news",
"newark+advertiser",
"nottingham+evening+post",
"worksop+guardian",
"oldham+advertiser",
"oldham+evening+chronicle",
"ormskirk+and+west+lancashire+advertiser",
"ormskirk+and+west+lancashire+champion",
"oxford+mail",
"oxford+star",
"oxford+times",
"cumberland+and+westmorland+herald",
"peterlee+star",
"plymouth+evening+herald",
"western+morning+news",
"sports+mail",
"prestwich+and+whitefield+guide",
"reading+chronicle",
"reading+evening+post",
"retford+times",
"retford+trader+and+guardian",
"ripon+gazette",
"rochdale+observer",
"romford+recorder",
"romsey+advertiser",
"rotherham+advertiser",
"rugby+advertiser",
"rugby+observer",
"salford+advertiser",
"scarborough+evening+news",
"scarborough+mercury",
"scunthorpe+telegraph",
"selby+post",
"selby+star",
"selby+times",
"seaford+gazette",
"sheffield+star",
"shrewsbury+chronicle",
"east+kent+gazette",
"sleaford+standard",
"sleaford+target",
"solent+times",
"slough+express",
"somerton+sentinel",
"shields+gazette",
"southport+champion",
"southport+reporter",
"southport+visiter",
"stamford+mercury",
"sheffield+telegraph",
"stockport+express",
"stowmarket+mercury",
"stratford+herald",
"stratford+observer",
"stroud+news+and+journal",
"sunderland+echo",
"sutton+coldfield+observer",
"swindon+advertiser",
"swindon+star",
"tameside+advertiser",
"tameside+reporter",
"tamworth+herald",
"the+somerset+county+gazette",
"the+taunton+times",
"melton+times",
"wakefield+express",
"wakefield+express+extra",
"warminster+journal",
"warrington+guardian",
"wetherby+news",
"whitby+gazette",
"whitchurch+herald",
"widnes+weekly+news",
"widnes+world",
"wigan+evening+post",
"wigan+observer",
"wigan+reporter",
"gazette+and+herald",
"wiltshire+times",
"winchester+today",
"wirral+globe",
"wirral+news",
"the+wokingham+paper",
"express+and+star",
"worcester+news",
"kidderminster+shuttle",
"worksop+guardian",
"worksop+trader",
"western+gazette",
"york+press",
]


newspapers = {}

for site in searchterms:

    text = urllib.parse.quote_plus(site)

    url = f'https://www.google.co.uk/search?q={text}'

    response = requests.get(url)


    soup = BeautifulSoup(response.text)
    g_results = soup.find_all(class_='g')
    first_result = list(g_results)[0]

    d = str(first_result.find('a')['href'][7:])
    d = urllib.parse.urlparse(d)

    newspapers[site] = d.netloc

print(newspapers)