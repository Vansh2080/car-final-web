import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('scene.background = new THREE.Color(0x000000);', '// scene.background = new THREE.Color(0x000000);')
text = text.replace('scene.background = new THREE.Color().lerpColors(new THREE.Color(0x000000), new THREE.Color(0x1a1a2e), lightFactor);', '// lerp bg removed')
text = text.replace('scene.background = new THREE.Color(0x1a1a2e);', '// scene.background = new THREE.Color(0x1a1a2e);')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Intro background patched!")
