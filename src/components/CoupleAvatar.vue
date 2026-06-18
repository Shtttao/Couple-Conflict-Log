<script setup>
import { ref, onMounted } from 'vue'

defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})

// 图片加载状态：true = 成功加载真实图片，false = 显示 SVG fallback
const boyLoaded = ref(false)
const girlLoaded = ref(false)

// 用运行时拼接路径，避免 Vite 静态分析时检查文件是否存在
const boySrc = '/images/couple-boy.png'
const girlSrc = '/images/couple-girl.png'

const onBoyLoad = () => { boyLoaded.value = true }
const onGirlLoad = () => { girlLoaded.value = true }
// 图片加载失败时保持 false，显示 SVG fallback
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">

    <!-- ========== 双人模式：并排显示 ========== -->
    <div v-if="variant === 'together'" class="avatar-wrap together-wrap">

      <!-- 男生圆形头像 -->
      <div class="photo-circle photo-boy">
        <!-- 优先显示真实照片 -->
        <img
          :src="boySrc"
          alt="男生头像"
          @load="onBoyLoad"
          @error="boyLoaded = false"
          v-show="boyLoaded"
        />
        <!-- SVG fallback（默认显示，直到图片加载成功后隐藏） -->
        <svg v-show="!boyLoaded" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="fallback-svg">
          <!-- 蓝色T恤 -->
          <path d="M20 78 Q50 70 80 78 L80 92 L20 92 Z" fill="#6b8ba8"/>
          <!-- 领口 -->
          <path d="M42 74 Q50 78 58 74" stroke="#4a6a88" stroke-width="1.2" fill="none"/>
          <!-- 脖子 -->
          <rect x="42" y="64" width="16" height="14" rx="4" fill="#f5d0b8"/>
          <!-- 头部 -->
          <ellipse cx="50" cy="46" rx="20" ry="22" fill="#f5d0b8"/>
          <!-- 头发（短发蓬松） -->
          <path d="M30 44 Q28 20 50 18 Q72 20 70 44 Q72 30 60 28 Q55 22 50 24 Q45 22 40 28 Q28 30 30 44 Z" fill="#3a3a3a"/>
          <!-- 刘海 -->
          <path d="M36 40 Q42 30 50 34 Q58 30 64 40 Q62 44 55 42 Q50 46 45 42 Q38 44 36 40 Z" fill="#2a2a2a"/>
          <!-- 腮红 -->
          <ellipse cx="38" cy="52" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.6"/>
          <ellipse cx="62" cy="52" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.6"/>
          <!-- 眼睛（大圆可爱眼） -->
          <circle cx="42" cy="46" r="3.5" fill="#2a2a2a"/>
          <circle cx="58" cy="46" r="3.5" fill="#2a2a2a"/>
          <circle cx="43.5" cy="45" r="1.2" fill="#fff"/>
          <circle cx="59.5" cy="45" r="1.2" fill="#fff"/>
          <!-- 眉毛 -->
          <path d="M38 40 Q42 37 46 40" stroke="#2a2a2a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
          <path d="M54 40 Q58 37 62 40" stroke="#2a2a2a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
          <!-- 微笑嘴巴 -->
          <path d="M44 58 Q50 62 56 58" stroke="#c07070" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <!-- 耳朵 -->
          <ellipse cx="30" cy="46" rx="3" ry="5" fill="#f5d0b8"/>
          <ellipse cx="70" cy="46" rx="3" ry="5" fill="#f5d0b8"/>
        </svg>
      </div>

      <!-- 中间的心形连接 -->
      <div class="heart-connector">♡</div>

      <!-- 女生圆形头像 -->
      <div class="photo-circle photo-girl">
        <img
          :src="girlSrc"
          alt="女生头像"
          @load="onGirlLoad"
          @error="girlLoaded = false"
          v-show="girlLoaded"
        />
        <!-- SVG fallback -->
        <svg v-show="!girlLoaded" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="fallback-svg">
          <!-- 长发（背后部分） -->
          <path d="M18 48 Q12 75 22 88 Q30 84 35 78 L35 72 Q25 75 22 60 Q18 55 18 48 Z" fill="#4a3a3a"/>
          <path d="M82 48 Q88 75 78 88 Q70 84 65 78 L65 72 Q75 75 78 60 Q82 55 82 48 Z" fill="#4a3a3a"/>
          <!-- 米白上衣 -->
          <path d="M22 82 Q50 74 78 82 L78 92 L22 92 Z" fill="#e8dcc8"/>
          <!-- 领口 -->
          <path d="M40 78 Q50 82 60 78" stroke="#d0c0a8" stroke-width="1.2" fill="none"/>
          <!-- 心形项链 -->
          <path d="M47 86 L50 90 L53 86 Q52 83 50 83 Q48 83 47 86 Z" fill="#ff9cb5" stroke="#d87890" stroke-width="0.6"/>
          <!-- 脖子 -->
          <rect x="42" y="62" width="16" height="16" rx="4" fill="#f5d8c0"/>
          <!-- 头部 -->
          <ellipse cx="50" cy="44" rx="20" ry="23" fill="#f5d8c0"/>
          <!-- 前发（刘海蓬松） -->
          <path d="M30 40 Q28 18 50 16 Q72 18 70 40 Q72 28 60 26 Q55 20 50 22 Q45 20 40 26 Q28 28 30 40 Z" fill="#4a3a3a"/>
          <!-- 刘海细节 -->
          <path d="M36 38 Q44 26 50 32 Q56 26 64 38 Q60 42 55 38 Q50 42 45 38 Q40 42 36 38 Z" fill="#3a2a2a"/>
          <!-- 侧发 -->
          <path d="M30 40 Q26 55 32 68 Q36 65 36 55 Q35 48 30 40 Z" fill="#4a3a3a"/>
          <path d="M70 40 Q74 55 68 68 Q64 65 64 55 Q65 48 70 40 Z" fill="#4a3a3a"/>
          <!-- 腮红（更明显） -->
          <ellipse cx="36" cy="52" rx="5" ry="3" fill="#ffb8b8" opacity="0.65"/>
          <ellipse cx="64" cy="52" rx="5" ry="3" fill="#ffb8b8" opacity="0.65"/>
          <!-- 眼睛（更大更圆，可爱感） -->
          <circle cx="42" cy="45" r="4" fill="#2a2a2a"/>
          <circle cx="58" cy="45" r="4" fill="#2a2a2a"/>
          <circle cx="43.5" cy="44" r="1.5" fill="#fff"/>
          <circle cx="59.5" cy="44" r="1.5" fill="#fff"/>
          <!-- 眉毛 -->
          <path d="M38 38 Q42 36 46 38" stroke="#3a2a2a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
          <path d="M54 38 Q58 36 62 38" stroke="#3a2a2a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
          <!-- 微笑嘴巴 -->
          <path d="M44 58 Q50 62 56 58" stroke="#c07070" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <!-- 耳朵 -->
          <ellipse cx="30" cy="48" rx="3" ry="5" fill="#f5d8c0"/>
          <ellipse cx="70" cy="48" rx="3" ry="5" fill="#f5d8c0"/>
        </svg>
      </div>

    </div>

    <!-- ========== 单人模式：只显示男生 ========== -->
    <div v-if="variant === 'bear'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-boy">
        <img
          :src="boySrc"
          alt="男生头像"
          @load="onBoyLoad"
          @error="boyLoaded = false"
          v-show="boyLoaded"
        />
        <svg v-show="!boyLoaded" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="fallback-svg">
          <path d="M20 78 Q50 70 80 78 L80 92 L20 92 Z" fill="#6b8ba8"/>
          <path d="M42 74 Q50 78 58 74" stroke="#4a6a88" stroke-width="1.2" fill="none"/>
          <rect x="42" y="64" width="16" height="14" rx="4" fill="#f5d0b8"/>
          <ellipse cx="50" cy="46" rx="20" ry="22" fill="#f5d0b8"/>
          <path d="M30 44 Q28 20 50 18 Q72 20 70 44 Q72 30 60 28 Q55 22 50 24 Q45 22 40 28 Q28 30 30 44 Z" fill="#3a3a3a"/>
          <path d="M36 40 Q42 30 50 34 Q58 30 64 40 Q62 44 55 42 Q50 46 45 42 Q38 44 36 40 Z" fill="#2a2a2a"/>
          <ellipse cx="38" cy="52" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.6"/>
          <ellipse cx="62" cy="52" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.6"/>
          <circle cx="42" cy="46" r="3.5" fill="#2a2a2a"/>
          <circle cx="58" cy="46" r="3.5" fill="#2a2a2a"/>
          <circle cx="43.5" cy="45" r="1.2" fill="#fff"/>
          <circle cx="59.5" cy="45" r="1.2" fill="#fff"/>
          <path d="M38 40 Q42 37 46 40" stroke="#2a2a2a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
          <path d="M54 40 Q58 37 62 40" stroke="#2a2a2a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
          <path d="M44 58 Q50 62 56 58" stroke="#c07070" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <ellipse cx="30" cy="46" rx="3" ry="5" fill="#f5d0b8"/>
          <ellipse cx="70" cy="46" rx="3" ry="5" fill="#f5d0b8"/>
        </svg>
      </div>
      <div class="name-tag tag-boy">小熊 ♡</div>
    </div>

    <!-- ========== 单人模式：只显示女生 ========== -->
    <div v-if="variant === 'bunny'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-girl">
        <img
          :src="girlSrc"
          alt="女生头像"
          @load="onGirlLoad"
          @error="girlLoaded = false"
          v-show="girlLoaded"
        />
        <svg v-show="!girlLoaded" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" class="fallback-svg">
          <path d="M18 48 Q12 75 22 88 Q30 84 35 78 L35 72 Q25 75 22 60 Q18 55 18 48 Z" fill="#4a3a3a"/>
          <path d="M82 48 Q88 75 78 88 Q70 84 65 78 L65 72 Q75 75 78 60 Q82 55 82 48 Z" fill="#4a3a3a"/>
          <path d="M22 82 Q50 74 78 82 L78 92 L22 92 Z" fill="#e8dcc8"/>
          <path d="M40 78 Q50 82 60 78" stroke="#d0c0a8" stroke-width="1.2" fill="none"/>
          <path d="M47 86 L50 90 L53 86 Q52 83 50 83 Q48 83 47 86 Z" fill="#ff9cb5" stroke="#d87890" stroke-width="0.6"/>
          <rect x="42" y="62" width="16" height="16" rx="4" fill="#f5d8c0"/>
          <ellipse cx="50" cy="44" rx="20" ry="23" fill="#f5d8c0"/>
          <path d="M30 40 Q28 18 50 16 Q72 18 70 40 Q72 28 60 26 Q55 20 50 22 Q45 20 40 26 Q28 28 30 40 Z" fill="#4a3a3a"/>
          <path d="M36 38 Q44 26 50 32 Q56 26 64 38 Q60 42 55 38 Q50 42 45 38 Q40 42 36 38 Z" fill="#3a2a2a"/>
          <ellipse cx="36" cy="52" rx="5" ry="3" fill="#ffb8b8" opacity="0.65"/>
          <ellipse cx="64" cy="52" rx="5" ry="3" fill="#ffb8b8" opacity="0.65"/>
          <circle cx="42" cy="45" r="4" fill="#2a2a2a"/>
          <circle cx="58" cy="45" r="4" fill="#2a2a2a"/>
          <circle cx="43.5" cy="44" r="1.5" fill="#fff"/>
          <circle cx="59.5" cy="44" r="1.5" fill="#fff"/>
          <path d="M38 38 Q42 36 46 38" stroke="#3a2a2a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
          <path d="M54 38 Q58 36 62 38" stroke="#3a2a2a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
          <path d="M44 58 Q50 62 56 58" stroke="#c07070" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          <ellipse cx="30" cy="48" rx="3" ry="5" fill="#f5d8c0"/>
          <ellipse cx="70" cy="48" rx="3" ry="5" fill="#f5d8c0"/>
        </svg>
      </div>
      <div class="name-tag tag-girl">小兔 ♡</div>
    </div>

    <!-- 装饰漂浮元素 -->
    <span class="floaty f1">♡</span>
    <span class="floaty f2">✿</span>
    <span class="floaty f3">☆</span>
    <span class="floaty f4">♡</span>

  </div>
</template>

<style scoped>
.couple-avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0;
  position: relative;
  padding: 10px 0;
}

/* ========== 照片圆形头像 ========== */
.photo-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow:
    0 10px 25px rgba(180, 150, 170, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(255, 200, 210, 0.3);
  transition: transform 0.4s ease;
}

.photo-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.fallback-svg {
  width: 100%;
  height: 100%;
  display: block;
}

/* 男生头像背景色边框 */
.photo-boy {
  box-shadow:
    0 10px 25px rgba(100, 150, 200, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(168, 204, 232, 0.4);
  background: linear-gradient(135deg, #e0ecf7, #a8cce8);
}

/* 女生头像背景色边框 */
.photo-girl {
  box-shadow:
    0 10px 25px rgba(240, 150, 180, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(252, 228, 236, 0.5);
  background: linear-gradient(135deg, #fce4ec, #f8bbd0);
}

/* ========== 尺寸调整 ========== */
.couple-avatar.big .photo-circle {
  width: 190px;
  height: 190px;
}

.couple-avatar.small .photo-circle {
  width: 90px;
  height: 90px;
}

/* ========== 双人并排布局 ========== */
.together-wrap {
  display: flex;
  align-items: center;
  gap: 18px;
  position: relative;
}

/* 中间的心形连接 */
.heart-connector {
  position: absolute;
  left: 50%;
  bottom: 12px;
  transform: translateX(-50%);
  font-size: 2rem;
  color: #ff6b9d;
  text-shadow: 0 2px 10px rgba(255, 107, 157, 0.4);
  z-index: 5;
  animation: heart-pulse 2s ease-in-out infinite;
}

/* ========== 名字标签 ========== */
.single-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.name-tag {
  margin-top: 12px;
  padding: 4px 14px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 500;
  text-align: center;
}

.tag-boy {
  background: linear-gradient(135deg, #d4e8f7, #a8cce8);
  color: #2a5a8a;
}

.tag-girl {
  background: linear-gradient(135deg, #fce4ec, #f8bbd0);
  color: #8a3a5a;
}

/* ========== 呼吸动画 ========== */
@keyframes breathe {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-3px) scale(1.02); }
}

.photo-boy {
  animation: breathe 4s ease-in-out infinite;
}

.photo-girl {
  animation: breathe 4.5s ease-in-out infinite;
  animation-delay: 0.8s;
}

@keyframes heart-pulse {
  0%, 100% { transform: translateX(-50%) scale(1); opacity: 0.85; }
  50% { transform: translateX(-50%) scale(1.2); opacity: 1; }
}

/* ========== 装饰漂浮元素 ========== */
.floaty {
  position: absolute;
  font-size: 1.2rem;
  opacity: 0.5;
  animation: floaty 6s ease-in-out infinite;
  pointer-events: none;
  z-index: 1;
}

.f1 { top: 0; right: 5%; animation-delay: 0s; color: #ff9cb5; font-size: 1.3rem; }
.f2 { bottom: 15%; left: 0%; animation-delay: 1.6s; color: #98bdff; font-size: 1.1rem; }
.f3 { top: 30%; right: 20%; animation-delay: 3s; color: #ffc08a; font-size: 0.95rem; }
.f4 { bottom: 35%; right: 25%; animation-delay: 4.5s; color: #c5a8ff; font-size: 1rem; }

@keyframes floaty {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.4; }
  50% { transform: translateY(-8px) rotate(12deg); opacity: 0.75; }
}

/* ========== 响应式 ========== */
@media (max-width: 480px) {
  .photo-circle {
    width: 100px;
    height: 100px;
  }
  .couple-avatar.big .photo-circle {
    width: 130px;
    height: 130px;
  }
  .heart-connector {
    font-size: 1.4rem;
    bottom: 4px;
  }
  .together-wrap {
    gap: 10px;
  }
}
</style>
