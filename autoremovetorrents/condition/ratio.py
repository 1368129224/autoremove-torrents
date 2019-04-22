#-*- coding:utf-8 -*-

from .base import Comparer
from .base import Condition
from ..torrentstatus import TorrentStatus

class RatioCondition(Condition):
    def __init__(self, r, comp = Comparer.GT):
        Condition.__init__(self) # Initialize remain and remove list
        self._ratio = r
        self._comparer = comp

    def apply(self, torrents):
        for torrent in torrents:
            if torrent.status == TorrentStatus.Uploading and \
                self.compare(torrent.ratio, self._ratio, self._comparer):
                self.remove.add(torrent)
            else:
                self.remain.add(torrent)