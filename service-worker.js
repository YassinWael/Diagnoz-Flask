// Install the service worker
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('offline').then(function(cache) {
      return cache.addAll([
        '/',
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
      ]);
    })
  );
});

// Fetch the content using the service worker
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.match(event.request).then(function(response) {
      return response || fetch(event.request);
    })
  );
});