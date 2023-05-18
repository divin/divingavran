// Get some constants
const preferredTheme = localStorage.getItem("theme"); // Get preferred Theme
const prefersDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches; // Check the system settings 
const defaultTheme = prefersDarkMode ? "theme-dark" : "theme-light"; // Sets the defaultTheme

// Check if the localStorage item is set, if not set it to the default theme
if (!preferredTheme) {
    localStorage.setItem("theme", defaultTheme);
}

// Function to set a given theme
function setTheme(themeName) {
    localStorage.setItem("theme", themeName);
    document.documentElement.className = themeName;
}

// Sets the icon
function setIcon(themeName) {
    var icon = document.querySelector("#theme-icon");
    icon.setAttribute("class", (themeName === "theme-dark") ? "fas fa-moon" : "fas fa-sun");
}

// Change theme
function changeTheme() {

    var hasDarkMode = localStorage.getItem("theme") === "theme-dark"
    var themeName = hasDarkMode ? "theme-light" : "theme-dark"

    setIcon(themeName);
    setTheme(themeName);
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem("theme") === "theme-dark") {
        setIcon("theme-dark");
        setTheme("theme-dark");
    } 
    else {
        setIcon("theme-light");
        setTheme("theme-light");
    }
})();