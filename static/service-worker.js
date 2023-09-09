const CACHE_NAME = 'my-site-cache-v1';
const urlsToCache = [
"/template/about.html",
"/template/choose.html",
"/template/contact.html",
"/template/diseases.html",
"/template/download.html",
"/template/home.html",
"/template/layout.html",
"/template/learn_more.html",
"/template/symptoms.html",
"/template/symptoms_set.html",
"/datasets/dataset.csv",
"/datasets/symptom_Description.csv",
"/static/style.css",
"/static/images/512Logo.png",
"/static/images/apple-icon-180.png",
"/static/images/download-app.png",
"/static/images/manifest-icon-192.maskable.png",
"/static/images/manifest-icon-512.maskable.png"
];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        console.log("caching")
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request)
      .then(function(response) {
        // Cache hit - return response
        if (response) {
          return response;
        }
        return fetch(event.request);
      }
    )
  );
});