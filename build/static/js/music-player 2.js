// Get Elements
const playButton = document.getElementById("play-button");
const musicPlayer = document.getElementById("music-player");
const musicIcon = document.getElementById("music-play-icon");

// Get Playlist
const playlist = document.getElementById('playlist');
const links = playlist.getElementsByTagName('a');

var hrefs = [];
for (var i = 0; i < links.length; i++) {
    hrefs.push(links[i].href);
}

// Add Event Listener
musicPlayer.addEventListener("ended", playNext);
playButton.addEventListener("click", audioControl);

// State Tracker
let currentAudio = -1;
let isPlaying = false;
let hasStarted = false;

function playNext() {
    currentAudio = (currentAudio + 1);
    musicPlayer.src = hrefs[currentAudio]
    musicPlayer.load();
    musicPlayer.play();
    console.log("YES!");
    console.log(musicPlayer.src);
}

function audioControl() {
    
    if (isPlaying) {
        musicPlayer.pause();
        isPlaying = false;
    }
    else {
        if (hasStarted) {
            musicPlayer.play();
            isPlaying = true;
        }
        else {
            playNext();
            isPlaying = true;
        }
    }

    musicIcon.setAttribute("class", (isPlaying) ? "fas fa-pause" : "fas fa-play");
}
