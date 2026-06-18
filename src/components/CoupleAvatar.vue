<script setup>
defineProps({
  variant: { type: String, default: 'together' },
  size: { type: String, default: 'medium' }
})
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">

    <!-- 双人模式 -->
    <div v-if="variant === 'together'" class="avatar-wrap together-wrap">
      <div class="photo-circle photo-boy">
        <img src="/images/couple-boy.png" alt="小熊头像" />
      </div>
      <div class="heart-connector">♡</div>
      <div class="photo-circle photo-girl">
        <img src="/images/couple-girl.png" alt="小兔头像" />
      </div>
    </div>

    <!-- 单人男生模式 -->
    <div v-if="variant === 'bear'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-boy">
        <img src="/images/couple-boy.png" alt="小熊头像" />
      </div>
      <div class="name-tag tag-boy">小熊 ♡</div>
    </div>

    <!-- 单人女生模式 -->
    <div v-if="variant === 'bunny'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-girl">
        <img src="/images/couple-girl.png" alt="小兔头像" />
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

.photo-boy {
  box-shadow:
    0 10px 25px rgba(100, 150, 200, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(168, 204, 232, 0.4);
  background: linear-gradient(135deg, #e0ecf7, #a8cce8);
}

.photo-girl {
  box-shadow:
    0 10px 25px rgba(240, 150, 180, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(252, 228, 236, 0.5);
  background: linear-gradient(135deg, #fce4ec, #f8bbd0);
}

.couple-avatar.big .photo-circle {
  width: 190px;
  height: 190px;
}

.couple-avatar.small .photo-circle {
  width: 90px;
  height: 90px;
}

.together-wrap {
  display: flex;
  align-items: center;
  gap: 18px;
  position: relative;
}

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
