import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_cams = '''        captureCam.position.set(5.5, 1.8, 5.5);
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
        if(img3_2) img3_2.src = renderer.domElement.toDataURL('image/jpeg', 0.9);'''

new_cams = '''        captureCam.position.set(4.5, 1.5, 5.0);
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
        if(img3_2) img3_2.src = renderer.domElement.toDataURL('image/jpeg', 0.92);'''

if old_cams in text:
    text = text.replace(old_cams, new_cams)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Cameras adjusted!")
else:
    print("Old cams not found!")
