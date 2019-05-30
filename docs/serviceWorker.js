var CACHE_NAME  = "PTEST-cache-v1";
var urlsToCache = [
    "https://kazukazuprogram.github.io/swtest/",
    "https://kazukazuprogram.github.io/swtest/index.html"
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(
            function(cache){
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
      caches.match(event.request)
        .then(
        function (response) {
            if (response) {
                return response;
            }
            return fetch(event.request);
        })
    );
});
