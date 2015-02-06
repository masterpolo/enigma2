# Embedded file name: /usr/lib/enigma2/python/Components/Renderer/dmmNextEvent.py
from Components.VariableText import VariableText
from enigma import eLabel, eEPGCache
from Renderer import Renderer
from time import localtime

class dmmNextEvent(Renderer, VariableText):

    def __init__(self):
        Renderer.__init__(self)
        VariableText.__init__(self)
        self.epgcache = eEPGCache.getInstance()

    GUI_WIDGET = eLabel

    def changed(self, what):
        if not self.suspended:
            ref = self.source.service
            info = ref and self.source.info
            if info is None:
                self.text = ''
                return
            ENext = ''
            eventNext = self.epgcache.lookupEvent(['IBDCTSERNX', (ref.toString(), 1, -1)])
            if eventNext:
                if eventNext[0][4]:
                    t = localtime(eventNext[0][1])
                    duration = '%d min' % (eventNext[0][2] / 60)
                    ENext = _('Next:') + ' ' + '%02d:%02d - %s\n%s' % (t[3],
                     t[4],
                     duration,
                     eventNext[0][4])
            self.text = ENext
        return