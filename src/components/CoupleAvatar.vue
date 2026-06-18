<script setup>
defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">
    <!-- BEAR (loverA / Little Bear - Boy with dark hair, blue shirt) -->
    <svg v-if="variant !== 'bunny'" class="avatar bear" viewBox="0 0 120 140" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="bgBear" cx="50%" cy="40%">
          <stop offset="0%" stop-color="#cfe0ff" />
          <stop offset="100%" stop-color="#a7c5ee" />
        </radialGradient>
        <linearGradient id="shirtBear" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#9bb7e0" />
          <stop offset="100%" stop-color="#7d9cd0" />
        </linearGradient>
      </defs>

      <!-- soft background circle -->
      <circle cx="60" cy="70" r="55" fill="url(#bgBear)" opacity="0.45" />

      <!-- shoulders / shirt -->
      <path d="M18 130 Q18 95 60 92 Q102 95 102 130 Z" fill="url(#shirtBear)" />
      <!-- neck -->
      <rect x="50" y="82" width="20" height="14" rx="6" fill="#ffe3cf" />

      <!-- head -->
      <ellipse cx="60" cy="58" rx="34" ry="34" fill="#ffe3cf" />
      <!-- hair top -->
      <path
        d="M28 50 Q30 22 60 22 Q92 24 92 52 Q88 40 78 42 Q72 30 60 32 Q48 28 44 42 Q34 40 28 50 Z"
        fill="#3a3a44"
      />
      <!-- hair bangs -->
      <path d="M40 46 Q48 38 58 44 Q54 50 48 50 Q42 52 40 46 Z" fill="#3a3a44" />
      <path d="M58 44 Q68 38 74 46 Q72 54 64 52 Q58 52 58 44 Z" fill="#3a3a44" />
      <path d="M74 46 Q82 44 86 54 Q82 58 76 54 Z" fill="#3a3a44" />

      <!-- cheeks -->
      <circle cx="42" cy="68" r="5" fill="#ffb6b6" opacity="0.65" />
      <circle cx="78" cy="68" r="5" fill="#ffb6b6" opacity="0.65" />

      <!-- eyes -->
      <ellipse cx="48" cy="60" rx="3.2" ry="4.2" fill="#2b2b36" />
      <ellipse cx="72" cy="60" rx="3.2" ry="4.2" fill="#2b2b36" />
      <!-- eye highlights -->
      <circle cx="49" cy="58.5" r="1" fill="#fff" />
      <circle cx="73" cy="58.5" r="1" fill="#fff" />

      <!-- eyebrows -->
      <path d="M42 52 Q48 49 54 52" stroke="#3a3a44" stroke-width="2" fill="none" stroke-linecap="round" />
      <path d="M66 52 Q72 49 78 52" stroke="#3a3a44" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- nose -->
      <ellipse cx="60" cy="66" rx="2.5" ry="1.8" fill="#e8a68d" />

      <!-- mouth (small smile) -->
      <path d="M54 73 Q60 78 66 73" stroke="#b8606c" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- little heart pocket on shirt -->
      <g transform="translate(52 110)">
        <path d="M0 2 C -3 -2 -8 0 -8 4 C -8 9 0 14 0 14 C 0 14 8 9 8 4 C 8 0 3 -2 0 2 Z"
              fill="#fff" opacity="0.9" />
      </g>
    </svg>

    <!-- BUNNY (loverB / Sweet Bunny - Girl with long dark hair, cream shirt) -->
    <svg v-if="variant !== 'bear'" class="avatar bunny" viewBox="0 0 120 140" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <radialGradient id="bgBun" cx="50%" cy="40%">
          <stop offset="0%" stop-color="#ffd9e3" />
          <stop offset="100%" stop-color="#ffc0cf" />
        </radialGradient>
        <linearGradient id="shirtBun" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#fff2e6" />
          <stop offset="100%" stop-color="#ffe0cc" />
        </linearGradient>
      </defs>

      <circle cx="60" cy="70" r="55" fill="url(#bgBun)" opacity="0.45" />

      <!-- hair back (long waves) behind head -->
      <path
        d="M22 60 Q18 100 32 128 L52 128 Q44 100 48 78 Q30 78 32 60 Z"
        fill="#5a3a3a"
      />
      <path
        d="M98 60 Q102 100 88 128 L68 128 Q76 100 72 78 Q90 78 88 60 Z"
        fill="#5a3a3a"
      />

      <!-- shoulders / shirt -->
      <path d="M20 130 Q20 95 60 92 Q100 95 100 130 Z" fill="url(#shirtBun)" />
      <!-- neck -->
      <rect x="50" y="82" width="20" height="14" rx="6" fill="#ffe3cf" />

      <!-- head -->
      <ellipse cx="60" cy="58" rx="34" ry="35" fill="#ffe3cf" />

      <!-- front hair -->
      <path
        d="M28 48 Q30 22 60 20 Q92 22 94 50 Q92 38 78 36 Q72 28 60 30 Q48 26 44 38 Q34 38 28 48 Z"
        fill="#5a3a3a"
      />
      <!-- side bangs -->
      <path d="M28 50 Q34 66 42 66 Q38 58 32 58 Z" fill="#5a3a3a" />
      <path d="M94 50 Q88 66 80 66 Q84 58 90 58 Z" fill="#5a3a3a" />

      <!-- cheeks -->
      <circle cx="42" cy="68" r="5" fill="#ffb6b6" opacity="0.65" />
      <circle cx="78" cy="68" r="5" fill="#ffb6b6" opacity="0.65" />

      <!-- eyes (bigger, more kawaii) -->
      <ellipse cx="48" cy="61" rx="3.8" ry="5" fill="#2b2b36" />
      <ellipse cx="72" cy="61" rx="3.8" ry="5" fill="#2b2b36" />
      <circle cx="49" cy="59" r="1.4" fill="#fff" />
      <circle cx="73" cy="59" r="1.4" fill="#fff" />
      <circle cx="47.5" cy="62.5" r="0.7" fill="#fff" />
      <circle cx="71.5" cy="62.5" r="0.7" fill="#fff" />

      <!-- eyebrows -->
      <path d="M42 52 Q48 50 54 52" stroke="#5a3a3a" stroke-width="2" fill="none" stroke-linecap="round" />
      <path d="M66 52 Q72 50 78 52" stroke="#5a3a3a" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- nose -->
      <path d="M58 66 Q60 68 62 66 Q60 69 58 66 Z" fill="#e8a68d" />

      <!-- mouth -->
      <path d="M55 74 Q60 78 65 74" stroke="#b8606c" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- heart necklace -->
      <g transform="translate(56 108)">
        <path d="M0 2 C -2 -1 -6 0 -6 3 C -6 7 0 11 0 11 C 0 11 6 7 6 3 C 6 0 2 -1 0 2 Z"
              fill="#ff9cb5" stroke="#e27a96" stroke-width="0.8" />
      </g>
      <!-- necklace string -->
      <path d="M50 96 Q60 104 70 96" stroke="#e27a96" stroke-width="1.2" fill="none" opacity="0.6" />
    </svg>

    <!-- decorative floating hearts -->
    <span class="floaty f1">♡</span>
    <span class="floaty f2">✿</span>
    <span class="floaty f3">☆</span>
  </div>
</template>

<style scoped>
.couple-avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  position: relative;
}

.avatar {
  width: 120px;
  height: 140px;
  filter: drop-shadow(0 8px 14px rgba(180, 140, 170, 0.25));
}

.couple-avatar.big .avatar { width: 150px; height: 175px; }
.couple-avatar.small .avatar { width: 76px; height: 90px; }

.couple-avatar.together .avatar.bear { transform: translateY(-4px); }
.couple-avatar.together .avatar.bunny { transform: translateY(2px); }

.floaty {
  position: absolute;
  font-size: 1rem;
  color: #ff9cb5;
  opacity: 0.55;
  animation: floaty 6s ease-in-out infinite;
  pointer-events: none;
}
.f1 { top: 4%; right: -6%; animation-delay: 0s; color: #ff9cb5; }
.f2 { bottom: 8%; left: -6%; animation-delay: 1.6s; color: #98bdff; }
.f3 { top: 30%; left: 38%; animation-delay: 3s; color: #ffc08a; font-size: 0.85rem; }

@keyframes floaty {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.45; }
  50% { transform: translateY(-6px) rotate(10deg); opacity: 0.75; }
}

@media (max-width: 480px) {
  .avatar { width: 100px; height: 120px; }
  .couple-avatar.big .avatar { width: 120px; height: 140px; }
}
</style>
