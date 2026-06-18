<script setup>
import { ref } from 'vue'

defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})

// 图片加载失败的状态
const boyImgError = ref(false)
const girlImgError = ref(false)

const onBoyError = () => { boyImgError.value = true }
const onGirlError = () => { girlImgError.value = true }
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">

    <!-- ========== 双人模式：并排显示 ========== -->
    <div v-if="variant === 'together'" class="avatar-wrap together-wrap">

      <!-- 男生圆形头像 -->
      <div class="photo-circle photo-boy">
        <!-- 优先显示照片 -->
        <img v-if="!boyImgError" src="/images/couple-boy.png" alt="男生头像" @error="onBoyError" />
        <!-- 照片加载失败时，显示一个优雅备用头像 -->
        <div v-else class="fallback-boy">
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="40" r="18" fill="#5a4a3a"/>
            <path d="M20 75 Q50 60 80 75 L80 90 L20 90 Z" fill="#6b8ba8"/>
            <circle cx="40" cy="42" r="4" fill="#fff"/>
            <circle cx="60" cy="42" r="4" fill="#fff"/>
            <path d="M40 52 Q50 58 60 52" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
      </div>

      <!-- 中间的心形连接 -->
      <div class="heart-connector">♡</div>

      <!-- 女生圆形头像 -->
      <div class="photo-circle photo-girl">
        <img v-if="!girlImgError" src="/images/couple-girl.png" alt="女生头像" @error="onGirlError" />
        <div v-else class="fallback-girl">
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M30 35 Q50 20 70 35 Q72 55 65 70 Q50 65 35 70 Q28 55 30 35 Z" fill="#4a3a3a"/>
            <ellipse cx="50" cy="55" rx="18" ry="20" fill="#ffd5c0"/>
            <circle cx="42" cy="55" r="3.5" fill="#2a2a2a"/>
            <circle cx="58" cy="55" r="3.5" fill="#2a2a2a"/>
            <path d="M42 65 Q50 72 58 65" stroke="#c07070" stroke-width="1.8" fill="none" stroke-linecap="round"/>
          </svg>
        </div>
      </div>

    </div>

    <!-- ========== 单人模式：只显示男生 ========== -->
    <div v-if="variant === 'bear'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-boy">
        <img v-if="!boyImgError" src="/images/couple-boy.png" alt="男生头像" @error="onBoyError" />
        <div v-else class="fallback-boy">
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M25 38 Q50 25 75 38 Q78 58 72 72 L68 72 Q50 60 32 72 L28 72 Q22 58 25 38 Z" fill="#3a3a3a"/>
            <circle cx="50" cy="50" r="16" fill="#ffd5c0"/>
            <circle cx="42" cy="52" r="3.5" fill="#2a2a2a"/>
            <circle cx="58" cy="52" r="3.5" fill="#2a2a2a"/>
            <circle cx="43" cy="51" r="1.2" fill="#fff"/>
            <circle cx="57" cy="51" r="1.2" fill="#fff"/>
            <ellipse cx="38" cy="58" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.5"/>
            <ellipse cx="62" cy="58" rx="4" ry="2.5" fill="#ffb8b8" opacity="0.5"/>
            <path d="M40 65 Q50 70 60 65" stroke="#c07070" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M25 78 Q50 70 75 78 L75 90 L25 90 Z" fill="#6b8ba8"/>
          </svg>
        </div>
      </div>
      <div class="name-tag tag-boy">小熊 ♡</div>
    </div>

    <!-- ========== 单人模式：只显示女生 ========== -->
    <div v-if="variant === 'bunny'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-girl">
        <img v-if="!girlImgError" src="/images/couple-girl.png" alt="女生头像" @error="onGirlError" />
        <div v-else class="fallback-girl">
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M25 35 Q50 18 75 35 Q82 70 70 80 Q70 75 65 72 Q50 80 35 72 Q30 75 30 80 Q18 70 25 35 Z" fill="#4a3a3a"/>
            <circle cx="50" cy="48" r="17" fill="#ffd5c0"/>
            <circle cx="40" cy="50" r="4" fill="#2a2a2a"/>
            <circle cx="60" cy="50" r="4" fill="#2a2a2a"/>
            <circle cx="41" cy="49" r="1.5" fill="#fff"/>
            <circle cx="61" cy="49" r="1.5" fill="#fff"/>
            <ellipse cx="36" cy="57" rx="5" ry="3" fill="#ffb8b8" opacity="0.55"/>
            <ellipse cx="64" cy="57" rx="5" ry="3" fill="#ffb8b8" opacity="0.55"/>
            <path d="M40 62 Q50 68 60 62" stroke="#c07070" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M25 82 Q50 74 75 82 L75 90 L25 90 Z" fill="#e8dcc8"/>
            <path d="M40 78 Q50 82 60 78" stroke="#d0c0a8" stroke-width="1.5" fill="none"/>
            <path d="M47 85 Q50 88 53 85 Q50 90 47 85 Z" fill="#ffb8b8"/>
          </svg>
        </div>
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

.photo-circle svg {
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
  background: linear-gradient(135deg, #d4e8f7, #a8cce8);
}

.fallback-boy {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #e8f0f8, #bcd0e4);
}

/* 女生头像背景色边框 */
.photo-girl {
  box-shadow:
    0 10px 25px rgba(240, 150, 180, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(252, 228, 236, 0.5);
  background: linear-gradient(135deg, #fce4ec, #f8bbd0);
}

.fallback-girl {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #f8e8ee, #f0c4d4);
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

/* 让两个头像稍微靠近，像靠在一起 */
.together-wrap .photo-boy,
.together-wrap .photo-girl {
  z-index: 2;
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
  0%, 100% { transform: translateX(-50%) scale(1); opacity: 0.8; }
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
