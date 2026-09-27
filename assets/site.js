(function(){
  var root=document.documentElement, header=document.querySelector('.site-header'), toTop=document.querySelector('.to-top');
  var burger=document.querySelector('.burger'), mnav=document.getElementById('mnav');

  // Header shadow + back-to-top, one rAF-batched scroll handler
  var ticking=false;
  function onScroll(){
    var y=window.scrollY;
    header.classList.toggle('scrolled', y>20);
    toTop.classList.toggle('show', y>700);
    ticking=false;
  }
  window.addEventListener('scroll',function(){ if(!ticking){ticking=true;requestAnimationFrame(onScroll);} },{passive:true});
  onScroll();

  // Mobile menu
  function setMenu(open){
    root.classList.toggle('menu-open',open);
    document.body.classList.toggle('menu-open',open);
    burger.setAttribute('aria-expanded',open);
    burger.setAttribute('aria-label',open?'Close menu':'Open menu');
  }
  burger.addEventListener('click',function(){ setMenu(!root.classList.contains('menu-open')); });
  mnav.addEventListener('click',function(e){ if(e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){ setMenu(false); closeLightbox(); } });

  // Scroll reveals: anything already on screen shows immediately; never leaves content hidden
  var els=[].slice.call(document.querySelectorAll('.rv'));
  if(!('IntersectionObserver' in window)){ els.forEach(function(el){el.classList.add('in');}); }
  else{
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target);} });
    },{rootMargin:'0px 0px -8% 0px',threshold:0.01});
    els.forEach(function(el){
      var sibs=[].slice.call(el.parentElement.children).filter(function(c){return c.classList.contains('rv');});
      el.style.transitionDelay=(Math.min(sibs.indexOf(el),4)*90)+'ms';
      io.observe(el);
    });
    setTimeout(function(){ els.forEach(function(el){ if(el.getBoundingClientRect().top<innerHeight) el.classList.add('in'); }); },1500);
  }

  // Click-to-play YouTube: loads the player only when someone presses play
  document.querySelectorAll('.video .play').forEach(function(btn){
    btn.addEventListener('click',function(){
      var frame=btn.parentElement, id=frame.getAttribute('data-yt');
      var ifr=document.createElement('iframe');
      ifr.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';
      ifr.title=btn.getAttribute('aria-label')||'Video';
      ifr.allow='accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
      ifr.allowFullscreen=true;
      frame.innerHTML=''; frame.appendChild(ifr);
    });
  });

  // Lightbox (portfolio pieces + enlargeable covers)
  var lb=document.querySelector('.lightbox'), lbImg, lbCap, group=[], idx=0;
  if(lb){ lbImg=lb.querySelector('img'); lbCap=lb.querySelector('figcaption'); }
  function show(i){
    idx=(i+group.length)%group.length;
    var it=group[idx];
    lbImg.src=it.src; lbImg.alt=it.alt||''; lbCap.textContent=it.caption||'';
  }
  function openLightbox(items,i){
    if(!lb) return;
    group=items; lb.classList.toggle('single',items.length<2);
    show(i); lb.classList.add('open'); document.body.style.overflow='hidden';
    lb.querySelector('.lb-close').focus();
  }
  function closeLightbox(){ if(lb&&lb.classList.contains('open')){ lb.classList.remove('open'); document.body.style.overflow=''; } }
  if(lb){
    lb.querySelector('.lb-close').addEventListener('click',closeLightbox);
    lb.querySelector('.lb-prev').addEventListener('click',function(){show(idx-1);});
    lb.querySelector('.lb-next').addEventListener('click',function(){show(idx+1);});
    lb.addEventListener('click',function(e){ if(e.target===lb) closeLightbox(); });
    document.addEventListener('keydown',function(e){
      if(!lb.classList.contains('open')) return;
      if(e.key==='ArrowLeft') show(idx-1);
      if(e.key==='ArrowRight') show(idx+1);
    });
  }
  document.querySelectorAll('a[data-zoom]').forEach(function(a){
    a.addEventListener('click',function(e){
      e.preventDefault();
      var img=a.querySelector('img');
      openLightbox([{src:a.getAttribute('href'),alt:img?img.alt:'',caption:''}],0);
    });
  });

  // Portfolio filters (also honours links like portfolio.html#editorial)
  var gallery=document.querySelector('.gallery');
  if(gallery){
    var pieces=[].slice.call(gallery.querySelectorAll('.piece')), buttons=[].slice.call(document.querySelectorAll('.filters button'));
    function visible(){ return pieces.filter(function(p){return !p.hidden;}); }
    function applyFilter(f){
      if(!buttons.some(function(b){return b.dataset.filter===f;})) f='all';
      buttons.forEach(function(b){ b.setAttribute('aria-pressed', b.dataset.filter===f); });
      pieces.forEach(function(p){ p.hidden = !(f==='all' || p.dataset.tags.split(' ').indexOf(f)>-1); });
    }
    buttons.forEach(function(b){ b.addEventListener('click',function(){
      applyFilter(b.dataset.filter);
      history.replaceState(null,'',b.dataset.filter==='all'?location.pathname:'#'+b.dataset.filter);
    }); });
    pieces.forEach(function(p){
      p.querySelector('button').addEventListener('click',function(){
        var vis=visible(), items=vis.map(function(v){ var im=v.querySelector('img'); return {src:im.src,alt:im.alt,caption:v.dataset.title}; });
        openLightbox(items, vis.indexOf(p));
      });
    });
    applyFilter((location.hash||'#all').slice(1));
    window.addEventListener('hashchange',function(){ applyFilter((location.hash||'#all').slice(1)); });
  }

  // Preview-only contact forms: validate, but don't send anywhere
  document.querySelectorAll('form.js-contact').forEach(function(form){
    var note=form.querySelector('.form-note');
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var bad=[].slice.call(form.querySelectorAll('[required]')).filter(function(f){return !f.value.trim()||(f.type==='email'&&!/^\S+@\S+\.\S+$/.test(f.value));});
      if(bad.length){ note.textContent='Please fill in all required fields.'; bad[0].focus(); return; }
      note.textContent='Preview only — this mockup form doesn’t send messages yet.';
    });
  });
})();
