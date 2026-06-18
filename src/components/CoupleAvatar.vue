<script setup>
defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">
    <!-- ============ BOY (Little Bear) - fluffy short hair, soft round eyes ============ -->
    <svg v-if="variant !== 'bunny'" class="avatar bear" viewBox="0 0 140 170" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="bgBear" cx="50%" cy="40%">
          <stop offset="0%" stop-color="#ffe3ec" />
          <stop offset="100%" stop-color="#c6d8f5" />
        </radialGradient>
        <linearGradient id="shirtBear" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#b6ccef" />
          <stop offset="100%" stop-color="#89a8d0" />
        </linearGradient>
        <!-- hair shadow -->
        <linearGradient id="hairBear" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#4a4652" />
          <stop offset="100%" stop-color="#2b2b36" />
        </linearGradient>
      </defs>

      <!-- soft glow background circle -->
      <circle cx="70" cy="85" r="62" fill="url(#bgBear)" opacity="0.5" />

      <!-- shoulders / shirt (wider for more casual look) -->
      <path d="M16 160 Q16 115 70 112 Q124 115 124 160 Z" fill="url(#shirtBear)" stroke="#6d8ab5" stroke-width="1.5" stroke-linejoin="round" />
      <!-- collar -->
      <path d="M58 112 Q70 120 82 112" stroke="#6d8ab5" stroke-width="1.5" fill="none" stroke-linecap="round" />

      <!-- neck -->
      <rect x="60" y="100" width="20" height="18" rx="6" fill="#ffe3cf" />
      <path d="M60 110 Q70 116 80 110" stroke="#e0b89a" stroke-width="1" fill="none" opacity="0.5" />

      <!-- ==== HEAD ==== -->
      <ellipse cx="70" cy="68" rx="36" ry="38" fill="#ffe3cf" stroke="#d4b896" stroke-width="0.8" />

      <!-- ===== HAIR (fluffy short style with volume) ===== -->
      <!-- main hair top -- fluffy rounded shape -->
      <path
        d="M34 62
           Q30 30 70 22
           Q110 30 106 62
           Q104 48 94 44
           Q90 32 70 30
           Q50 32 46 44
           Q36 48 34 62 Z"
        fill="url(#hairBear)"
        stroke="#1a1a24"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <!-- hair tuft on top -->
      <path d="M64 24 Q70 16 76 24 Q74 22 70 24 Q66 22 64 24 Z" fill="url(#hairBear)" stroke="#1a1a24" stroke-width="1.2" />

      <!-- side hair pieces -->
      <path d="M34 62 Q32 72 38 80 Q42 76 42 68 Z" fill="url(#hairBear)" stroke="#1a1a24" stroke-width="1.2" stroke-linejoin="round" />
      <path d="M106 62 Q108 72 102 80 Q98 76 98 68 Z" fill="url(#hairBear)" stroke="#1a1a24" stroke-width="1.2" stroke-linejoin="round" />

      <!-- front bangs (rounded, natural fall) -->
      <path
        d="M42 50
           Q46 42 54 46
           Q52 54 46 58
           Q40 56 42 50 Z"
        fill="url(#hairBear)"
        stroke="#1a1a24"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M56 44
           Q64 38 72 44
           Q70 52 62 54
           Q54 52 56 44 Z"
        fill="url(#hairBear)"
        stroke="#1a1a24"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M74 44
           Q82 40 88 50
           Q86 56 78 58
           Q74 54 74 44 Z"
        fill="url(#hairBear)"
        stroke="#1a1a24"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M88 48
           Q94 46 100 54
           Q98 60 90 60
           Q86 56 88 48 Z"
        fill="url(#hairBear)"
        stroke="#1a1a24"
        stroke-width="1.2"
        stroke-linejoin="round"
      />

      <!-- ==== EYES (soft round eyes, warm friendly look) ==== -->
      <ellipse cx="56" cy="66" rx="3.8" ry="5" fill="#1a1a24" />
      <ellipse cx="84" cy="66" rx="3.8" ry="5" fill="#1a1a24" />
      <!-- main highlight -->
      <circle cx="57.2" cy="64.5" r="1.6" fill="#fff" />
      <circle cx="85.2" cy="64.5" r="1.6" fill="#fff" />
      <!-- secondary tiny highlight -->
      <circle cx="54.5" cy="68.5" r="0.7" fill="#fff" opacity="0.8" />
      <circle cx="82.5" cy="68.5" r="0.7" fill="#fff" opacity="0.8" />

      <!-- eyebrows (soft, thin arcs) -->
      <path d="M48 55 Q56 52 64 55" stroke="#1a1a24" stroke-width="1.8" fill="none" stroke-linecap="round" />
      <path d="M76 55 Q84 52 92 55" stroke="#1a1a24" stroke-width="1.8" fill="none" stroke-linecap="round" />

      <!-- ==== CHEEKS (soft pink blush - noticeable!) ==== -->
      <ellipse cx="48" cy="78" rx="6" ry="4" fill="#ff9cb5" opacity="0.55" />
      <ellipse cx="92" cy="78" rx="6" ry="4" fill="#ff9cb5" opacity="0.55" />
      <!-- extra blush gradient dots for cute effect -->
      <circle cx="44" cy="79" r="1.2" fill="#ffb8cb" opacity="0.7" />
      <circle cx="96" cy="79" r="1.2" fill="#ffb8cb" opacity="0.7" />

      <!-- ==== NOSE (soft little dot) ==== -->
      <ellipse cx="70" cy="74" rx="2" ry="1.5" fill="#e8a68d" opacity="0.7" />

      <!-- ==== MOUTH (gentle small smile) ==== -->
      <path d="M62 84 Q70 90 78 84" stroke="#b8606c" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" />

      <!-- ==== SHIRT HEART POCKET ==== -->
      <g transform="translate(58 130)">
        <path d="M0 4 C -4 -2 -12 -1 -12 7 C -12 16 0 22 0 22 C 0 22 12 16 12 7 C 12 -1 4 -2 0 4 Z"
              fill="#fff" stroke="#6d8ab5" stroke-width="1.2" stroke-linejoin="round" />
      </g>

      <!-- ==== DOODLE COLOR LINES (like the user's 5th image - colorful scribbles) ==== -->
      <path d="M22 90 Q18 100 24 110" stroke="#ff9cb5" stroke-width="1.5" fill="none" opacity="0.7" stroke-linecap="round" />
      <path d="M118 96 Q122 106 116 116" stroke="#a8d0ff" stroke-width="1.5" fill="none" opacity="0.7" stroke-linecap="round" />
      <circle cx="30" cy="140" r="2" fill="#ffc08a" opacity="0.6" />
      <circle cx="110" cy="140" r="2" fill="#c5a8ff" opacity="0.6" />
    </svg>

    <!-- ============ GIRL (Sweet Bunny) - long flowing hair, big eyes ============ -->
    <svg v-if="variant !== 'bear'" class="avatar bunny" viewBox="0 0 140 170" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="bgBun" cx="50%" cy="40%">
          <stop offset="0%" stop-color="#ffe0ea" />
          <stop offset="100%" stop-color="#ffc2d4" />
        </radialGradient>
        <linearGradient id="shirtBun" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#f9e6d4" />
          <stop offset="100%" stop-color="#f2d4b8" />
        </linearGradient>
        <linearGradient id="hairBun" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#5a3a3a" />
          <stop offset="50%" stop-color="#4a2a2a" />
          <stop offset="100%" stop-color="#2a1818" />
        </linearGradient>
      </defs>

      <circle cx="70" cy="85" r="62" fill="url(#bgBun)" opacity="0.5" />

      <!-- ===== LONG HAIR (flowing down on both sides) ===== -->
      <!-- hair back - left big wave -->
      <path
        d="M20 68
           Q14 110 28 150
           L50 150
           Q42 118 48 92
           Q30 90 28 78
           Q24 72 20 68 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <!-- hair back - right big wave -->
      <path
        d="M120 68
           Q126 110 112 150
           L90 150
           Q98 118 92 92
           Q110 90 112 78
           Q116 72 120 68 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />

      <!-- shoulders / shirt -->
      <path d="M18 160 Q18 115 70 112 Q122 115 122 160 Z" fill="url(#shirtBun)" stroke="#d8b895" stroke-width="1.5" stroke-linejoin="round" />
      <!-- collar -->
      <path d="M58 112 Q70 120 82 112" stroke="#d8b895" stroke-width="1.5" fill="none" stroke-linecap="round" />

      <!-- neck -->
      <rect x="60" y="100" width="20" height="18" rx="6" fill="#ffe3cf" />
      <path d="M60 110 Q70 116 80 110" stroke="#e0b89a" stroke-width="1" fill="none" opacity="0.5" />

      <!-- head -->
      <ellipse cx="70" cy="68" rx="36" ry="38" fill="#ffe3cf" stroke="#d4b896" stroke-width="0.8" />

      <!-- ==== FRONT HAIR (voluminous top + soft bangs) ==== -->
      <path
        d="M32 56
           Q30 22 70 18
           Q110 22 108 56
           Q106 40 92 38
           Q88 26 70 26
           Q52 26 48 38
           Q34 40 32 56 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <!-- top hair tuft -->
      <path d="M62 20 Q70 10 78 20 Q76 18 70 20 Q64 18 62 20 Z" fill="url(#hairBun)" stroke="#1a1014" stroke-width="1.2" />

      <!-- side face-framing hair -->
      <path d="M32 58 Q28 70 34 82 Q40 78 42 68 Z" fill="url(#hairBun)" stroke="#1a1014" stroke-width="1.2" stroke-linejoin="round" />
      <path d="M108 58 Q112 70 106 82 Q100 78 98 68 Z" fill="url(#hairBun)" stroke="#1a1014" stroke-width="1.2" stroke-linejoin="round" />

      <!-- front bangs (softer, curtain style) -->
      <path
        d="M40 48
           Q46 40 54 46
           Q52 54 48 58
           Q40 56 40 48 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M52 44
           Q62 36 70 42
           Q68 52 60 54
           Q52 52 52 44 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M72 42
           Q80 38 88 48
           Q86 56 78 58
           Q72 54 72 42 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />
      <path
        d="M88 48
           Q96 44 102 54
           Q100 60 92 60
           Q86 56 88 48 Z"
        fill="url(#hairBun)"
        stroke="#1a1014"
        stroke-width="1.2"
        stroke-linejoin="round"
      />

      <!-- ==== EYES (large round kawaii eyes with double highlights) ==== -->
      <ellipse cx="56" cy="66" rx="4.5" ry="6" fill="#1a1014" />
      <ellipse cx="84" cy="66" rx="4.5" ry="6" fill="#1a1014" />
      <!-- iris hint (soft brown reflection) -->
      <ellipse cx="56" cy="67" rx="3" ry="4" fill="#3a2424" opacity="0.5" />
      <ellipse cx="84" cy="67" rx="3" ry="4" fill="#3a2424" opacity="0.5" />
      <!-- main highlight -->
      <circle cx="57.5" cy="64" r="1.8" fill="#fff" />
      <circle cx="85.5" cy="64" r="1.8" fill="#fff" />
      <!-- bottom tiny highlight -->
      <circle cx="54.5" cy="69.5" r="0.8" fill="#fff" opacity="0.85" />
      <circle cx="82.5" cy="69.5" r="0.8" fill="#fff" opacity="0.85" />

      <!-- eyebrows -->
      <path d="M48 54 Q56 51 64 54" stroke="#2a1818" stroke-width="1.8" fill="none" stroke-linecap="round" />
      <path d="M76 54 Q84 51 92 54" stroke="#2a1818" stroke-width="1.8" fill="none" stroke-linecap="round" />

      <!-- ==== CHEEKS (bigger, warmer blush) ==== -->
      <ellipse cx="46" cy="78" rx="7" ry="5" fill="#ff9cb5" opacity="0.6" />
      <ellipse cx="94" cy="78" rx="7" ry="5" fill="#ff9cb5" opacity="0.6" />
      <circle cx="42" cy="80" r="1.3" fill="#ffb8cb" opacity="0.75" />
      <circle cx="98" cy="80" r="1.3" fill="#ffb8cb" opacity="0.75" />
      <!-- tiny heart blush dots -->
      <circle cx="50" cy="81" r="0.8" fill="#ffd6e0" opacity="0.8" />
      <circle cx="90" cy="81" r="0.8" fill="#ffd6e0" opacity="0.8" />

      <!-- ==== NOSE (tiny) ==== -->
      <path d="M68 74 Q70 76.5 72 74 Q70 77 68 74 Z" fill="#e8a68d" opacity="0.8" />

      <!-- ==== MOUTH (small cute smile) ==== -->
      <path d="M63 84 Q70 90 77 84" stroke="#b8606c" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" />

      <!-- ==== HEART NECKLACE ==== -->
      <path d="M52 110 Q70 122 88 110" stroke="#e27a96" stroke-width="1.2" fill="none" opacity="0.7" />
      <g transform="translate(66 114)">
        <path d="M0 3 C -3 -1 -9 0 -9 6 C -9 13 0 18 0 18 C 0 18 9 13 9 6 C 9 0 3 -1 0 3 Z"
              fill="#ff9cb5" stroke="#e27a96" stroke-width="1" stroke-linejoin="round" />
      </g>

      <!-- ==== DOODLE COLOR LINES (matching the boy's style) ==== -->
      <path d="M24 92 Q20 104 26 114" stroke="#c5a8ff" stroke-width="1.5" fill="none" opacity="0.7" stroke-linecap="round" />
      <path d="M116 98 Q120 108 114 118" stroke="#ffb8cb" stroke-width="1.5" fill="none" opacity="0.7" stroke-linecap="round" />
      <circle cx="32" cy="145" r="2" fill="#ffc08a" opacity="0.6" />
      <circle cx="108" cy="145" r="2" fill="#a8d0ff" opacity="0.6" />
    </svg>

    <!-- decorative floating hearts & doodles -->
    <span class="floaty f1">♡</span>
    <span class="floaty f2">✿</span>
    <span class="floaty f3">☆</span>
    <span class="floaty f4">♡</span>
    <span class="doodle-sparkle">✦</span>
  </div>
</template>

<style scoped>
.couple-avatar {
  display: inline-flex;
  align-items: flex-end;
  justify-content: center;
  gap: 0px;
  position: relative;
}

.avatar {
  width: 130px;
  height: 160px;
  filter: drop-shadow(0 10px 18px rgba(200, 150, 180, 0.35));
}

.couple-avatar.big .avatar { width: 170px; height: 210px; }
.couple-avatar.small .avatar { width: 84px; height: 102px; }

/* overlap them slightly like a couple photo */
.couple-avatar.together .avatar.bear { transform: translateY(-6px) rotate(-1deg); z-index: 1; }
.couple-avatar.together .avatar.bunny { transform: translateY(2px) translateX(-20px) rotate(1.5deg); z-index: 2; }

/* subtle breathing animation */
@keyframes breathe {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-2px); }
}
.avatar.bear { animation: breathe 4s ease-in-out infinite; }
.avatar.bunny { animation: breathe 4.5s ease-in-out infinite; animation-delay: 1s; }

.floaty {
  position: absolute;
  font-size: 1rem;
  opacity: 0.55;
  animation: floaty 6s ease-in-out infinite;
  pointer-events: none;
}
.f1 { top: 2%; right: 8%; animation-delay: 0s; color: #ff9cb5; font-size: 1.3rem; }
.f2 { bottom: 12%; left: 2%; animation-delay: 1.6s; color: #98bdff; font-size: 1.1rem; }
.f3 { top: 30%; left: 48%; animation-delay: 3s; color: #ffc08a; font-size: 0.95rem; }
.f4 { bottom: 30%; right: 15%; animation-delay: 4.5s; color: #c5a8ff; font-size: 1rem; }

.doodle-sparkle {
  position: absolute;
  top: 18%;
  left: 20%;
  font-size: 1rem;
  color: #ffd700;
  opacity: 0.5;
  animation: sparkle 2.5s ease-in-out infinite;
  pointer-events: none;
}

@keyframes floaty {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.45; }
  50% { transform: translateY(-6px) rotate(12deg); opacity: 0.8; }
}

@keyframes sparkle {
  0%, 100% { transform: scale(0.8) rotate(0deg); opacity: 0.3; }
  50% { transform: scale(1.3) rotate(180deg); opacity: 0.7; }
}

@media (max-width: 480px) {
  .avatar { width: 100px; height: 120px; }
  .couple-avatar.big .avatar { width: 130px; height: 160px; }
}
</style>
