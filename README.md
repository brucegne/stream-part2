# stream-part2
Second app
### Let's try another * commit* and see how it goes

Hey, got some databases working with streamlit !!!
Deta
Firestore
Google Sheets


def addUp(data):
    recs = data['records']
    for rec in recs:
        if rec['location'] in locations:
            locations[rec['location']] = locations[rec['location']] + 1
        else:
            locations[rec['location']] = 1

    topZone.header(str(recsProc))

for i in range(15):
    result = requests.get("https://hfpintranet.appspot.com/dailyjson?pageno=%s" % i)
    results = json.loads(result.text)
    if(len(results) != 0):
        recs = results['records']
        for rec in recs:
            db.put(rec)
            fullSet.append(rec)
        topZone.header(len(fullSet))    
    else:
        pass




