from time import perf_counter
from urllib import request


class WebPage:
    def __init__(self, url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
        
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        # we'll lazy load the page - i.e. we wait until some property is requested
        
    @property
    def page(self):
        if self._page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page is None:
            # need to first download the page
            self.download_page()
        return self._page_size
        
    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs
            
    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        
        self._page_size = len(self._page)
        self._load_time_secs = end_time - start_time