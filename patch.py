import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_css = """  /* Editorial Sections CSS */
  #section-02 { background: linear-gradient(to bottom, #1a1a2e 0%, #15151a 15%, #0d0d11 50%, #0a0a0c 100%); }
  #section-03 { background: #0a0a0c; }
  .editorial-section { position: relative; width: 100%; min-height: 100vh; color: #f0f0f0; display: flex; align-items: center; justify-content: center; padding: 4rem; box-sizing: border-box; z-index: 10; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
  .editorial-container { max-width: 1400px; width: 100%; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; opacity: 0; transform: translateY(40px); transition: opacity 1.2s cubic-bezier(0.2, 0.8, 0.2, 1), transform 1.2s cubic-bezier(0.2, 0.8, 0.2, 1); }
  .editorial-section.is-visible .editorial-container { opacity: 1; transform: translateY(0); }
  .editorial-label { font-size: 0.85rem; letter-spacing: 0.2em; color: #888; margin-bottom: 2rem; text-transform: uppercase; }
  .editorial-title { font-size: 4rem; font-weight: 300; margin: 0 0 1rem 0; letter-spacing: -0.02em; color: #fff; line-height: 1.1; }
  .editorial-subtitle { font-size: 1.5rem; color: #aaa; margin: 0 0 2rem 0; font-weight: 400; }
  .editorial-paragraph { font-size: 1.1rem; line-height: 1.7; color: #ccc; margin-bottom: 3rem; max-width: 90%; }
  .editorial-principles { display: flex; flex-direction: column; gap: 2rem; }
  .editorial-principles h4 { font-size: 0.9rem; letter-spacing: 0.1em; margin: 0 0 0.5rem 0; color: #fff; text-transform: uppercase; }
  .editorial-principles p { margin: 0; font-size: 0.95rem; color: #888; line-height: 1.5; }
  .editorial-divider { height: 1px; background: rgba(255, 255, 255, 0.15); margin: 3rem 0; width: 100%; }
  .editorial-meta { font-size: 0.75rem; color: #666; letter-spacing: 0.15em; display: flex; justify-content: space-between; text-transform: uppercase; }
  .editorial-image-wrapper { width: 100%; height: 80vh; position: relative; overflow: hidden; background: radial-gradient(circle at 50% 50%, #202028 0%, #0a0a0c 100%); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 4px; display: flex; align-items: center; justify-content: center; }
  .placeholder-car-silhouette { position: absolute; bottom: 20%; left: 10%; right: 10%; height: 35%; background: linear-gradient(180deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0) 100%); border-top: 1px solid rgba(255,255,255,0.15); border-radius: 40% 60% 0 0 / 100% 100% 0 0; box-shadow: 0 -10px 40px rgba(255,255,255,0.03); opacity: 0.8; }
  .editorial-image-wrapper::after { content: 'PHANTOM X1 // VISUAL ASSET'; color: rgba(255, 255, 255, 0.04); font-size: 1.5rem; letter-spacing: 0.3em; transform: rotate(-90deg); position: absolute; white-space: nowrap; }
  .editorial-specs-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 3rem; }
  .editorial-spec-item { border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 1rem; }
  .editorial-spec-value { font-size: 2.5rem; font-weight: 300; color: #fff; margin: 0; display: flex; align-items: baseline; gap: 0.5rem; }
  .editorial-spec-unit { font-size: 1rem; color: #888; font-weight: 400; letter-spacing: 0.05em; }
  .editorial-spec-label { font-size: 0.75rem; color: #888; letter-spacing: 0.1em; margin-top: 0.5rem; text-transform: uppercase; }
  .editorial-spec-list { margin-top: 3rem; border-top: 1px solid rgba(255, 255, 255, 0.15); padding-top: 1.5rem; }
  .editorial-spec-list-item { display: flex; justify-content: space-between; padding: 0.75rem 0; border-bottom: 1px solid rgba(255, 255, 255, 0.05); font-size: 0.85rem; letter-spacing: 0.05em; }
  .editorial-spec-list-item span:first-child { color: #888; }
  .editorial-spec-list-item span:last-child { color: #ddd; text-align: right; }
  @media (max-width: 1024px) {
    .editorial-container { grid-template-columns: 1fr; gap: 3rem; }
    .editorial-section { padding: 3rem 2rem; }
    .editorial-image-wrapper { height: 50vh; order: 2; }
    .editorial-content { order: 1; }
  }
""" + '\n'

new_html = """<!-- SECTION 02 -->
<div id="section-02" class="editorial-section">
  <div class="editorial-container">
    <div class="editorial-content">
      <div class="editorial-label">02 / 03 &nbsp;&nbsp;&nbsp; PHANTOM AUTOMOTIVE</div>
      <h2 class="editorial-title">PHANTOM</h2>
      <h3 class="editorial-subtitle">THE MARQUE BEHIND THE MACHINE</h3>
      <p class="editorial-paragraph">PHANTOM Automotive was founded around a simple idea: extreme performance should be engineered with the same discipline as fine machinery. The result is a marque where mechanical capability, sculpted design and uncompromising craftsmanship exist as one.</p>
      
      <div class="editorial-principles">
        <div class="principle">
          <h4>01 &mdash; ORIGIN</h4>
          <p>PHANTOM was conceived as a limited-production performance marque focused on creating machines that feel mechanical, purposeful and unmistakable.</p>
        </div>
        <div class="principle">
          <h4>02 &mdash; DESIGN LANGUAGE</h4>
          <p>Every PHANTOM is shaped around tension &mdash; low proportions, dramatic surfaces and functional aerodynamic forms rather than decoration for its own sake.</p>
        </div>
        <div class="principle">
          <h4>03 &mdash; ENGINEERING PHILOSOPHY</h4>
          <p>The marque prioritizes mechanical systems that communicate directly with the driver, combining advanced engineering with the character and response of a high-performance combustion powertrain.</p>
        </div>
        <div class="principle">
          <h4>04 &mdash; EXCLUSIVITY</h4>
          <p>PHANTOM vehicles are produced in deliberately limited numbers. The X1 is planned as a 99-unit flagship, allowing engineering and craftsmanship to remain central to the ownership experience.</p>
        </div>
      </div>
      
      <div class="editorial-divider"></div>
      
      <div class="editorial-meta">
        <span>PHANTOM AUTOMOTIVE<br>EST. 2026</span>
        <span style="text-align: right;">LIMITED PRODUCTION<br>PERFORMANCE MARQUE</span>
      </div>
    </div>
    
    <div class="editorial-image-wrapper">
      <div class="placeholder-car-silhouette"></div>
    </div>
  </div>
</div>

<!-- SECTION 03 -->
<div id="section-03" class="editorial-section">
  <div class="editorial-container">
    <div class="editorial-image-wrapper" style="order: 0;">
      <div class="placeholder-car-silhouette"></div>
    </div>
    
    <div class="editorial-content" style="order: 1;">
      <div class="editorial-label">03 / 03 &nbsp;&nbsp;&nbsp; PHANTOM AUTOMOTIVE</div>
      <h2 class="editorial-title">PHANTOM X1</h2>
      <h3 class="editorial-subtitle">THE MACHINE</h3>
      <p class="editorial-paragraph">The X1 is the first production expression of the PHANTOM philosophy &mdash; a limited-production V12 machine developed around power, stability, response and driver control.</p>
      
      <div class="editorial-principles">
        <div class="principle">
          <h4>01 &mdash; POWERTRAIN</h4>
          <p>At its core is a 6.5L twin-turbocharged V12 producing a projected 1,050 HP and 1,150 Nm of torque. Power is delivered through an 8-speed dual-clutch transmission and all-wheel-drive system.</p>
        </div>
        <div class="principle">
          <h4>02 &mdash; AERODYNAMICS</h4>
          <p>The X1's low body and aggressive surface geometry are designed around high-speed stability, controlled airflow and a planted stance.</p>
        </div>
        <div class="principle">
          <h4>03 &mdash; CHASSIS</h4>
          <p>A carbon-fibre monocoque forms the structural foundation of the vehicle, combining high rigidity with a targeted 1,580 kg vehicle mass.</p>
        </div>
        <div class="principle">
          <h4>04 &mdash; BRAKING</h4>
          <p>Carbon-ceramic performance brakes provide the thermal capacity required for repeated high-speed deceleration.</p>
        </div>
        <div class="principle">
          <h4>05 &mdash; DRIVER CONTROL</h4>
          <p>All-wheel drive, rapid dual-clutch shifting and carefully calibrated chassis systems are designed to keep the X1 composed as performance builds.</p>
        </div>
        <div class="principle">
          <h4>06 &mdash; EXCLUSIVITY</h4>
          <p>Production is limited to 99 units worldwide, positioning the X1 as a deliberately rare flagship rather than a mass-produced performance vehicle.</p>
        </div>
      </div>
      
      <div class="editorial-divider"></div>
      
      <div class="editorial-label" style="margin-bottom: 1rem;">PHANTOM X1 // CONCEPT SPECIFICATIONS</div>
      
      <div class="editorial-specs-grid">
        <div class="editorial-spec-item">
          <p class="editorial-spec-value">1,050 <span class="editorial-spec-unit">HP</span></p>
          <p class="editorial-spec-label">Power</p>
        </div>
        <div class="editorial-spec-item">
          <p class="editorial-spec-value">1,150 <span class="editorial-spec-unit">NM</span></p>
          <p class="editorial-spec-label">Torque</p>
        </div>
        <div class="editorial-spec-item">
          <p class="editorial-spec-value">2.4 <span class="editorial-spec-unit">SEC</span></p>
          <p class="editorial-spec-label">0&ndash;100 KM/H</p>
        </div>
        <div class="editorial-spec-item">
          <p class="editorial-spec-value">365 <span class="editorial-spec-unit">KM/H</span></p>
          <p class="editorial-spec-label">Top Speed</p>
        </div>
      </div>
      
      <div class="editorial-spec-list">
        <div class="editorial-spec-list-item">
          <span>ENGINE</span>
          <span>6.5L TWIN-TURBO V12</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>TRANSMISSION</span>
          <span>8-SPEED DUAL-CLUTCH</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>DRIVETRAIN</span>
          <span>ALL-WHEEL DRIVE</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>CHASSIS</span>
          <span>CARBON-FIBRE MONOCOQUE</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>BRAKES</span>
          <span>CARBON-CERAMIC PERFORMANCE SYSTEM</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>WEIGHT</span>
          <span>1,580 KG</span>
        </div>
        <div class="editorial-spec-list-item">
          <span>PRODUCTION</span>
          <span>99 UNITS</span>
        </div>
      </div>
      
      <div class="editorial-divider"></div>
      
      <p style="font-size: 1.2rem; color: #fff; letter-spacing: 0.05em; margin-bottom: 0.5rem; text-transform: uppercase;">BUILT WITH INTENT.</p>
      <p style="font-size: 0.9rem; color: #888; margin-bottom: 2rem;">Performance is not a number. It is the result of every decision made before the road begins.</p>
      
      <div class="editorial-meta">
        <span>PHANTOM X1 // V12 // AWD // 1050 HP</span>
      </div>
    </div>
  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    }, { threshold: 0.15 });
    
    document.querySelectorAll('.editorial-section').forEach(section => {
      observer.observe(section);
    });
  });
</script>
""" + '\n'

final_lines = lines[:56] + [new_css] + lines[255:898] + [new_html] + lines[1026:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Patch successful!")
