// "A.I. na lang!" — landing page interactivity

document.addEventListener("DOMContentLoaded", () => {
  initFaq();
  initPlayModal();
  initScrollMeter();
});

/* ---------- FAQ accordion ---------- */
function initFaq() {
  document.querySelectorAll(".faq-item").forEach((item) => {
    const btn = item.querySelector(".faq-q");
    if (!btn) return;
    btn.addEventListener("click", () => {
      const wasOpen = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach((open) => {
        if (open !== item) open.classList.remove("open");
      });
      item.classList.toggle("open", !wasOpen);
    });
  });
}

/* ---------- Play-in-browser modal ---------- */
function initPlayModal() {
  const modal = document.getElementById("playModal");
  const iframe = document.getElementById("gameFrame");
  const gamePath = "./game/web-build/index.html";
  if (!modal || !iframe) return;

  const openModal = () => {
    iframe.src = gamePath;
    modal.classList.add("open");
    document.body.style.overflow = "hidden";
  };
  const closeModal = () => {
    modal.classList.remove("open");
    iframe.src = "";
    document.body.style.overflow = "";
  };

  document.querySelectorAll("[data-open-play]").forEach((el) => {
    el.addEventListener("click", (e) => {
      e.preventDefault();
      openModal();
    });
  });
  document.querySelectorAll("[data-close-play]").forEach((el) => {
    el.addEventListener("click", closeModal);
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("open")) closeModal();
  });
}

/* ---------- Scroll-linked CT meter (playful nod to the game's own mechanic) ---------- */
function initScrollMeter() {
  const segs = document.querySelectorAll("#scrollCtMeter .hud-meter-seg");
  if (!segs.length) return;

  const total = segs.length;
  const onScroll = () => {
    const scrolled = window.scrollY;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const pct = max > 0 ? Math.min(1, scrolled / max) : 0;
    const filled = Math.round(pct * total);
    segs.forEach((seg, i) => seg.classList.toggle("on", i < filled));
  };

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
}
