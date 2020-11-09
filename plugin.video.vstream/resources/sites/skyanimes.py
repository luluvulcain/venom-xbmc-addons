#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
# Makoto
from resources.lib.gui.hoster import cHosterGui
from resources.lib.gui.gui import cGui
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.comaddon import progress, VSlog
 
SITE_IDENTIFIER = 'skyanimes'
SITE_NAME = 'Sky-Animes'
SITE_DESC = 'Animés, Dramas en Direct Download'
 
URL_MAIN = 'http://www.sky-animes.com/'
 
STREAM = 'index.php?file=Media&nuked_nude=index&op=do_dl&dl_id='
 
URL_SEARCH_SERIES = (URL_MAIN + 'index.php?file=Search&op=mod_search&searchtype=matchand&autor=&module=Download&limit=100&main=', 'showEpisode')
FUNCTION_SEARCH = 'showEpisode'
 
ANIM_VOSTFRS = (URL_MAIN + '', 'showCatA')
SERIE_VOSTFRS = (URL_MAIN + '', 'showCatD')
MOVIE_GENRESA = (True, 'showGenresA') 
MOVIE_GENRESD = (True, 'showGenresD')
def load():
    oGui = cGui()
 
    oOutputParameterHandler = cOutputParameterHandler() #appelle la fonction pour sortir un parametre
    oOutputParameterHandler.addParameter('siteUrl', URL_SEARCH_SERIES[0]) # sortie du parametres siteUrl n'oubliez pas la Majuscule
    oGui.addTV(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', '', '', oOutputParameterHandler)
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', ANIM_VOSTFRS[0])
    oGui.addTV(SITE_IDENTIFIER, ANIM_VOSTFRS[1], 'Animés', 'animes.png', '', '', oOutputParameterHandler)
 
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFRS[0])
    oGui.addTV(SITE_IDENTIFIER, SERIE_VOSTFRS[1], 'Dramas', 'vostfr.png', '', '', oOutputParameterHandler)
    
    
 
    oGui.setEndOfDirectory()
 
def showCatA():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRESA[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRESA[1], 'Animes (Genres)', 'genres.png', oOutputParameterHandler)
 
    
    liste = []
    liste.append( ['En Cours', URL_MAIN + 'streaming-animes-en-cours?p=-1'] )
    liste.append( ['Terminés', URL_MAIN + 'download-animes-termines?p=-1'] )
 
    for sTitle, sUrl in liste:
 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addTV(SITE_IDENTIFIER, 'showSeries', sTitle, 'anime.png', '', '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
 
def showCatD():
    oGui = cGui()
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRESD[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRESD[1], 'Dramas (Genres)', 'genres.png', oOutputParameterHandler)
    
    liste = []
    liste.append( ['En Cours', URL_MAIN + 'download-dramas-en-cours?p=-1'] )
    liste.append( ['Terminés', URL_MAIN + 'download-dramas-termines?p=-1'] )
 
    for sTitle, sUrl in liste:
 
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl)
        oGui.addTV(SITE_IDENTIFIER, 'showSeries', sTitle, 'vostfr.png', '', '', oOutputParameterHandler)
 
    oGui.setEndOfDirectory()
 
def showGenresA():
    oGui = cGui()
    oParser = cParser()
        
    sUrl = URL_MAIN + 'streaming-animes-en-cours'

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sStart = 'id="id_genre"'
    sEnd = '<select id="triGenre"'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    
    sPattern = '<a href="([^"]+)">([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        #total = len(aResult[1])
        #progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            #progress_.VSupdate(progress_, total)
            #if progress_.iscanceled():
                #break

            
            sUrl = URL_MAIN + aEntry[0]
            sTitle = aEntry[1]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            #oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            
            oGui.addTV(SITE_IDENTIFIER, 'showSeries', sTitle, '', '', '', oOutputParameterHandler)
            

            

        #progress_.VSclose(progress_)

        

        oGui.setEndOfDirectory()
    
def showGenresD():
    oGui = cGui()
    oParser = cParser()
        
    sUrl = URL_MAIN + 'download-dramas-en-cours?p=-1'

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    sStart = 'id="id_genre"'
    sEnd = '<select id="triGenre"'
    sHtmlContent = oParser.abParse(sHtmlContent, sStart, sEnd)
    
    sPattern = '<a href="([^"]+)">([^<]+)'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        #total = len(aResult[1])
        #progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            #progress_.VSupdate(progress_, total)
            #if progress_.iscanceled():
                #break

            
            sUrl = URL_MAIN + aEntry[0]
            sTitle = aEntry[1]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            #oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            
            oGui.addTV(SITE_IDENTIFIER, 'showSeries', sTitle, '', '', '', oOutputParameterHandler)
            

            

        #progress_.VSclose(progress_)

        

        oGui.setEndOfDirectory()

def showSearch(): #fonction de recherche
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
 
    sSearchText = oGui.showKeyBoard() #appelle le clavier xbmc
    if (sSearchText != False):
        sUrl = sUrl + sSearchText.replace(' ','+') #modifie l'url de recherche
        showEpisode(sUrl) #appelle la fonction qui pourra lire la page de resultats
        oGui.setEndOfDirectory()
        return
 
def showSeries():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl').replace('+' , '%2B')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 
    oParser = cParser()
    sPattern = '<a href="([^<]+)"><img src="(.+?)" width.+?alt="(.+?)".+?></a>'
 
    aResult = oParser.parse(sHtmlContent, sPattern)
 
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
 
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
 
        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
 
            sTitle = aEntry[2]
            sUrl2 = URL_MAIN + aEntry[0]
            sThumb = URL_MAIN + aEntry[1].replace(' ','%20')
            sDesc = ""
            
            sTitle = sTitle.replace(', telecharger en ddl', '')
 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
 
            oGui.addTV(SITE_IDENTIFIER, 'showEpisode', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
 
        progress_.VSclose(progress_)
 
        oGui.setEndOfDirectory()
 
def showEpisode(sSearch = ''):
    oGui = cGui()
 
    if sSearch:
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl')
        sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
        sThumb = oInputParameterHandler.getValue('sThumb')
 
    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
 
    oParser = cParser()
    if sSearch:
        sPattern = '<a href=".+?id=([^"]+)"><b>(.+?)</b>'
    else:
        sPattern = '<td style="padding-left: 12px;"><a href="([^"]+)".+?><b><img.+?>(.+?)</b>.+?</a>'
 
    aResult = oParser.parse(sHtmlContent, sPattern)
    VSlog(aResult)
 
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)
 
    if (aResult[0] == True):
        total = len(aResult[1])
        progress_ = progress().VScreate(SITE_NAME)
 
        for aEntry in sorted(aResult[1]):
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break
 
            if sSearch:
                sTitle = aEntry[1]
                sTitle,sTitle1 = sTitle.replace('1080p','').replace('BD','').replace('V2','').replace('FIN','').replace('Fin','').replace('fin','').replace('OAV','').replace('Bluray','').replace('Blu-Ray','').rstrip().rsplit(' ',1)
                sTitle = 'E'+sTitle1 + ' '+sTitle
                sUrl2 = URL_MAIN + STREAM + aEntry[0]
                sThumb = ""
                sDesc = ""
            else:
                sTitle = aEntry[1]
                sTitle,sTitle1 = sTitle.replace('1080p','').replace('BD','').replace('V2','').replace('FIN','').replace('Fin','').replace('fin','').replace('OAV','').replace('Bluray','').replace('Blu-Ray','').rstrip().rsplit(' ',1)
                sTitle = 'E'+sTitle1 + ' '+sTitle
                sUrl2 = URL_MAIN + STREAM + aEntry[0]
 
                sUrl2 = sUrl2.replace('#','')
 
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            oGui.addTV(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumb, '', oOutputParameterHandler)
 
        progress_.VSclose(progress_)
    if not sSearch:
        oGui.setEndOfDirectory()
 
def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
 
    oHoster = cHosterGui().checkHoster('m3u8')
 
    if (oHoster != False):
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sUrl, sThumb)
 
    oGui.setEndOfDirectory()