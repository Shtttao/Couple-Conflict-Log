<script setup>
import { useRouter } from 'vue-router'
import { ref, computed } from 'vue'
import { useAvatarStore } from '../utils/avatarStore.js'

const props = defineProps({
  user: { type: Object, required: true }
})
const emit = defineEmits(['logout'])

const router = useRouter()
const avatarStore = useAvatarStore()

// 当前用户的头像（根据 role 决定）
const avatarUrl = computed(() =>
  props.user?.role === 'me'
    ? avatarStore.getAvatar('boy')
    : avatarStore.getAvatar('girl')
)

const showMenu = ref(false)

const fileInput = ref(null)
const otherFileInput = ref(null)

function onLogout () {
  showMenu.value = false
  emit('logout')
  router.replace('/login')
}

function toggleMenu () {
  showMenu.value = !showMenu.value
}

function closeMenu () {
  showMenu.value = false
}

function pickMyAvatar () {
  showMenu.value = false
  fileInput.value?.click()
}

function pickPartnerAvatar () {
  showMenu.value = false
  otherFileInput.value?.click()
}

function resetMyAvatar () {
  showMenu.value = false
  if (confirm('确定恢复默认头像吗？')) {
    avatarStore.resetAvatar(props.user?.role === 'me' ? 'boy' : 'girl')
  }
}

function resetPartnerAvatar () {
  showMenu.value = false
  if (confirm('确定恢复对方的默认头像吗？')) {
    avatarStore.resetAvatar(props.user?.role === 'me' ? 'girl' : 'boy')
  }
}

async function onFile (event, role) {
  const file = event.target.files?.[0]
  if (!file) return
  await avatarStore.setAvatarFromFile(role, file)
  event.target.value = ''
}
</script>

<template>
  <header class="app-header">
    <div class="logo">
      <span class="logo-bubble">♡</span>
      <span class="logo-text">情侣吵架日记</span>
    </div>

    <div class="user-area" @click.stop>
      <button class="user-chip" :class="'chip-' + user.color" @click="toggleMenu" aria-label="账户菜单">
        <span class="chip-avatar">
          <img :src="avatarUrl" :alt="user.displayName" />
        </span>
        <span class="chip-name">{{ user.displayName }}</span>
        <span class="chip-caret">▾</span>
      </button>

      <transition name="fade">
        <div v-if="showMenu" class="dropdown" role="menu" @click.stop>
          <div class="dropdown-title">自定义头像</div>
          <button class="menu-item" @click="pickMyAvatar">
            <span class="mi-icon">📷</span>
            <span class="mi-text">更换 {{ user.displayName }} 的头像</span>
          </button>
          <button class="menu-item" @click="pickPartnerAvatar">
            <span class="mi-icon">📷</span>
            <span class="mi-text">更换对方的头像</span>
          </button>
          <div class="divider"></div>
          <button class="menu-item" @click="resetMyAvatar">
            <span class="mi-icon">↺</span>
            <span class="mi-text">恢复 {{ user.displayName }} 默认</span>
          </button>
          <button class="menu-item" @click="resetPartnerAvatar">
            <span class="mi-icon">↺</span>
            <span class="mi-text">恢复对方默认</span>
          </button>
          <div class="divider"></div>
          <button class="menu-item menu-danger" @click="onLogout">
            <span class="mi-icon">✕</span>
            <span class="mi-text">退出登录</span>
          </button>
        </div>
      </transition>

      <!-- 点击空白处关闭菜单 -->
      <div v-if="showMenu" class="backdrop" @click="closeMenu"></div>
    </div>

    <!-- 隐藏的文件输入框 -->
    <input
      ref="fileInput"
      type="file"
      accept="image/png,image/jpeg,image/webp"
      style="display:none"
      @change="onFile($event, user.role === 'me' ? 'boy' : 'girl')"
    />
    <input
      ref="otherFileInput"
      type="file"
      accept="image/png,image/jpeg,image/webp"
      style="display:none"
      @change="onFile($event, user.role === 'me' ? 'girl' : 'boy')"
    />
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
  position: relative;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.logo-bubble {
  display: inline-flex;
  width: 38px;
  height: 38px;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  background: linear-gradient(135deg, #ffc0d3, #c3b8ff);
  color: #fff;
  box-shadow: 0 6px 14px rgba(255, 160, 190, 0.4);
  font-size: 1.2rem;
}

.logo-text {
  font-weight: 700;
  color: var(--cocoa);
  letter-spacing: 0.3px;
  font-size: 1.05rem;
}

.user-area {
  position: relative;
}

.user-chip {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 4px 12px 4px 4px;
  border-radius: 999px;
  background: #fff;
  border: none;
  box-shadow: 0 6px 16px rgba(180, 190, 255, 0.28);
  font-size: 0.88rem;
  cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
  font-family: inherit;
  min-height: 38px;
}

.user-chip:hover {
  transform: translateY(-1px);
  box-shadow: 0 8px 20px rgba(180, 190, 255, 0.35);
}

.user-chip:active {
  transform: scale(0.97);
}

.chip-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff0f6;
  box-shadow: inset 0 0 0 1.5px rgba(255, 200, 210, 0.6);
}

.chip-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.chip-name {
  color: var(--cocoa);
}

.chip-caret {
  color: #b5a6bd;
  font-size: 0.7rem;
}

/* 下拉菜单 */
.backdrop {
  position: fixed;
  inset: 0;
  z-index: 99;
}

.dropdown {
  position: absolute;
  top: calc(100% + 8px);
  right: 0;
  min-width: 240px;
  background: #fff;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(120, 110, 160, 0.25), 0 0 0 1px rgba(255, 200, 210, 0.3);
  padding: 8px;
  z-index: 100;
  overflow: hidden;
}

.dropdown-title {
  font-size: 0.75rem;
  color: #b5a6bd;
  padding: 6px 12px 8px;
  font-weight: 600;
}

.menu-item {
  width: 100%;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 12px;
  border-radius: 12px;
  border: none;
  background: transparent;
  color: var(--cocoa);
  text-align: left;
  cursor: pointer;
  font-size: 0.9rem;
  font-family: inherit;
  transition: background 0.15s;
  min-height: 40px;
}

.menu-item:hover {
  background: linear-gradient(135deg, #fff0f6, #eef3ff);
}

.menu-item:active {
  background: #ffe1ec;
}

.mi-icon {
  font-size: 1rem;
  width: 20px;
  text-align: center;
  flex-shrink: 0;
}

.mi-text {
  flex: 1;
}

.menu-danger {
  color: #c45d7a;
}

.menu-danger:hover {
  background: #fff0f6;
}

.divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, #f0dbe8, transparent);
  margin: 4px 8px;
}

/* 下拉菜单淡入淡出 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.15s, transform 0.15s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}

.chip-sky { background: linear-gradient(135deg, #eaf3ff, #ffffff); }
.chip-pink { background: linear-gradient(135deg, #fff0f6, #ffffff); }

@media (max-width: 560px) {
  .logo-text { display: none; }
  .app-header { padding: 12px 14px; }
  .dropdown { right: 4px; min-width: 220px; }
}
</style>
