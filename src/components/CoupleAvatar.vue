<script setup>
import { computed, ref } from 'vue'
import { useAvatarStore } from '../utils/avatarStore.js'

const props = defineProps({
  variant: { type: String, default: 'together' }, // together / bear / bunny
  size: { type: String, default: 'medium' } // small / medium / big
})

const avatarStore = useAvatarStore()

const boyAvatar = computed(() => avatarStore.getAvatar('boy'))
const girlAvatar = computed(() => avatarStore.getAvatar('girl'))

// 上传功能（可选 — 通过 ref 从父组件调用）
const boyInput = ref(null)
const girlInput = ref(null)
const uploading = ref(false)

async function onPick (role, event) {
  const file = event.target.files?.[0]
  if (!file) return
  uploading.value = true
  try {
    await avatarStore.setAvatarFromFile(role, file)
  } finally {
    uploading.value = false
    event.target.value = ''
  }
}

function reset (role) {
  if (confirm('确定恢复默认头像吗？')) {
    avatarStore.resetAvatar(role)
  }
}

// 暴露操作方法，便于父组件直接调用
defineExpose({
  pickBoy: () => boyInput.value?.click(),
  pickGirl: () => girlInput.value?.click(),
  resetBoy: () => reset('boy'),
  resetGirl: () => reset('girl'),
  hasBoy: () => avatarStore.hasCustom('boy'),
  hasGirl: () => avatarStore.hasCustom('girl')
})
</script>

<template>
  <div class="couple-avatar" :class="[variant, size]">
    <!-- 双人模式：并排显示 -->
    <div v-if="variant === 'together'" class="avatar-wrap together-wrap">
      <div class="photo-circle photo-boy">
        <img :src="boyAvatar" alt="小熊头像" class="avatar-img" />
      </div>
      <div class="heart-connector">♡</div>
      <div class="photo-circle photo-girl">
        <img :src="girlAvatar" alt="小兔头像" class="avatar-img" />
      </div>
    </div>

    <!-- 单人：小熊（男生） -->
    <div v-else-if="variant === 'bear'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-boy big-circle">
        <img :src="boyAvatar" alt="小熊头像" class="avatar-img" />
      </div>
    </div>

    <!-- 单人：小兔（女生） -->
    <div v-else-if="variant === 'bunny'" class="avatar-wrap single-wrap">
      <div class="photo-circle photo-girl big-circle">
        <img :src="girlAvatar" alt="小兔头像" class="avatar-img" />
      </div>
    </div>

    <span class="floaty">✿</span>
    <span class="floaty small">☆</span>

    <!-- 隐藏文件输入框，由外部触发 -->
    <input
      ref="boyInput"
      type="file"
      accept="image/png,image/jpeg,image/webp"
      style="display:none"
      @change="onPick('boy', $event)"
    />
    <input
      ref="girlInput"
      type="file"
      accept="image/png,image/jpeg,image/webp"
      style="display:none"
      @change="onPick('girl', $event)"
    />
  </div>
</template>

<style scoped>
.couple-avatar {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  position: relative;
  padding: 6px;
}

.avatar-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}

.together-wrap {
  gap: 18px;
}

.photo-circle {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  position: relative;
  box-shadow:
    0 10px 25px rgba(180, 150, 170, 0.35),
    0 0 0 5px rgba(255, 255, 255, 0.9),
    0 0 0 7px rgba(255, 200, 210, 0.3);
  transition: transform 0.3s ease;
  background: linear-gradient(135deg, #ffeef5, #e8f0ff);
  flex-shrink: 0;
}

.photo-boy {
  background: linear-gradient(135deg, #e0ecf7, #a8cce8);
  animation: breathe 4.5s ease-in-out infinite;
}

.photo-girl {
  background: linear-gradient(135deg, #fce4ec, #f8bbd0);
  animation: breathe 4.5s ease-in-out 0.6s infinite;
}

.photo-boy::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  box-shadow: inset 0 0 0 2px rgba(168, 204, 232, 0.5);
  pointer-events: none;
}

.photo-girl::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  box-shadow: inset 0 0 0 2px rgba(248, 187, 208, 0.5);
  pointer-events: none;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 50%;
}

.big-circle {
  width: 150px;
  height: 150px;
}

/* 尺寸变体 */
.couple-avatar.big .photo-circle {
  width: 150px;
  height: 150px;
}
.couple-avatar.big .big-circle {
  width: 170px;
  height: 170px;
}

.couple-avatar.small .photo-circle {
  width: 80px;
  height: 80px;
}

/* 心形连接器 */
.heart-connector {
  position: absolute;
  left: 50%;
  bottom: 8px;
  transform: translateX(-50%);
  font-size: 1.8rem;
  color: #ff6b9d;
  animation: heart-pulse 2s ease-in-out infinite;
  text-shadow: 0 2px 4px rgba(255, 107, 157, 0.3);
  z-index: 10;
  pointer-events: none;
}

/* 双人模式：头像稍微错开 */
.couple-avatar.together .photo-boy {
  transform: translateY(-6px);
}

.couple-avatar.together .photo-girl {
  transform: translateY(2px);
}

/* 漂浮装饰 */
.floaty {
  position: absolute;
  font-size: 1.2rem;
  color: #ff9cb5;
  opacity: 0.5;
  animation: floaty 7s ease-in-out infinite;
  pointer-events: none;
}
.floaty:nth-child(odd) {
  top: -8px;
  right: -4px;
  color: #ffb6c1;
}
.floaty:nth-child(even) {
  bottom: -4px;
  left: -2px;
  animation-delay: 2.5s;
  color: #b6c9ff;
}
.floaty.small {
  font-size: 0.9rem;
}

/* ============================================================
   动画
   ============================================================ */
@keyframes breathe {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-4px) scale(1.02); }
}

@keyframes heart-pulse {
  0%, 100% { transform: translateX(-50%) scale(1); opacity: 1; }
  50% { transform: translateX(-50%) scale(1.2); opacity: 0.85; }
}

@keyframes floaty {
  0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.45; }
  50% { transform: translateY(-8px) rotate(8deg); opacity: 0.7; }
}

/* ============================================================
   移动端响应式
   ============================================================ */
@media (max-width: 480px) {
  .photo-circle {
    width: 100px;
    height: 100px;
  }
  .couple-avatar.big .photo-circle {
    width: 120px;
    height: 120px;
  }
  .couple-avatar.big .big-circle {
    width: 140px;
    height: 140px;
  }
  .together-wrap { gap: 14px; }
  .heart-connector { font-size: 1.4rem; bottom: 6px; }
}

@media (max-width: 360px) {
  .photo-circle {
    width: 85px;
    height: 85px;
  }
  .couple-avatar.big .photo-circle {
    width: 105px;
    height: 105px;
  }
  .together-wrap { gap: 10px; }
}
</style>
