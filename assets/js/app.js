/* motikad — client-side utilities */

(function () {
  'use strict';

  /* ---- Persistent checklists ---- */
  document.querySelectorAll('input[type="checkbox"][data-persist]').forEach(function (cb) {
    var key = 'motikad-' + cb.dataset.persist;
    cb.checked = localStorage.getItem(key) === 'true';
    cb.disabled = false;
    cb.addEventListener('change', function () {
      localStorage.setItem(key, cb.checked);
    });
  });

  /* ---- Checklist reset buttons ---- */
  document.querySelectorAll('[data-reset]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var prefix = btn.dataset.reset;
      document.querySelectorAll('input[data-persist^="' + prefix + '"]').forEach(function (cb) {
        cb.checked = false;
        localStorage.removeItem('motikad-' + cb.dataset.persist);
      });
    });
  });

  /* ---- Relative dates ---- */
  document.querySelectorAll('[data-date]').forEach(function (el) {
    var d = new Date(el.dataset.date);
    var days = Math.floor((Date.now() - d) / 86400000);
    var text;
    if (days < 0) text = 'in ' + Math.abs(days) + ' days';
    else if (days === 0) text = 'today';
    else if (days === 1) text = 'yesterday';
    else if (days < 7) text = days + ' days ago';
    else if (days < 30) text = Math.floor(days / 7) + (days < 14 ? ' week ago' : ' weeks ago');
    else if (days < 365) text = Math.floor(days / 30) + (days < 60 ? ' month ago' : ' months ago');
    else text = el.dataset.date;
    el.textContent = text;
    el.title = el.dataset.date;
  });

  /* ---- Deadline countdowns ---- */
  document.querySelectorAll('[data-deadline]').forEach(function (el) {
    var d = new Date(el.dataset.deadline);
    var days = Math.ceil((d - Date.now()) / 86400000);
    var text;
    if (days < 0) text = Math.abs(days) + ' days overdue';
    else if (days === 0) text = 'today';
    else if (days <= 7) text = days + (days === 1 ? ' day left' : ' days left');
    else if (days <= 60) text = Math.ceil(days / 7) + ' weeks left';
    else text = Math.floor(days / 30) + ' months left';
    el.textContent = text;
    el.title = el.dataset.deadline;
    if (days <= 30 && days >= 0) el.classList.add('deadline-urgent');
    if (days < 0) el.classList.add('deadline-overdue');
  });

  /* ---- Table wrapping ---- */
  document.querySelectorAll('table').forEach(function (t) {
    if (t.parentElement.classList.contains('table-wrap')) return;
    var w = document.createElement('div');
    w.className = 'table-wrap';
    t.parentNode.insertBefore(w, t);
    w.appendChild(t);
  });

  /* ---- Lightbox ---- */
  var images = document.querySelectorAll('.gallery img[loading]');
  if (images.length) {
    var lb = document.createElement('div');
    lb.id = 'lightbox';
    lb.innerHTML = '<button class="lb-close">&times;</button><button class="lb-prev">&#10094;</button><img><button class="lb-next">&#10095;</button><p class="lb-cap"></p>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lb-cap');
    var idx = 0;

    function show(i) {
      idx = (i + images.length) % images.length;
      lbImg.src = images[idx].src;
      var fig = images[idx].closest('figure');
      lbCap.textContent = fig ? fig.querySelector('figcaption strong').textContent : '';
      lb.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function hide() {
      lb.classList.remove('active');
      document.body.style.overflow = '';
    }

    images.forEach(function (img, i) {
      img.style.cursor = 'pointer';
      img.addEventListener('click', function () { show(i); });
    });

    lb.querySelector('.lb-close').addEventListener('click', hide);
    lb.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(idx - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(idx + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) hide(); });

    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('active')) return;
      if (e.key === 'Escape') hide();
      if (e.key === 'ArrowRight') show(idx + 1);
      if (e.key === 'ArrowLeft') show(idx - 1);
    });
  }
})();
