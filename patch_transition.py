import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace #section-02 CSS
old_css = '''  #section-02 {
    background-color: #0a0a0c;
    background-image: 
      linear-gradient(180deg, #1a1a2e 0%, rgba(26,26,46,0) 25%),
      radial-gradient(circle at 80% 30%, rgba(40, 44, 55, 0.15) 0%, transparent 60%),
      linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 4rem 4rem, 4rem 4rem;
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
    bottom: 100%; /* Positioned exactly on top of section-02, extending upwards into section-01 */
    left: 0;
    right: 0;
    height: 250px;
    background: linear-gradient(to bottom, rgba(10, 10, 12, 0) 0%, #0a0a0c 100%);
    pointer-events: none;
    z-index: 20;
  }'''

if old_css in text:
    text = text.replace(old_css, new_css)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Transition patched!")
else:
    print("CSS block not found!")
