# -*- coding: utf-8 -*-
"""
Script to generate invitacion.html
"""
import base64
import os

with open('scratch/audio_b64.txt', 'r', encoding='utf-8') as f:
    audio_b64 = f.read().strip()

html_template = f'''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  
  <!-- SEO & WhatsApp Link Preview Meta Tags -->
  <title>Cumpleaños de Rubén | Invitación VIP</title>
  <meta name="description" content="¡Estás invitado al cumpleaños de Rubén! Sábado 19/09 - 20 hs en Alambique Bar (Honduras 4413, Palermo). Toca para ver la invitación interactiva." />
  <meta property="og:title" content="🎉 Cumpleaños de Rubén | Invitación VIP 🍸" />
  <meta property="og:description" content="Sábado 19/09 · 20 hs · Alambique Bar (Palermo). ¡Toca para abrir la tarjeta interactiva con música y aviso luminoso!" />
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="es_LA" />
  <meta name="theme-color" content="#0d0d11" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700;900&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400;1,600&family=Alex+Brush&display=swap" rel="stylesheet" />

  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <style>
    /* ============================================================
       RESET & BASE DESIGN SYSTEM
       ============================================================ */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    :root {{
      --bg-deep: #08070a;
      --bg-card: rgba(14, 12, 17, 0.88);
      --gold-light: #fff0d4;
      --gold-primary: #f5ba68;
      --gold-amber: #e68d2e;
      --gold-neon: #ff9922;
      --neon-glow-core: #ffffff;
      --neon-glow-primary: #ffaa33;
      --neon-glow-secondary: #e65c00;
      --neon-glow-dark: rgba(255, 90, 0, 0.4);
      --copper-subtle: #d69864;
      --text-muted: #d0c5bc;
      --border-outer: rgba(230, 141, 46, 0.7);
      --border-inner: rgba(245, 186, 104, 0.35);
      --glass-blur: blur(12px);
      --transition-smooth: all 0.35s cubic-bezier(0.25, 1, 0.5, 1);
    }}

    body {{
      background-color: var(--bg-deep);
      color: #fff;
      font-family: 'Montserrat', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      overflow-x: hidden;
      position: relative;
      padding: 20px 14px 60px 14px;
      background: radial-gradient(circle at 50% 25%, #1c1514 0%, #0c0a0f 65%, #050406 100%);
    }}

    /* Background Particle Canvas */
    #particle-canvas {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 0;
    }}

    /* Ambient Warm Spotlights */
    .ambient-glow {{
      position: fixed;
      border-radius: 50%;
      filter: blur(80px);
      pointer-events: none;
      z-index: 0;
      opacity: 0.35;
      transition: opacity 0.8s ease;
    }}
    .ambient-glow-top {{
      top: -100px;
      left: 50%;
      transform: translateX(-50%);
      width: 420px;
      height: 350px;
      background: radial-gradient(circle, rgba(255, 153, 34, 0.45) 0%, rgba(230, 92, 0, 0) 70%);
    }}
    .ambient-glow-bottom {{
      bottom: -150px;
      left: 50%;
      transform: translateX(-50%);
      width: 500px;
      height: 400px;
      background: radial-gradient(circle, rgba(214, 152, 100, 0.25) 0%, transparent 70%);
    }}

    /* ============================================================
       INTRO OVERLAY (ENVELOPE / VIP PASS)
       Solves mobile browser audio autoplay restriction smoothly!
       ============================================================ */
    #intro-overlay {{
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at 50% 40%, #1a141b 0%, #08060a 80%);
      z-index: 9999;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 24px;
      text-align: center;
      transition: opacity 0.8s ease, visibility 0.8s ease;
    }}

    #intro-overlay.hidden {{
      opacity: 0;
      visibility: hidden;
      pointer-events: none;
    }}

    .intro-box {{
      max-width: 380px;
      width: 100%;
      padding: 38px 24px;
      background: rgba(20, 16, 24, 0.7);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-radius: 20px;
      border: 1px solid rgba(245, 186, 104, 0.3);
      box-shadow: 0 0 35px rgba(255, 153, 34, 0.25), inset 0 0 20px rgba(255, 153, 34, 0.1);
      position: relative;
      animation: floatGentle 4s ease-in-out infinite;
    }}

    .intro-seal {{
      width: 80px;
      height: 80px;
      margin: 0 auto 20px auto;
      border-radius: 50%;
      background: linear-gradient(135deg, #ffd89b 0%, #e68d2e 50%, #b86210 100%);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.2rem;
      box-shadow: 0 0 25px rgba(255, 153, 34, 0.6), inset 0 0 8px rgba(255, 255, 255, 0.8);
      cursor: pointer;
      animation: pulseNeon 2.5s infinite;
    }}

    .intro-tag {{
      font-family: 'Cinzel', serif;
      font-size: 0.85rem;
      letter-spacing: 4px;
      color: var(--copper-subtle);
      margin-bottom: 8px;
      text-transform: uppercase;
    }}

    .intro-title {{
      font-family: 'Cinzel', serif;
      font-size: 2rem;
      font-weight: 900;
      color: #fff;
      margin-bottom: 12px;
      text-shadow: 0 0 12px rgba(255, 170, 51, 0.6);
    }}

    .intro-desc {{
      font-size: 0.92rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 28px;
    }}

    .btn-open-card {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      padding: 16px 24px;
      border-radius: 50px;
      border: 1px solid rgba(255, 230, 180, 0.8);
      background: linear-gradient(135deg, #ffaa33 0%, #e65c00 100%);
      color: #fff;
      font-family: 'Montserrat', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      letter-spacing: 1px;
      cursor: pointer;
      box-shadow: 0 0 25px rgba(255, 153, 34, 0.6), 0 4px 15px rgba(0,0,0,0.5);
      transition: var(--transition-smooth);
    }}

    .btn-open-card:hover, .btn-open-card:active {{
      transform: scale(1.03);
      box-shadow: 0 0 35px rgba(255, 153, 34, 0.9), 0 6px 20px rgba(0,0,0,0.6);
    }}

    /* ============================================================
       TOP FLOATING TOOLBAR (LIGHT SWITCH & MUSIC)
       ============================================================ */
    .top-toolbar {{
      position: sticky;
      top: 10px;
      z-index: 100;
      width: 100%;
      max-width: 440px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 15px;
      padding: 8px 14px;
      background: rgba(14, 12, 17, 0.75);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-radius: 30px;
      border: 1px solid rgba(245, 186, 104, 0.25);
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }}

    .toolbar-chip {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 180, 80, 0.2);
      border-radius: 20px;
      padding: 6px 12px;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--gold-light);
      cursor: pointer;
      transition: var(--transition-smooth);
    }}

    .toolbar-chip:hover {{
      background: rgba(255, 170, 50, 0.15);
      border-color: rgba(255, 180, 80, 0.5);
    }}

    .neon-indicator-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00ff88;
      box-shadow: 0 0 8px #00ff88;
      transition: var(--transition-smooth);
    }}

    .neon-indicator-dot.off {{
      background: #555;
      box-shadow: none;
    }}

    /* Sound Visualizer Equalizer Bars */
    .sound-equalizer {{
      display: flex;
      align-items: flex-end;
      gap: 2.5px;
      height: 14px;
      width: 16px;
    }}
    .eq-bar {{
      flex: 1;
      background: var(--gold-primary);
      border-radius: 2px;
      height: 4px;
      transition: height 0.15s ease;
    }}
    .playing .eq-bar:nth-child(1) {{ animation: eqJump 0.6s infinite alternate ease-in-out; }}
    .playing .eq-bar:nth-child(2) {{ animation: eqJump 0.8s infinite 0.2s alternate ease-in-out; }}
    .playing .eq-bar:nth-child(3) {{ animation: eqJump 0.5s infinite 0.1s alternate ease-in-out; }}

    @keyframes eqJump {{
      0% {{ height: 3px; }}
      100% {{ height: 14px; }}
    }}

    /* ============================================================
       MAIN INVITATION CARD (EXACT REPLICA + NEON ILLUMINATION)
       ============================================================ */
    .card-wrapper {{
      position: relative;
      width: 100%;
      max-width: 440px;
      z-index: 10;
      perspective: 1000px;
    }}

    /* Outer Neon Tube Frame */
    .invitation-card {{
      position: relative;
      width: 100%;
      background-color: var(--bg-card);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border-radius: 12px;
      padding: 36px 22px 32px 22px;
      text-align: center;
      transition: var(--transition-smooth);
      /* Default Neon Glow */
      border: 1.5px solid var(--border-outer);
      box-shadow: 
        0 0 10px var(--neon-glow-primary),
        0 0 25px var(--neon-glow-dark),
        inset 0 0 15px rgba(255, 150, 30, 0.15),
        0 15px 35px rgba(0,0,0,0.7);
    }}

    /* Internal Frame Line (Fiel a la foto) */
    .inner-border {{
      position: absolute;
      inset: 8px;
      border: 1px solid var(--border-inner);
      border-radius: 8px;
      pointer-events: none;
      transition: var(--transition-smooth);
    }}

    /* Neon OFF State */
    body.neon-off .invitation-card {{
      box-shadow: 0 10px 30px rgba(0,0,0,0.8);
      border-color: rgba(255, 255, 255, 0.12);
    }}
    body.neon-off .inner-border {{
      border-color: rgba(255, 255, 255, 0.06);
    }}
    body.neon-off .neon-text {{
      text-shadow: none !important;
      color: #dfd8cf !important;
    }}
    body.neon-off .ambient-glow {{
      opacity: 0.05 !important;
    }}
    body.neon-off .neon-icon svg {{
      filter: none !important;
      stroke: #a89f91 !important;
    }}

    /* ============================================================
       CARD CONTENT & TYPOGRAPHY
       ============================================================ */
    
    /* Neon Cocktail Icon */
    .neon-icon {{
      width: 60px;
      height: 60px;
      margin: 0 auto 14px auto;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      position: relative;
    }}

    .neon-icon svg {{
      width: 44px;
      height: 44px;
      stroke: #ffbd6a;
      fill: none;
      stroke-width: 1.8;
      stroke-linecap: round;
      stroke-linejoin: round;
      filter: drop-shadow(0 0 6px #ff9922) drop-shadow(0 0 14px #ff6600);
      transition: var(--transition-smooth);
      animation: pulseGlow 3s infinite ease-in-out;
    }}

    .neon-icon:hover svg {{
      transform: scale(1.1) rotate(5deg);
      filter: drop-shadow(0 0 10px #ffbb44) drop-shadow(0 0 25px #ff6600);
    }}

    /* Title Section */
    .card-subtitle-top {{
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 1.35rem;
      color: #ede2d8;
      letter-spacing: 0.5px;
      margin-bottom: 4px;
      opacity: 0.95;
    }}

    .card-main-name {{
      font-family: 'Cinzel', serif;
      font-size: 3.5rem;
      font-weight: 900;
      letter-spacing: 1px;
      color: #fff9f0;
      line-height: 1.1;
      margin-bottom: 22px;
      position: relative;
      /* Glowing Neon Sign Effect */
      text-shadow: 
        0 0 4px #ffffff,
        0 0 10px #ffc06a,
        0 0 22px #ff941a,
        0 0 40px #ff6a00,
        0 0 65px rgba(230, 80, 0, 0.85);
      animation: neonFlicker 6s infinite ease-in-out;
    }}

    /* Subtle Neon Flicker Animation */
    @keyframes neonFlicker {{
      0%, 19.999%, 22%, 62.999%, 64%, 64.999%, 70%, 100% {{
        opacity: 1;
        text-shadow: 
          0 0 4px #ffffff,
          0 0 10px #ffc06a,
          0 0 22px #ff941a,
          0 0 40px #ff6a00,
          0 0 65px rgba(230, 80, 0, 0.85);
      }}
      20%, 21.999%, 63%, 63.999%, 65%, 69.999% {{
        opacity: 0.85;
        text-shadow: 
          0 0 2px #ffffff,
          0 0 6px #ffaa33,
          0 0 12px #cc5500;
      }}
    }}

    /* Elegant Glowing Divider Line */
    .card-divider {{
      width: 100%;
      height: 1px;
      background: linear-gradient(90deg, 
        transparent 0%, 
        rgba(230, 141, 46, 0.25) 20%, 
        rgba(255, 180, 80, 0.8) 50%, 
        rgba(230, 141, 46, 0.25) 80%, 
        transparent 100%
      );
      margin: 18px 0;
      position: relative;
      box-shadow: 0 0 8px rgba(255, 150, 30, 0.4);
    }}

    /* Content Sections (DÓNDE / CUÁNDO / VESTIMENTA) */
    .info-section {{
      padding: 6px 0;
    }}

    .section-label {{
      font-family: 'Montserrat', sans-serif;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 4px;
      color: var(--copper-subtle);
      text-transform: uppercase;
      margin-bottom: 6px;
      opacity: 0.95;
    }}

    .section-value-primary {{
      font-family: 'Montserrat', sans-serif;
      font-size: 1.32rem;
      font-weight: 700;
      color: #ffffff;
      margin-bottom: 3px;
      letter-spacing: 0.2px;
    }}

    .section-value-secondary {{
      font-family: 'Montserrat', sans-serif;
      font-size: 1.05rem;
      font-weight: 400;
      color: #e5ded7;
      letter-spacing: 0.3px;
    }}

    /* Dress code tag */
    .dresscode-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      margin-top: 6px;
      padding: 4px 14px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 180, 80, 0.2);
      font-size: 0.82rem;
      color: var(--gold-light);
    }}

    /* Card Footer Message */
    .card-footer-quote {{
      font-family: 'Playfair Display', serif;
      font-style: italic;
      font-size: 1.35rem;
      font-weight: 600;
      color: #ffaa55;
      margin-top: 24px;
      margin-bottom: 8px;
      text-shadow: 0 0 10px rgba(255, 150, 30, 0.5);
    }}

    /* ============================================================
       INTERACTIVE LIVE COUNTDOWN TIMER
       ============================================================ */
    .countdown-container {{
      margin: 14px 0 6px 0;
      padding: 12px 8px;
      background: rgba(0, 0, 0, 0.35);
      border-radius: 12px;
      border: 1px solid rgba(245, 186, 104, 0.15);
    }}

    .countdown-title {{
      font-size: 0.72rem;
      letter-spacing: 2px;
      color: var(--copper-subtle);
      text-transform: uppercase;
      margin-bottom: 8px;
    }}

    .countdown-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
    }}

    .countdown-box {{
      background: rgba(20, 16, 24, 0.8);
      border: 1px solid rgba(255, 170, 50, 0.3);
      border-radius: 8px;
      padding: 6px 2px;
      box-shadow: 0 0 10px rgba(255, 140, 0, 0.15);
    }}

    .countdown-num {{
      font-family: 'Cinzel', serif;
      font-size: 1.3rem;
      font-weight: 700;
      color: #fff;
      text-shadow: 0 0 8px rgba(255, 170, 50, 0.7);
      line-height: 1.1;
    }}

    .countdown-unit {{
      font-size: 0.65rem;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }}

    /* ============================================================
       ACTION BUTTONS (MAPS, CALENDAR, RSVP, SHARE)
       ============================================================ */
    .button-stack {{
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 22px;
    }}

    .btn-action {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      width: 100%;
      padding: 14px 18px;
      border-radius: 10px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.95rem;
      font-weight: 600;
      letter-spacing: 0.5px;
      text-decoration: none;
      cursor: pointer;
      transition: var(--transition-smooth);
      border: none;
    }}

    /* Primary WhatsApp RSVP Button */
    .btn-whatsapp-rsvp {{
      background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
      color: #fff;
      box-shadow: 0 0 18px rgba(37, 211, 102, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}
    .btn-whatsapp-rsvp:hover, .btn-whatsapp-rsvp:active {{
      transform: translateY(-2px);
      box-shadow: 0 0 25px rgba(37, 211, 102, 0.75);
    }}

    /* Location / Maps Button */
    .btn-maps {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(245, 186, 104, 0.4);
      color: var(--gold-light);
      box-shadow: 0 0 12px rgba(255, 150, 30, 0.15);
    }}
    .btn-maps:hover, .btn-maps:active {{
      background: rgba(245, 186, 104, 0.15);
      border-color: var(--gold-primary);
      transform: translateY(-2px);
    }}

    /* Secondary Action Row (Calendar + Share) */
    .btn-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
    }}

    .btn-secondary {{
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ede2d8;
      font-size: 0.85rem;
      padding: 12px 10px;
    }}
    .btn-secondary:hover, .btn-secondary:active {{
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(245, 186, 104, 0.4);
      transform: translateY(-2px);
    }}

    /* ============================================================
       MUSIC PLAYER & GRATITUDE LYRICS CARD
       ============================================================ */
    .music-widget-card {{
      margin-top: 24px;
      background: rgba(10, 8, 14, 0.75);
      border: 1px solid rgba(245, 186, 104, 0.2);
      border-radius: 12px;
      padding: 14px 16px;
      text-align: left;
    }}

    .music-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .music-meta {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .vinyl-disc {{
      width: 42px;
      height: 42px;
      border-radius: 50%;
      background: radial-gradient(circle, #ffaa33 15%, #151218 16%, #25202a 35%, #151218 55%, #352b3c 75%, #0e0c12 100%);
      border: 2px solid rgba(245, 186, 104, 0.4);
      box-shadow: 0 0 10px rgba(255, 150, 30, 0.3);
      position: relative;
    }}
    .playing .vinyl-disc {{
      animation: spinVinyl 3.5s linear infinite;
    }}

    @keyframes spinVinyl {{
      100% {{ transform: rotate(360deg); }}
    }}

    .song-title {{
      font-size: 0.88rem;
      font-weight: 700;
      color: #fff;
    }}
    .song-artist {{
      font-size: 0.76rem;
      color: var(--copper-subtle);
    }}

    .music-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-play-pause {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--gold-amber);
      border: none;
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1rem;
      cursor: pointer;
      box-shadow: 0 0 12px rgba(230, 141, 46, 0.6);
      transition: var(--transition-smooth);
    }}
    .btn-play-pause:hover {{
      transform: scale(1.08);
      background: var(--gold-primary);
    }}

    /* Lyrics Accordion */
    .lyrics-toggle-btn {{
      background: none;
      border: none;
      color: var(--gold-primary);
      font-size: 0.76rem;
      font-weight: 600;
      margin-top: 10px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 5px;
      padding: 2px 0;
    }}

    .lyrics-box {{
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.45s ease-out;
      background: rgba(0, 0, 0, 0.4);
      border-radius: 8px;
      margin-top: 8px;
    }}

    .lyrics-box.open {{
      max-height: 280px;
      border: 1px solid rgba(245, 186, 104, 0.25);
    }}

    .lyrics-content {{
      padding: 14px;
      font-size: 0.84rem;
      line-height: 1.6;
      color: #f7ede2;
      font-style: italic;
      text-align: center;
      position: relative;
    }}

    .lyrics-highlight {{
      color: #ffd285;
      font-weight: 600;
      text-shadow: 0 0 6px rgba(255, 170, 50, 0.4);
    }}

    /* Toast Notification */
    #toast {{
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: rgba(18, 15, 23, 0.95);
      border: 1px solid var(--gold-primary);
      color: #fff;
      padding: 12px 22px;
      border-radius: 30px;
      font-size: 0.88rem;
      box-shadow: 0 4px 20px rgba(0,0,0,0.6), 0 0 15px rgba(255, 150, 30, 0.4);
      z-index: 10000;
      opacity: 0;
      transition: transform 0.4s ease, opacity 0.4s ease;
      pointer-events: none;
      white-space: nowrap;
    }}
    #toast.show {{
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }}

    /* ============================================================
       ANIMATIONS
       ============================================================ */
    @keyframes floatGentle {{
      0%, 100% {{ transform: translateY(0); }}
      50% {{ transform: translateY(-8px); }}
    }}

    @keyframes pulseNeon {{
      0%, 100% {{ transform: scale(1); box-shadow: 0 0 20px rgba(255, 153, 34, 0.5); }}
      50% {{ transform: scale(1.06); box-shadow: 0 0 35px rgba(255, 153, 34, 0.85); }}
    }}

    @keyframes pulseGlow {{
      0%, 100% {{ filter: drop-shadow(0 0 6px #ff9922) drop-shadow(0 0 14px #ff6600); }}
      50% {{ filter: drop-shadow(0 0 10px #ffbb44) drop-shadow(0 0 22px #ff6600); }}
    }}

    /* Media query for tiny screens */
    @media (max-width: 360px) {{
      .card-main-name {{ font-size: 2.9rem; }}
      .section-value-primary {{ font-size: 1.15rem; }}
      .btn-action {{ font-size: 0.88rem; padding: 12px 14px; }}
    }}
  </style>
</head>

<body>

  <!-- Ambient Golden Glows -->
  <div class="ambient-glow ambient-glow-top"></div>
  <div class="ambient-glow ambient-glow-bottom"></div>

  <!-- Particle canvas for floating golden dust / sparkles -->
  <canvas id="particle-canvas"></canvas>

  <!-- ============================================================
       INTRO / UNLOCK SCREEN (Garantiza reproducción de audio en móviles)
       ============================================================ -->
  <div id="intro-overlay">
    <div class="intro-box">
      <div class="intro-seal" id="intro-seal-btn" title="Toca para abrir">
        🍸
      </div>
      <p class="intro-tag">Invitación VIP</p>
      <h1 class="intro-title">Rubén</h1>
      <p class="intro-desc">
        Estás cordialmente invitado a celebrar una noche inolvidable.
        Toca para encender las luces y escuchar la dedicatoria.
      </p>
      <button class="btn-open-card" id="btn-open-card" type="button">
        <span>✨ ABRIR INVITACIÓN</span>
      </button>
    </div>
  </div>

  <!-- ============================================================
       TOP FLOATING TOOLBAR
       ============================================================ -->
  <header class="top-toolbar">
    <!-- Toggle Neon Light Switch -->
    <button class="toolbar-chip" id="neon-toggle-btn" type="button" title="Encender o apagar efecto de aviso luminoso">
      <span class="neon-indicator-dot" id="neon-dot"></span>
      <span id="neon-toggle-text">Neón: ON</span>
    </button>

    <!-- Music Status Chip -->
    <div class="toolbar-chip" id="music-chip-btn" title="Control de música">
      <div class="sound-equalizer" id="sound-eq">
        <span class="eq-bar"></span>
        <span class="eq-bar"></span>
        <span class="eq-bar"></span>
      </div>
      <span id="music-chip-text">Búscame</span>
    </div>
  </header>

  <!-- ============================================================
       MAIN INVITATION CARD (EXACT REPLICA + AVISO LUMINOSO)
       ============================================================ -->
  <main class="card-wrapper">
    <article class="invitation-card" id="main-card">
      <!-- Internal Double Border -->
      <div class="inner-border"></div>

      <!-- Neon Cocktail Coupe Icon -->
      <div class="neon-icon" id="cocktail-icon" title="¡Brindemos!">
        <svg viewBox="0 0 24 24">
          <!-- Stylized Coupe Glass -->
          <path d="M4 4h16l-7 8v7M9 20h6" />
          <!-- Sparkling liquid glow line -->
          <path d="M6.5 7h11" stroke="#fff" stroke-width="1.2" opacity="0.8" />
        </svg>
      </div>

      <!-- Header: Cumpleaños de Rubén -->
      <h2 class="card-subtitle-top">Cumpleaños de</h2>
      <h1 class="card-main-name neon-text" id="name-ruben">Rubén</h1>

      <!-- Divider -->
      <div class="card-divider"></div>

      <!-- SECTION: DÓNDE -->
      <section class="info-section">
        <h3 class="section-label">D Ó N D E</h3>
        <p class="section-value-primary">Alambique Bar</p>
        <p class="section-value-secondary">Honduras 4413, Palermo</p>
      </section>

      <!-- Divider -->
      <div class="card-divider"></div>

      <!-- SECTION: CUÁNDO -->
      <section class="info-section">
        <h3 class="section-label">C U Á N D O</h3>
        <p class="section-value-primary">Sábado 19/09 · 20 hs</p>

        <!-- Live Countdown Timer -->
        <div class="countdown-container">
          <p class="countdown-title">⏱️ CUENTA REGRESIVA</p>
          <div class="countdown-grid">
            <div class="countdown-box">
              <div class="countdown-num" id="cd-days">00</div>
              <div class="countdown-unit">Días</div>
            </div>
            <div class="countdown-box">
              <div class="countdown-num" id="cd-hours">00</div>
              <div class="countdown-unit">Horas</div>
            </div>
            <div class="countdown-box">
              <div class="countdown-num" id="cd-minutes">00</div>
              <div class="countdown-unit">Min</div>
            </div>
            <div class="countdown-box">
              <div class="countdown-num" id="cd-seconds">00</div>
              <div class="countdown-unit">Seg</div>
            </div>
          </div>
        </div>
      </section>

      <!-- Divider -->
      <div class="card-divider"></div>

      <!-- SECTION: VESTIMENTA -->
      <section class="info-section">
        <h3 class="section-label">V E S T I M E N T A</h3>
        <p class="section-value-primary">Blanco y negro</p>
        <div class="dresscode-badge">
          <span>👔 Dress Code: Black & White 👗</span>
        </div>
      </section>

      <!-- Divider -->
      <div class="card-divider"></div>

      <!-- FOOTER MESSAGE -->
      <footer class="card-footer-quote">
        No te lo pierdas, ¡habrá sorpresas!
      </footer>

      <!-- ============================================================
           ACTION BUTTONS (WHATSAPP, MAPS, CALENDAR, SHARE)
           ============================================================ -->
      <div class="button-stack">
        <!-- WhatsApp RSVP Button -->
        <button class="btn-action btn-whatsapp-rsvp" id="btn-rsvp" type="button">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.698c.969.586 1.761.777 2.796.777 3.182 0 5.768-2.587 5.768-5.766.001-3.187-2.575-5.964-5.768-5.964zm0 10.435c-.911 0-1.782-.249-2.545-.718l-.182-.108-1.891.496.505-1.843-.118-.188c-.517-.822-.791-1.773-.79-2.753.001-2.628 2.14-4.767 4.769-4.767 2.628 0 4.766 2.139 4.767 4.767-.001 2.628-2.139 5.114-4.766 5.114z"/>
          </svg>
          <span>Confirmar Asistencia por WhatsApp</span>
        </button>

        <!-- Google Maps Button -->
        <a class="btn-action btn-maps" id="btn-maps" target="_blank" rel="noopener noreferrer" href="https://www.google.com/maps/search/?api=1&query=Alambique+Bar,+Honduras+4413,+Palermo,+Buenos+Aires">
          <span>📍 Cómo llegar en Google Maps</span>
        </a>

        <!-- Calendar + Share Buttons -->
        <div class="btn-row">
          <button class="btn-action btn-secondary" id="btn-calendar" type="button">
            <span>📅 Agendar Fecha</span>
          </button>
          <button class="btn-action btn-secondary" id="btn-share" type="button">
            <span>📤 Compartir</span>
          </button>
        </div>
      </div>

      <!-- ============================================================
           MUSIC PLAYER WIDGET
           ============================================================ -->
      <section class="music-widget-card" id="music-card">
        <div class="music-header">
          <div class="music-meta">
            <div class="vinyl-disc" id="vinyl-disc"></div>
            <div>
              <p class="song-title">Búscame</p>
              <p class="song-artist">Orquesta Adolescentes</p>
            </div>
          </div>
          <div class="music-controls">
            <button class="btn-play-pause" id="btn-audio-toggle" type="button" title="Reproducir / Pausar">
              <span id="play-pause-icon">▶</span>
            </button>
          </div>
        </div>

        <!-- Lyrics Dropdown / Dedication Quote -->
        <button class="lyrics-toggle-btn" id="lyrics-toggle-btn" type="button">
          <span>📖 Ver fragmento de agradecimiento</span>
          <span id="lyrics-arrow">▼</span>
        </button>

        <div class="lyrics-box" id="lyrics-box">
          <p class="lyrics-content">
            “<span class="lyrics-highlight">Te agradezco, Señor, te doy mil gracias por todo lo que me diste a mí</span>, por todo lo que me rodea y por siempre acompañarme, por darme amor y poder respirar, por darme amigos y dejarme amar y vivir, <span class="lyrics-highlight">gracias por mi alma, gracias por darme todo, mi vida es tuya mi Dios</span>.”
          </p>
        </div>
      </section>

    </article>
  </main>

  <!-- Audio Element with Fallback -->
  <audio id="bg-audio" preload="auto" loop>
    <source src="audio_buscame.mp3" type="audio/mp3" />
    <source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3" />
  </audio>

  <!-- Toast Notification -->
  <div id="toast">¡Enlace copiado para compartir!</div>

  <!-- ============================================================
       SCRIPTS: AUDIO, INTERACTION, COUNTDOWN, PARTICLES
       ============================================================ -->
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      // DOM Elements
      const introOverlay = document.getElementById('intro-overlay');
      const btnOpenCard = document.getElementById('btn-open-card');
      const introSealBtn = document.getElementById('intro-seal-btn');
      const bgAudio = document.getElementById('bg-audio');
      const btnAudioToggle = document.getElementById('btn-audio-toggle');
      const playPauseIcon = document.getElementById('play-pause-icon');
      const musicCard = document.getElementById('music-card');
      const soundEq = document.getElementById('sound-eq');
      const neonToggleBtn = document.getElementById('neon-toggle-btn');
      const neonDot = document.getElementById('neon-dot');
      const neonToggleText = document.getElementById('neon-toggle-text');
      const lyricsToggleBtn = document.getElementById('lyrics-toggle-btn');
      const lyricsBox = document.getElementById('lyrics-box');
      const lyricsArrow = document.getElementById('lyrics-arrow');
      const btnRsvp = document.getElementById('btn-rsvp');
      const btnShare = document.getElementById('btn-share');
      const btnCalendar = document.getElementById('btn-calendar');
      const cocktailIcon = document.getElementById('cocktail-icon');
      const toast = document.getElementById('toast');

      let isPlaying = false;
      let neonOn = true;

      // -----------------------------------------------------------
      // AUDIO PLAYBACK HANDLER
      // -----------------------------------------------------------
      function playMusic() {{
        bgAudio.play().then(() => {{
          isPlaying = true;
          playPauseIcon.textContent = '❚❚';
          musicCard.classList.add('playing');
          soundEq.classList.add('playing');
        }}).catch(err => {{
          console.warn('Playback blocked or pending gesture:', err);
          isPlaying = false;
          playPauseIcon.textContent = '▶';
          musicCard.classList.remove('playing');
          soundEq.classList.remove('playing');
        }});
      }}

      function pauseMusic() {{
        bgAudio.pause();
        isPlaying = false;
        playPauseIcon.textContent = '▶';
        musicCard.classList.remove('playing');
        soundEq.classList.remove('playing');
      }}

      function toggleMusic() {{
        if (isPlaying) {{
          pauseMusic();
        }} else {{
          playMusic();
        }}
      }}

      btnAudioToggle.addEventListener('click', toggleMusic);
      document.getElementById('music-chip-btn').addEventListener('click', toggleMusic);

      // -----------------------------------------------------------
      // OPEN INVITATION SEQUENCE (Unlocks audio & fires confetti)
      // -----------------------------------------------------------
      function openInvitation() {{
        introOverlay.classList.add('hidden');
        playMusic();

        // Celebratory Gold & Champagne Confetti Burst
        if (typeof confetti === 'function') {{
          confetti({{
            particleCount: 80,
            spread: 70,
            origin: {{ y: 0.6 }},
            colors: ['#ffd89b', '#f5ba68', '#e68d2e', '#ffffff', '#ff9922']
          }});
          setTimeout(() => {{
            confetti({{
              particleCount: 50,
              angle: 60,
              spread: 55,
              origin: {{ x: 0 }},
              colors: ['#ffd89b', '#f5ba68', '#ffffff']
            }});
            confetti({{
              particleCount: 50,
              angle: 120,
              spread: 55,
              origin: {{ x: 1 }},
              colors: ['#ffd89b', '#f5ba68', '#ffffff']
            }});
          }}, 350);
        }}
      }}

      btnOpenCard.addEventListener('click', openInvitation);
      introSealBtn.addEventListener('click', openInvitation);

      // -----------------------------------------------------------
      // NEON LIGHT TOGGLE SWITCH
      // -----------------------------------------------------------
      neonToggleBtn.addEventListener('click', () => {{
        neonOn = !neonOn;
        if (neonOn) {{
          document.body.classList.remove('neon-off');
          neonDot.classList.remove('off');
          neonToggleText.textContent = 'Neón: ON';
          showToast('⚡ Aviso Luminoso: ENCENDIDO');
        }} else {{
          document.body.classList.add('neon-off');
          neonDot.classList.add('off');
          neonToggleText.textContent = 'Neón: OFF';
          showToast('💡 Aviso Luminoso: APAGADO');
        }}
      }});

      // -----------------------------------------------------------
      // LYRICS ACCORDION
      // -----------------------------------------------------------
      lyricsToggleBtn.addEventListener('click', () => {{
        const isOpen = lyricsBox.classList.toggle('open');
        lyricsArrow.textContent = isOpen ? '▲' : '▼';
      }});

      // -----------------------------------------------------------
      // COCKTAIL ICON TAP CELEBRATION
      // -----------------------------------------------------------
      cocktailIcon.addEventListener('click', (e) => {{
        if (typeof confetti === 'function') {{
          const rect = cocktailIcon.getBoundingClientRect();
          const x = (rect.left + rect.width / 2) / window.innerWidth;
          const y = (rect.top + rect.height / 2) / window.innerHeight;
          confetti({{
            particleCount: 30,
            spread: 60,
            origin: {{ x, y }},
            colors: ['#ffd89b', '#ff9922', '#ffffff']
          }});
        }}
      }});

      // -----------------------------------------------------------
      // WHATSAPP RSVP (Confirmar Asistencia)
      // -----------------------------------------------------------
      btnRsvp.addEventListener('click', () => {{
        const phone = "5491170259429";
        const message = encodeURIComponent(
          "¡Hola Rubén! 🥂 Confirmo con mucho gusto mi asistencia a tu fiesta de cumpleaños este Sábado 19/09 en Alambique Bar. ¡Allí estaré para celebrar juntos! 🎉✨"
        );
        window.open(`https://api.whatsapp.com/send?phone=${{phone}}&text=${{message}}`, '_blank');
      }});

      // -----------------------------------------------------------
      // SHARE INVITATION (Web Share API / WhatsApp Link)
      // -----------------------------------------------------------
      btnShare.addEventListener('click', async () => {{
        const shareTitle = "🎉 Cumpleaños de Rubén | Invitación VIP 🍸";
        const shareText = "¡Estás invitado al Cumpleaños de Rubén! Sábado 19/09 - 20 hs en Alambique Bar (Honduras 4413, Palermo). Toca el enlace para abrir la tarjeta interactiva con música y aviso luminoso:";
        const shareUrl = window.location.href;

        if (navigator.share) {{
          try {{
            await navigator.share({{
              title: shareTitle,
              text: `${{shareText}} ${{shareUrl}}`,
              url: shareUrl
            }});
          }} catch (err) {{
            console.log('Share canceled or error:', err);
          }}
        }} else {{
          // Fallback to WhatsApp Web link or clipboard copy
          const waShareUrl = `https://api.whatsapp.com/send?text=${{encodeURIComponent(shareText + ' ' + shareUrl)}}`;
          window.open(waShareUrl, '_blank');
          showToast('Abriendo WhatsApp para compartir...');
        }}
      }});

      // -----------------------------------------------------------
      // ADD TO CALENDAR (Google Calendar + iCal .ics download)
      // -----------------------------------------------------------
      btnCalendar.addEventListener('click', () => {{
        // Event data: Sábado 19 de Septiembre, 20:00 hs
        // Let's determine the upcoming Sept 19th
        const now = new Date();
        let targetYear = now.getFullYear();
        // If September 19 has already passed this year, set to next year
        const thisYearSept19 = new Date(targetYear, 8, 19, 20, 0, 0); // Month 8 is September
        if (now > thisYearSept19) {{
          targetYear += 1;
        }}

        // Format dates for Google Calendar (YYYYMMDDTHHmmssZ)
        // Buenos Aires is UTC-3 (20:00 ART = 23:00 UTC)
        const startIso = `${{targetYear}}0919T230000Z`;
        const endIso = `${{targetYear}}0920T050000Z`; // 6 hours event

        const title = encodeURIComponent("Cumpleaños de Rubén 🍸");
        const details = encodeURIComponent("Festejo de Cumpleaños de Rubén en Alambique Bar. Vestimenta: Blanco y negro. ¡No te lo pierdas, habrá sorpresas!");
        const location = encodeURIComponent("Alambique Bar, Honduras 4413, Palermo, CABA");

        const gCalUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${{title}}&dates=${{startIso}}/${{endIso}}&details=${{details}}&location=${{location}}`;

        // Open Google Calendar
        window.open(gCalUrl, '_blank');
        showToast('Abriendo Google Calendar...');
      }});

      // -----------------------------------------------------------
      // LIVE COUNTDOWN TIMER
      // Target: Sábado 19/09 at 20:00 ART
      // -----------------------------------------------------------
      function updateCountdown() {{
        const now = new Date();
        let targetYear = now.getFullYear();
        let targetDate = new Date(targetYear, 8, 19, 20, 0, 0);

        if (now > targetDate) {{
          targetDate = new Date(targetYear + 1, 8, 19, 20, 0, 0);
        }}

        const diffMs = targetDate - now;

        if (diffMs <= 0) {{
          document.getElementById('cd-days').textContent = '00';
          document.getElementById('cd-hours').textContent = '00';
          document.getElementById('cd-minutes').textContent = '00';
          document.getElementById('cd-seconds').textContent = '00';
          return;
        }}

        const days = Math.floor(diffMs / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diffMs % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((diffMs % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((diffMs % (1000 * 60)) / 1000);

        document.getElementById('cd-days').textContent = String(days).padStart(2, '0');
        document.getElementById('cd-hours').textContent = String(hours).padStart(2, '0');
        document.getElementById('cd-minutes').textContent = String(minutes).padStart(2, '0');
        document.getElementById('cd-seconds').textContent = String(seconds).padStart(2, '0');
      }}

      updateCountdown();
      setInterval(updateCountdown, 1000);

      // -----------------------------------------------------------
      // TOAST NOTIFICATION HELPER
      // -----------------------------------------------------------
      function showToast(msg) {{
        toast.textContent = msg;
        toast.classList.add('show');
        setTimeout(() => {{
          toast.classList.remove('show');
        }}, 2800);
      }}

      // -----------------------------------------------------------
      // PARTICLE CANVAS (Champagne bubbles & golden embers)
      // -----------------------------------------------------------
      const canvas = document.getElementById('particle-canvas');
      const ctx = canvas.getContext('2d');
      let particles = [];

      function resizeCanvas() {{
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
      }}
      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();

      class Particle {{
        constructor() {{
          this.reset();
        }}
        reset() {{
          this.x = Math.random() * canvas.width;
          this.y = canvas.height + Math.random() * 50;
          this.radius = Math.random() * 2.2 + 0.8;
          this.speedY = Math.random() * 0.9 + 0.3;
          this.speedX = (Math.random() - 0.5) * 0.5;
          this.opacity = Math.random() * 0.6 + 0.2;
          this.color = Math.random() > 0.3 ? '#ffaa33' : '#ffd89b';
        }}
        update() {{
          this.y -= this.speedY;
          this.x += this.speedX;
          if (this.y < -10) {{
            this.reset();
          }}
        }}
        draw() {{
          ctx.beginPath();
          ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
          ctx.fillStyle = this.color;
          ctx.globalAlpha = this.opacity;
          ctx.shadowBlur = 8;
          ctx.shadowColor = this.color;
          ctx.fill();
        }}
      }}

      const numParticles = Math.min(window.innerWidth < 600 ? 30 : 60, 60);
      for (let i = 0; i < numParticles; i++) {{
        const p = new Particle();
        p.y = Math.random() * canvas.height;
        particles.push(p);
      }}

      function animateParticles() {{
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {{
          p.update();
          p.draw();
        }});
        requestAnimationFrame(animateParticles);
      }}
      animateParticles();

    }});
  </script>
</body>
</html>
'''

with open('invitacion.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('invitacion.html generated successfully. Size:', len(html_template), 'bytes')
