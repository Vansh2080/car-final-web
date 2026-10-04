import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_css = '''  #section-02 {
    background-color: #0a0a0c;
    background-image: 
      radial-gradient(circle at 80% 30%, rgba(40, 44, 55, 0.15) 0%, transparent 60%),
      linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 4rem 4rem, 4rem 4rem;
    position: relative;
  }'''

new_css = '''  #section-02 {
    background-color: #0a0a0c;
    background-image: 
      radial-gradient(circle at 80% 30%, rgba(40, 44, 55, 0.15) 0%, transparent 60%),
      linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 4rem 4rem, 4rem 4rem;
    position: relative;
  }
  #section-02::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 150px;
    background: linear-gradient(to bottom, #0a0a0c 0%, rgba(10, 10, 12, 0) 100%);
    pointer-events: none;
    z-index: 1; /* just above the background, behind content */
  }'''

if old_css in text:
    text = text.replace(old_css, new_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Grid fade patched!")
else:
    print("CSS block not found!")
