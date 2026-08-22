(function () {
  var ham = document.getElementById("ham");
  var drawer = document.getElementById("drawer");
  var backdrop = document.getElementById("backdrop");
  if (!ham || !drawer) return;
  function openMenu() {
    drawer.classList.add("open");
    backdrop.classList.add("open");
    ham.setAttribute("aria-expanded", "true");
    drawer.setAttribute("aria-hidden", "false");
  }
  function closeMenu() {
    drawer.classList.remove("open");
    backdrop.classList.remove("open");
    ham.setAttribute("aria-expanded", "false");
    drawer.setAttribute("aria-hidden", "true");
  }
  ham.addEventListener("click", function () {
    drawer.classList.contains("open") ? closeMenu() : openMenu();
  });
  if (backdrop) backdrop.addEventListener("click", closeMenu);
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenu();
  });
  var form = document.getElementById("enquiryForm");
  if (form) form.addEventListener("submit", function (e) { e.preventDefault(); });
})();
