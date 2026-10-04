import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update CSS
old_css = '''  /* Editorial Sections CSS */
  #section-02 { background: linear-gradient(to bottom, #1a1a2e 0%, #15151a 15%, #0d0d11 50%, #0a0a0c 100%); }
  #section-03 { background: #0a0a0c; }
  .editorial-section { position: relative; width: 100%; min-height: 100vh; color: #f0f0f0; display: flex; align-items: center; justify-content: center; padding: 4rem; box-sizing: border-box; z-index: 10; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }'''

new_css = '''  /* Editorial Sections CSS */
  #section-02 {
    background-color: #0a0a0c;
    background-image: 
      linear-gradient(180deg, #1a1a2e 0%, rgba(26,26,46,0) 25%),
      radial-gradient(circle at 80% 30%, rgba(40, 44, 55, 0.15) 0%, transparent 60%),
      linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 4rem 4rem, 4rem 4rem;
    position: relative;
  }
  #section-03 {
    background-color: #0a0a0c;
    background-image: 
      radial-gradient(circle at 100% 50%, rgba(40, 44, 55, 0.15) 0%, transparent 60%),
      radial-gradient(circle at 0% 100%, rgba(30, 32, 40, 0.15) 0%, transparent 60%),
      linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 4rem 4rem, 4rem 4rem;
    position: relative;
  }
  .editorial-section { position: relative; width: 100%; min-height: 100vh; color: #f0f0f0; display: flex; align-items: center; justify-content: center; padding: 4rem; box-sizing: border-box; z-index: 10; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
'''
if old_css in text:
    text = text.replace(old_css, new_css)
else:
    print("CSS part 1 not found!")

old_css2 = '''  .editorial-image-wrapper { width: 100%; height: 80vh; position: relative; overflow: hidden; background: radial-gradient(circle at 50% 50%, #202028 0%, #0a0a0c 100%); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 4px; display: flex; align-items: center; justify-content: center; }
  .placeholder-car-silhouette { position: absolute; bottom: 20%; left: 10%; right: 10%; height: 35%; background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0) 100%); border-top: 1px solid rgba(255,255,255,0.15); border-radius: 40% 60% 0 0 / 100% 100% 0 0; box-shadow: 0 -10px 40px rgba(255,255,255,0.03); opacity: 0.8; }
  .editorial-image-wrapper::after { content: 'PHANTOM X1 // VISUAL ASSET'; color: rgba(255, 255, 255, 0.04); font-size: 1.5rem; letter-spacing: 0.3em; transform: rotate(-90deg); position: absolute; white-space: nowrap; }'''

new_css2 = '''  .editorial-image-wrapper { width: 100%; height: auto; aspect-ratio: 16/10; position: relative; display: flex; align-items: center; justify-content: center; }
  .editorial-image { width: 100%; height: 100%; object-fit: cover; opacity: 0.95; mask-image: radial-gradient(circle at center, black 60%, transparent 100%); -webkit-mask-image: radial-gradient(circle at center, black 60%, transparent 100%); filter: contrast(1.1) brightness(1.1); }
'''
if old_css2 in text:
    text = text.replace(old_css2, new_css2)
else:
    print("CSS part 2 not found!")

# 2. Update HTML images
old_html1 = '''    <div class="editorial-image-wrapper">
      <div class="placeholder-car-silhouette"></div>
    </div>'''
new_html1 = '''    <div class="editorial-image-wrapper">
      <img id="img-sec2" class="editorial-image" src="" alt="PHANTOM X1 Visual">
    </div>'''
if old_html1 in text:
    text = text.replace(old_html1, new_html1)

old_html2 = '''    <div class="editorial-image-wrapper" style="order: 0;">
      <div class="placeholder-car-silhouette"></div>
    </div>'''
new_html2 = '''    <div class="editorial-image-column" style="order: 0; display: flex; flex-direction: column; gap: 3rem;">
      <div class="editorial-image-wrapper" style="aspect-ratio: 16/10;">
        <img id="img-sec3-main" class="editorial-image" src="" alt="PHANTOM X1 Main">
      </div>
      <div class="editorial-image-wrapper" style="aspect-ratio: 16/7;">
        <img id="img-sec3-powertrain" class="editorial-image" src="" alt="PHANTOM X1 Powertrain">
      </div>
      <div class="editorial-image-wrapper" style="aspect-ratio: 16/7;">
        <img id="img-sec3-detail" class="editorial-image" src="" alt="PHANTOM X1 Detail">
      </div>
    </div>'''
if old_html2 in text:
    text = text.replace(old_html2, new_html2)


# 3. Inject javascript captures
js_hook = '''      loadingEl.classList.add('hidden');
      setTimeout(() => loadingEl.remove(), 500);'''
js_inject = '''      loadingEl.classList.add('hidden');
      setTimeout(() => loadingEl.remove(), 500);

      try {
        const oldBg = scene.background;
        scene.background = new THREE.Color(0x0a0a0c);
        if (typeof grid !== 'undefined') grid.visible = false;
        
        const captureCam = new THREE.PerspectiveCamera(35, 16/9, 0.1, 100);
        
        captureCam.position.set(5.5, 1.8, 5.5);
        captureCam.lookAt(0, 0.4, 0);
        renderer.render(scene, captureCam);
        const img2 = document.getElementById('img-sec2');
        if(img2) img2.src = renderer.domElement.toDataURL('image/jpeg', 0.9);
        
        captureCam.position.set(-2, 0.6, 3.5);
        captureCam.lookAt(0, 0.3, 0);
        renderer.render(scene, captureCam);
        const img3_1 = document.getElementById('img-sec3-main');
        if(img3_1) img3_1.src = renderer.domElement.toDataURL('image/jpeg', 0.9);
        
        captureCam.position.set(0, 3.5, 1);
        captureCam.lookAt(0, 0, 0);
        renderer.render(scene, captureCam);
        const img3_3 = document.getElementById('img-sec3-powertrain');
        if(img3_3) img3_3.src = renderer.domElement.toDataURL('image/jpeg', 0.9);

        captureCam.position.set(3, 1.0, -3.5);
        captureCam.lookAt(-0.5, 0.4, -0.5);
        renderer.render(scene, captureCam);
        const img3_2 = document.getElementById('img-sec3-detail');
        if(img3_2) img3_2.src = renderer.domElement.toDataURL('image/jpeg', 0.9);

        scene.background = oldBg;
        if (typeof grid !== 'undefined') grid.visible = true;
      } catch (e) {
        console.error("Capture failed", e);
      }
'''
if js_hook in text:
    text = text.replace(js_hook, js_inject)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch applied successfully.")
