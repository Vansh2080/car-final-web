import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_js_scene = '''const scene = new THREE.Scene();
scene.background = new THREE.Color(0x1a1a2e);
scene.fog = new THREE.Fog(0x1a1a2e, 8, 40);'''
new_js_scene = '''const scene = new THREE.Scene();
scene.background = null;
scene.fog = new THREE.Fog(0x0a0a0c, 15, 45);'''

if old_js_scene in text:
    text = text.replace(old_js_scene, new_js_scene)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("JS scene patched!")
else:
    print("JS scene not found!")
