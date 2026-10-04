import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find exactly loadingEl.classList.add('hidden'); and setTimeout...
pattern = r"( {4}loadingEl\.classList\.add\('hidden'\);\n {4}setTimeout\(\(\) => loadingEl\.remove\(\), 500\);)"
match = re.search(pattern, text)
if match:
    inject = match.group(1) + '''

    try {
      const oldBg = scene.background;
      scene.background = new THREE.Color(0x0a0a0c);
      if (typeof grid !== 'undefined') grid.visible = false;
      
      const captureCam = new THREE.PerspectiveCamera(35, 16/9, 0.1, 100);
      
      captureCam.position.set(4.5, 1.5, 5.0);
      captureCam.lookAt(0, 0.4, 0);
      renderer.render(scene, captureCam);
      const img2 = document.getElementById('img-sec2');
      if(img2) img2.src = renderer.domElement.toDataURL('image/jpeg', 0.92);
      
      captureCam.position.set(-2.5, 0.7, 4.0);
      captureCam.lookAt(0, 0.3, 1.0);
      renderer.render(scene, captureCam);
      const img3_1 = document.getElementById('img-sec3-main');
      if(img3_1) img3_1.src = renderer.domElement.toDataURL('image/jpeg', 0.92);
      
      captureCam.position.set(0, 2.5, -2.5);
      captureCam.lookAt(0, 0.5, -1.0);
      renderer.render(scene, captureCam);
      const img3_3 = document.getElementById('img-sec3-powertrain');
      if(img3_3) img3_3.src = renderer.domElement.toDataURL('image/jpeg', 0.92);

      captureCam.position.set(2.5, 0.6, -3.5);
      captureCam.lookAt(-0.5, 0.4, -1.5);
      renderer.render(scene, captureCam);
      const img3_2 = document.getElementById('img-sec3-detail');
      if(img3_2) img3_2.src = renderer.domElement.toDataURL('image/jpeg', 0.92);

      scene.background = oldBg;
      if (typeof grid !== 'undefined') grid.visible = true;
    } catch (e) {
      console.error("Capture failed", e);
    }
'''
    text = text[:match.end()] + inject[len(match.group(1)):] + text[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("JS injected!")
else:
    print("Pattern not found!")
