document.addEventListener("DOMContentLoaded", () => {
  const groups = document.querySelectorAll(".site-nav__group");

  groups.forEach((group) => {
    const button = group.querySelector(".site-nav__toggle");
    const menu = group.querySelector(".site-nav__submenu");

    if (!button || !menu) return;

    const closeMenu = () => {
      button.setAttribute("aria-expanded", "false");
      menu.hidden = true;
    };

    const openMenu = () => {
      button.setAttribute("aria-expanded", "true");
      menu.hidden = false;
    };

    const toggleMenu = () => {
      const isOpen = button.getAttribute("aria-expanded") === "true";

      groups.forEach((otherGroup) => {
        const otherButton = otherGroup.querySelector(".site-nav__toggle");
        const otherMenu = otherGroup.querySelector(".site-nav__submenu");

        if (!otherButton || !otherMenu) return;

        otherButton.setAttribute("aria-expanded", "false");
        otherMenu.hidden = true;
      });

      if (isOpen) {
        closeMenu();
      } else {
        openMenu();
      }
    };

    button.addEventListener("click", (event) => {
      event.stopPropagation();
      toggleMenu();
    });

    button.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggleMenu();
      }

      if (event.key === "Escape") {
        closeMenu();
        button.focus();
      }
    });

    menu.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        closeMenu();
        button.focus();
      }
    });
  });

  document.addEventListener("click", (event) => {
    groups.forEach((group) => {
      const button = group.querySelector(".site-nav__toggle");
      const menu = group.querySelector(".site-nav__submenu");

      if (!button || !menu) return;

      if (!group.contains(event.target)) {
        button.setAttribute("aria-expanded", "false");
        menu.hidden = true;
      }
    });
  });
});
