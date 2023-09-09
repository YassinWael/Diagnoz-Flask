// Function to handle the installation of the service worker

console.log('Starting service worker')
function handleInstall(event) {
    event.waitUntil(
      openCache().then(function(cache) {
        return cacheAddAll(cache, [
          '/',
          'templates/*',
          'static/*',
          'dataset/*'

        ]);
      })
    );
  }
  
  // Function to open the cache
  function openCache() {
    return caches.open('my-cache');
  }
  
  // Function to add multiple files to the cache
  function cacheAddAll(cache, files) {
    console.log(files)
    return cache.addAll(files);
  }
  
  // Function to handle the fetch event
  function handleFetch(event) {
    event.respondWith(
      matchCache(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
  }
  
  // Function to check if the requested resource is available in the cache
  function matchCache(request) {
    return caches.match(request);
  }
  
  // Event listener for the 'install' event
  self.addEventListener('install', handleInstall);
  
  // Event listener for the 'fetch' event
  self.addEventListener('fetch', handleFetch);
  