let Philadelphia;
let AshurstRd;
let HaverfordAve;
let BrocktonRd;
let KimberlyDr;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  Philadelphia = new Map(document.getElementById("map"), {
    center: { lat: 39.952043, lng: -75.163988 },
    zoom: 13,
  });

  AshurstRd = new google.maps.Marker({
    position: { lat:  39.975028, lng: -75.273134 },
    map: Philadelphia,
    title: "AshurstRd",

  });

 HaverfordAve = new google.maps.Marker({
    position: { lat:   39.980086 , lng:-75.269204 },
    map: Philadelphia,
    title: "HaverfordAve",
  });

  BrocktonRd = new google.maps.Marker({
    position: { lat: 39.974505, lng: -75.260260},
    map: Philadelphia,
    title: "BrocktonRd",

  });

   KimberlyDr = new google.maps.Marker({
    position: { lat: 39.972062, lng: -75.263627 },
    map: Philadelphia,
    title: "KimberlyDr",

  });

   const infoWindow = new google.maps.InfoWindow({
     content: "<p>Construction Zone: AshurstRd--> HaverfordAve--> BrocktonRd--> KimberlyDr</p>"
   });
   infoWindow.open(Philadelphia,AshurstRd);

}

// Call the initMap function when the Google Maps API is loaded
initMap();
