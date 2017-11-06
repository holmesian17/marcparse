import pymarc

xml = 'AU_MARC/PGA-Australiana.xml'



def getMarcInfo(record):
    print('<record>')
    
    try:
        title = record['245']['a']
        print('<title>' + title + '</title>')
    except:
        pass

    try:
        title2 = record['245']['b']  
        print('<title2>' + title2 + '</title>')
    except:
        pass

    try:
        author = record['100']['a']
        print('<author>' + author + '</author>')
    except:
        pass

    try:
        authorDates = record['100']['d']
        print('<authorDates>' + authorDates + '</authorDates>')
    except:
        pass
    
    try:
        isbn = record['020']['a']
        print('<isbn>' + isbn + '</isbn>')
    except:
        pass

    try:
        LCCN = record['050']['a']
        print('<LCCN>' + LCCN + '</LCCN>')
    except:
        pass

    try:    
        LCCN2 = record ['050']['b']
        print('<LCCN2>' + LCCN2 + '</LCCN2>')
    except:
        pass

    try:
        dewey = record['082']['a']
        print( '<dewey>' + dewey + '</dewey>' )
    except:
        pass

    try:
        placePub = record['260']['a']
        print('<placePub>' + placePub + '</placePub>')
    except:
        pass

    try:
        publisher = record['260']['b']
        print('<publisher>' + publisher + '</publisher>')
    except:
        pass

    try:
        pubDate = record['260']['c']
        print('<pubDate>' + pubDate + '</pubDate>')
    except: 
        pass

    try:
        extent = record['300']['a']
        print('<extent>' + extent + '</extent>' )
    except:
        pass

    try:
        itemDetails = record['300']['b']
        print('<itemDetails>' + itemDetails + '</itemDetails>')
    except:
        pass

    try:        
        dimensions = record['300']['c']
        print('<dimensions>' + dimensions + '</dimensions>')
    except:
        pass

    try:
        generalNote = record['500']['a']
        print('<generalNote>' + generalNote + '</generalNote>')
    except:
        pass

    try:
        summary = record['520']['a']
        print('<summary>' + summary + '</summary>')
    except:
        pass

    try:
        subjectHeading = record['650']
        print('<subjectHeading>' + subjectHeading + '</subjectHeading>')
    except:
        pass

    print('</record>')


print('<collection>')
pymarc.map_xml(getMarcInfo, xml)
print('</collection>')
