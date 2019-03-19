// Easy way to wait for all videos to load before start playing

var promises = [];
function makePromise(i, video) {
  promises[i] = new $.Deferred();
  // This event tells us video can be played all the way through, without stopping or buffering
  video.oncanplaythrough = function() {
    // Resolve the promise
    promises[i].resolve();
  }
}
// Pause all videos and create the promise array
$('video').each(function(index){
  this.pause();
  makePromise(index, this);
})

// Wait for all promises to resolve then start playing
$.when.apply(null, promises).done(function () {
  $('video').each(function(){
    this.play();
  });
});