import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Modify CSS to make #section-01 background match #section-02
old_css_sec1 = '''  #section-01 {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    user-select: none;
    -webkit-user-select: none;
    background: var(--bg);
  }'''
new_css_sec1 = '''  #section-01 {
    position: relative;
    width: 100%;
    height: 100vh;
    overflow: hidden;
    user-select: none;
    -webkit-user-select: none;
    background: #0a0a0c;
  }'''
if old_css_sec1 in text:
    text = text.replace(old_css_sec1, new_css_sec1)
else:
    print("CSS sec1 not found!")

# 2. Modify JS to make scene background null and update fog
old_js_scene = '''const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x1a1a2e);
  scene.fog = new THREE.Fog(0x1a1a2e, 8, 40);'''
new_js_scene = '''const scene = new THREE.Scene();
  scene.background = null;
  scene.fog = new THREE.Fog(0x0a0a0c, 15, 45);'''
if old_js_scene in text:
    text = text.replace(old_js_scene, new_js_scene)
else:
    print("JS scene not found!")

# 3. Remove the overlapping gradient from section-02 we just added
old_gradient = '''  #section-02::before {
    content: '';
    position: absolute;
    bottom: 100%; /* Positioned exactly on top of section-02, extending upwards into section-01 */
    left: 0;
    right: 0;
    height: 250px;
    background: linear-gradient(to bottom, rgba(10, 10, 12, 0) 0%, #0a0a0c 100%);
    pointer-events: none;
    z-index: 20;
  }'''
if old_gradient in text:
    text = text.replace(old_gradient, "")
else:
    print("Gradient not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Transparency patched!")
