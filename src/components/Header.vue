<script setup>
import { useRouter } from 'vue-router'
import { usersMeta } from '../utils/auth.js'

const props = defineProps({
  user: { type: Object, required: true }
})
const emit = defineEmits(['logout'])

const router = useRouter()

function onLogout () {
  emit('logout')
  router.replace('/login')
}
</script>

<template>
  <header class="app-header">
    <div class="logo">
      <span class="logo-bubble">♡</span>
      <span class="logo-text">情侣吵架日记</span>
    </div>
    <div class="user-chip" :class="'chip-' + user.color">
      <span class="chip-avatar">{{ user.role === 'me' ? '🐻' : '🐰' }}</span>
      <span class="chip-name">{{ user.displayName }}</span>
      <button class="chip-logout" @click="onLogout" title="退出登录">✕</button>
    </div>
  </header>
</template>

<style scoped>
.app-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  max-width: 1080px;
  margin: 0 auto;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-bubble {
  display: inline-flex;
  width: 36px;
  height: 36px;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffc0d3, #c3b8ff);
  color: #fff;
  box-shadow: 0 6px 14px rgba(255, 160, 190, 0.4);
  font-size: 1.1rem;
}

.logo-text {
  font-weight: 700;
  color: var(--cocoa);
  letter-spacing: 0.3px;
  font-size: 1.02rem;
}

.user-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 6px 6px 12px;
  border-radius: 999px;
  background: #fff;
  box-shadow: 0 6px 16px rgba(180, 190, 255, 0.28);
  font-size: 0.88rem;
}

.chip-avatar {
  font-size: 1.1rem;
}

.chip-name {
  color: var(--cocoa);
}

.chip-logout {
  border: none;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: #fff0f6;
  color: #c45d7a;
  cursor: pointer;
  transition: all 0.2s;
  font-size: 0.85rem;
}

.chip-logout:hover {
  background: #ffd9e3;
  transform: rotate(90deg);
}

.chip-sky { background: linear-gradient(135deg, #eaf3ff, #ffffff); }
.chip-pink { background: linear-gradient(135deg, #fff0f6, #ffffff); }

@media (max-width: 480px) {
  .logo-text { display: none; }
}
</style>
