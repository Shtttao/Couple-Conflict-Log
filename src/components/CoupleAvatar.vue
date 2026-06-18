<script setup>
defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">
    <!-- ============ BOY - 蓬松短发、蓝色T恤、柔和表情 ============ -->
    <svg v-if="variant !== 'bunny'" class="avatar bear" viewBox="0 0 160 180" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- 男生背景 - 淡蓝色 -->
        <radialGradient id="bgBoy" cx="50%" cy="45%">
          <stop offset="0%" stop-color="#d4e8f7" />
          <stop offset="100%" stop-color="#a8cce8" />
        </radialGradient>
        <!-- 蓝色T恤 -->
        <linearGradient id="shirtBoy" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#7ba3c8" />
          <stop offset="100%" stop-color="#5a8ab8" />
        </linearGradient>
        <!-- 肤色 -->
        <radialGradient id="skinBoy" cx="50%" cy="45%">
          <stop offset="0%" stop-color="#ffe8d8" />
          <stop offset="100%" stop-color="#f5d4c0" />
        </radialGradient>
        <!-- 头发 -->
        <linearGradient id="hairBoy" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#3a3a3a" />
          <stop offset="100%" stop-color="#1a1a1a" />
        </linearGradient>
      </defs>

      <!-- 背景圆形 -->
      <circle cx="80" cy="90" r="70" fill="url(#bgBoy)" opacity="0.6" />

      <!-- 身体/T恤 -->
      <path d="M25 170 Q25 130 80 125 Q135 130 135 170 Z" fill="url(#shirtBoy)" />
      <!-- 领口 -->
      <path d="M60 125 Q80 135 100 125" stroke="#4a7aa5" stroke-width="1.5" fill="none" stroke-linecap="round" />
      <!-- 领口内侧 -->
      <path d="M65 125 Q80 132 95 125" stroke="#6a9ac5" stroke-width="1" fill="none" opacity="0.5" />
      <!-- 衣服上的小方块logo -->
      <rect x="72" y="152" width="8" height="8" rx="1.5" fill="#e8e8e8" opacity="0.8" />
      <rect x="74" y="154" width="4" height="4" rx="0.5" fill="#b0b0b0" opacity="0.5" />

      <!-- 脖子 -->
      <rect x="68" y="108" width="24" height="22" rx="8" fill="url(#skinBoy)" />
      <!-- 脖子阴影 -->
      <path d="M68 120 Q80 126 92 120" stroke="#e0c0a8" stroke-width="1" fill="none" opacity="0.4" />

      <!-- 头部 -->
      <ellipse cx="80" cy="68" rx="42" ry="44" fill="url(#skinBoy)" />

      <!-- ===== 头发（蓬松短发，多层） ===== -->
      <!-- 头发主体 - 蓬松感 -->
      <path
        d="M36 60
           Q32 25 55 18
           Q70 12 80 14
           Q90 12 105 18
           Q128 25 124 60
           Q126 48 115 44
           Q110 35 95 32
           Q85 28 80 30
           Q75 28 65 32
           Q50 35 45 44
           Q34 48 36 60 Z"
        fill="url(#hairBoy)"
      />
      <!-- 顶部蓬松 -->
      <path d="M55 18 Q70 8 80 10 Q90 8 105 18 Q95 14 80 16 Q65 14 55 18 Z" fill="url(#hairBoy)" />
      <!-- 左侧头发 -->
      <path d="M36 60 Q34 72 40 82 Q44 78 44 68 Z" fill="url(#hairBoy)" />
      <!-- 右侧头发 -->
      <path d="M124 60 Q126 72 120 82 Q116 78 116 68 Z" fill="url(#hairBoy)" />
      <!-- 刘海 - 自然分开 -->
      <path d="M48 48 Q55 38 65 42 Q62 52 55 54 Q48 56 48 48 Z" fill="url(#hairBoy)" />
      <path d="M65 40 Q75 34 85 40 Q82 50 75 52 Q68 50 65 40 Z" fill="url(#hairBoy)" />
      <path d="M85 40 Q95 36 105 44 Q102 54 95 56 Q88 54 85 40 Z" fill="url(#hairBoy)" />
      <path d="M105 44 Q112 42 118 52 Q115 58 108 58 Q104 54 105 44 Z" fill="url(#hairBoy)" />
      <!-- 头发高光 -->
      <ellipse cx="60" cy="28" rx="8" ry="4" fill="#555" opacity="0.3" />
      <ellipse cx="100" cy="30" rx="6" ry="3" fill="#555" opacity="0.3" />

      <!-- 耳朵 -->
      <ellipse cx="38" cy="72" rx="6" ry="10" fill="url(#skinBoy)" />
      <ellipse cx="122" cy="72" rx="6" ry="10" fill="url(#skinBoy)" />
      <!-- 耳朵内侧 -->
      <ellipse cx="38" cy="72" rx="3" ry="6" fill="#f0c8b0" opacity="0.5" />
      <ellipse cx="122" cy="72" rx="3" ry="6" fill="#f0c8b0" opacity="0.5" />

      <!-- 腮红 -->
      <ellipse cx="52" cy="82" rx="10" ry="7" fill="#ffb8b8" opacity="0.5" />
      <ellipse cx="108" cy="82" rx="10" ry="7" fill="#ffb8b8" opacity="0.5" />

      <!-- 眼睛（大圆眼，可爱风格） -->
      <!-- 左眼 -->
      <ellipse cx="62" cy="66" rx="9" ry="11" fill="#2a2a2a" />
      <ellipse cx="62" cy="67" rx="7" ry="9" fill="#3a3a3a" />
      <!-- 右眼 -->
      <ellipse cx="98" cy="66" rx="9" ry="11" fill="#2a2a2a" />
      <ellipse cx="98" cy="67" rx="7" ry="9" fill="#3a3a3a" />
      <!-- 眼睛高光 -->
      <circle cx="65" cy="62" r="3.5" fill="#fff" />
      <circle cx="101" cy="62" r="3.5" fill="#fff" />
      <circle cx="59" cy="69" r="1.5" fill="#fff" opacity="0.7" />
      <circle cx="95" cy="69" r="1.5" fill="#fff" opacity="0.7" />

      <!-- 眉毛 -->
      <path d="M52 52 Q62 48 72 52" stroke="#3a3a3a" stroke-width="2" fill="none" stroke-linecap="round" />
      <path d="M88 52 Q98 48 108 52" stroke="#3a3a3a" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- 鼻子 -->
      <path d="M78 78 Q80 80 82 78 Q80 82 78 78 Z" fill="#e0a890" opacity="0.6" />

      <!-- 嘴巴（柔和微笑） -->
      <path d="M68 88 Q80 96 92 88" stroke="#c07070" stroke-width="2" fill="none" stroke-linecap="round" />
    </svg>

    <!-- ============ GIRL - 长发、米白上衣、心形项链 ============ -->
    <svg v-if="variant !== 'bear'" class="avatar bunny" viewBox="0 0 160 180" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- 女生背景 - 淡粉色 -->
        <radialGradient id="bgGirl" cx="50%" cy="45%">
          <stop offset="0%" stop-color="#fce4ec" />
          <stop offset="100%" stop-color="#f8bbd0" />
        </radialGradient>
        <!-- 米白上衣 -->
        <linearGradient id="shirtGirl" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#f5f0e8" />
          <stop offset="100%" stop-color="#e8e0d0" />
        </linearGradient>
        <!-- 肤色 -->
        <radialGradient id="skinGirl" cx="50%" cy="45%">
          <stop offset="0%" stop-color="#fff0e0" />
          <stop offset="100%" stop-color="#f5e0d0" />
        </radialGradient>
        <!-- 头发 -->
        <linearGradient id="hairGirl" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#4a3a3a" />
          <stop offset="100%" stop-color="#2a1a1a" />
        </linearGradient>
      </defs>

      <!-- 背景圆形 -->
      <circle cx="80" cy="90" r="70" fill="url(#bgGirl)" opacity="0.6" />

      <!-- ===== 长发（背后） ===== -->
      <!-- 左侧长发 -->
      <path
        d="M20 70
           Q12 110 22 150
           Q28 165 40 170
           L55 170
           Q48 140 50 110
           Q52 90 48 75
           Q35 72 30 65
           Q24 68 20 70 Z"
        fill="url(#hairGirl)"
      />
      <!-- 右侧长发 -->
      <path
        d="M140 70
           Q148 110 138 150
           Q132 165 120 170
           L105 170
           Q112 140 110 110
           Q108 90 112 75
           Q125 72 130 65
           Q136 68 140 70 Z"
        fill="url(#hairGirl)"
      />
      <!-- 头发底部波浪 -->
      <path d="M40 170 Q55 175 70 170 Q85 175 100 170" stroke="url(#hairGirl)" stroke-width="8" fill="none" stroke-linecap="round" />

      <!-- 身体/米白上衣 -->
      <path d="M25 170 Q25 132 80 128 Q135 132 135 170 Z" fill="url(#shirtGirl)" />
      <!-- 领口 -->
      <path d="M62 128 Q80 138 98 128" stroke="#d0c8b8" stroke-width="1.5" fill="none" stroke-linecap="round" />
      <!-- 衣服褶皱 -->
      <path d="M40 150 Q50 155 60 150" stroke="#e0d8c8" stroke-width="1" fill="none" opacity="0.5" />
      <path d="M100 155 Q110 160 120 155" stroke="#e0d8c8" stroke-width="1" fill="none" opacity="0.5" />

      <!-- 脖子 -->
      <rect x="68" y="108" width="24" height="24" rx="8" fill="url(#skinGirl)" />
      <!-- 脖子阴影 -->
      <path d="M68 120 Q80 126 92 120" stroke="#e0c8b0" stroke-width="1" fill="none" opacity="0.4" />

      <!-- 头部 -->
      <ellipse cx="80" cy="68" rx="42" ry="44" fill="url(#skinGirl)" />

      <!-- ===== 前发（刘海） ===== -->
      <path
        d="M36 58
           Q34 22 55 16
           Q70 10 80 12
           Q90 10 105 16
           Q126 22 124 58
           Q122 42 110 38
           Q100 30 85 28
           Q80 26 75 28
           Q60 30 50 38
           Q38 42 36 58 Z"
        fill="url(#hairGirl)"
      />
      <!-- 刘海细节 -->
      <path d="M48 42 Q55 34 62 38 Q58 46 52 48 Q46 46 48 42 Z" fill="url(#hairGirl)" />
      <path d="M62 36 Q70 30 78 36 Q75 44 68 46 Q62 44 62 36 Z" fill="url(#hairGirl)" />
      <path d="M78 36 Q86 32 94 38 Q90 46 84 48 Q78 46 78 36 Z" fill="url(#hairGirl)" />
      <path d="M94 38 Q102 36 108 44 Q104 50 98 50 Q94 48 94 38 Z" fill="url(#hairGirl)" />
      <!-- 头发高光 -->
      <ellipse cx="55" cy="24" rx="10" ry="4" fill="#5a4a4a" opacity="0.4" />
      <ellipse cx="105" cy="26" rx="8" ry="3" fill="#5a4a4a" opacity="0.4" />

      <!-- 耳朵 -->
      <ellipse cx="38" cy="72" rx="6" ry="10" fill="url(#skinGirl)" />
      <ellipse cx="122" cy="72" rx="6" ry="10" fill="url(#skinGirl)" />
      <!-- 耳朵内侧 -->
      <ellipse cx="38" cy="72" rx="3" ry="6" fill="#f0d8c8" opacity="0.5" />
      <ellipse cx="122" cy="72" rx="3" ry="6" fill="#f0d8c8" opacity="0.5" />

      <!-- 腮红（更明显） -->
      <ellipse cx="52" cy="82" rx="11" ry="8" fill="#ffb8b8" opacity="0.55" />
      <ellipse cx="108" cy="82" rx="11" ry="8" fill="#ffb8b8" opacity="0.55" />

      <!-- 眼睛（大圆眼，比男生更大更可爱） -->
      <!-- 左眼 -->
      <ellipse cx="62" cy="64" rx="10" ry="12" fill="#2a2a2a" />
      <ellipse cx="62" cy="65" rx="8" ry="10" fill="#3a3a3a" />
      <!-- 右眼 -->
      <ellipse cx="98" cy="64" rx="10" ry="12" fill="#2a2a2a" />
      <ellipse cx="98" cy="65" rx="8" ry="10" fill="#3a3a3a" />
      <!-- 眼睛高光 -->
      <circle cx="65" cy="60" r="4" fill="#fff" />
      <circle cx="101" cy="60" r="4" fill="#fff" />
      <circle cx="59" cy="68" r="2" fill="#fff" opacity="0.7" />
      <circle cx="95" cy="68" r="2" fill="#fff" opacity="0.7" />

      <!-- 眉毛 -->
      <path d="M52 50 Q62 46 72 50" stroke="#3a2a2a" stroke-width="2" fill="none" stroke-linecap="round" />
      <path d="M88 50 Q98 46 108 50" stroke="#3a2a2a" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- 鼻子 -->
      <path d="M78 76 Q80 78 82 76 Q80 80 78 76 Z" fill="#e0a890" opacity="0.6" />

      <!-- 嘴巴（柔和微笑） -->
      <path d="M68 86 Q80 94 92 86" stroke="#c07070" stroke-width="2" fill="none" stroke-linecap="round" />

      <!-- ===== 心形项链 ===== -->
      <!-- 项链链条 -->
      <path d="M62 128 Q80 140 98 128" stroke="#c8a8a0" stroke-width="1.2" fill="none" opacity="0.7" />
      <!-- 心形吊坠 -->
      <g transform="translate(76 132)">
        <path d="M0 3 C -3 -1 -8 0 -8 5 C -8 11 0 16 0 16 C 0 16 8 11 8 5 C 8 0 3 -1 0 3 Z"
              fill="#e8a0a0" stroke="#c88080" stroke-width="0.8" />
      </g>
    </svg>

    <!-- 装饰漂浮元素 -->
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
  align-items: center;
  justify-content: center;
  gap: 16px;
  position: relative;
}

.avatar {
  width: 150px;
  height: 170px;
  filter: drop-shadow(0 8px 16px rgba(180, 150, 170, 0.3));
}

.couple-avatar.big .avatar { width: 190px; height: 215px; }
.couple-avatar.small .avatar { width: 96px; height: 108px; }

.couple-avatar.together .avatar.bear { z-index: 1; }
.couple-avatar.together .avatar.bunny { z-index: 2; }

/* 微妙的呼吸动画 */
@keyframes breathe {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-2px); }
}
.avatar.bear { animation: breathe 4s ease-in-out infinite; }
.avatar.bunny { animation: breathe 4.5s ease-in-out infinite; animation-delay: 1s; }

.floaty {
  position: absolute;
  font-size: 1rem;
  opacity: 0.5;
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
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.4; }
  50% { transform: translateY(-6px) rotate(12deg); opacity: 0.75; }
}

@keyframes sparkle {
  0%, 100% { transform: scale(0.8) rotate(0deg); opacity: 0.3; }
  50% { transform: scale(1.3) rotate(180deg); opacity: 0.7; }
}

@media (max-width: 480px) {
  .avatar { width: 120px; height: 135px; }
  .couple-avatar.big .avatar { width: 150px; height: 170px; }
}
</style>
