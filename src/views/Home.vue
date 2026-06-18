<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAuth } from '../utils/auth.js'
import {
  getAllConflicts,
  addConflict,
  updateConflict,
  deleteConflict,
  wipeAllData
} from '../utils/storage.js'
import ConflictForm from '../components/ConflictForm.vue'
import ConflictCard from '../components/ConflictCard.vue'
import Header from '../components/Header.vue'
import CoupleAvatar from '../components/CoupleAvatar.vue'

const { state, logout } = useAuth()
const conflicts = ref([])
const loading = ref(true)
const showForm = ref(false)
const confirmWipe = ref(false)

const filter = ref('all') // all / open / resolved

const visible = computed(() => {
  if (filter.value === 'open') return conflicts.value.filter((c) => !c.resolved)
  if (filter.value === 'resolved') return conflicts.value.filter((c) => c.resolved)
  return conflicts.value
})

const stats = computed(() => {
  const total = conflicts.value.length
  const resolved = conflicts.value.filter((c) => c.resolved).length
  return { total, resolved, open: total - resolved }
})

async function reload () {
  loading.value = true
  conflicts.value = await getAllConflicts()
  loading.value = false
}

async function onCreated (payload) {
  await addConflict(payload)
  showForm.value = false
  await reload()
}

async function onSaved (record) {
  await updateConflict(record)
  await reload()
}

async function onDeleted (id) {
  if (!window.confirm('Delete this memory? This cannot be undone ♡')) return
  await deleteConflict(id)
  await reload()
}

async function onWipe () {
  if (!confirmWipe.value) {
    confirmWipe.value = true
    return
  }
  await wipeAllData()
  confirmWipe.value = false
  await reload()
}

onMounted(reload)
</script>

<template>
  <div class="home-wrap">
    <Header :user="state.user" @logout="logout" />

    <main class="home-main">
      <section class="hero-panel">
        <span class="hero-doodle hero-doodle-1">♡</span>
        <span class="hero-doodle hero-doodle-2">✿</span>
        <span class="hero-doodle hero-doodle-3">☆</span>
        <span class="hero-doodle hero-doodle-4">~</span>
        <span class="hero-doodle hero-doodle-5">♡</span>

        <div class="hero-avatar-wrap">
          <CoupleAvatar variant="together" size="big" />
        </div>

        <div class="hero-text">
          <h2>你好，{{ state.user.displayName }} <span class="wave">♡</span></h2>
          <p>
            一个温柔的小角落，一起记录争执。
            你写你的想法，对方写对方的想法。
            倾听让爱成长。
          </p>
          <div class="hero-stats">
            <div class="stat stat-pink">
              <span class="stat-num">{{ stats.total }}</span>
              <span class="stat-label">回忆</span>
            </div>
            <div class="stat stat-peach">
              <span class="stat-num">{{ stats.open }}</span>
              <span class="stat-label">待拥抱</span>
            </div>
            <div class="stat stat-mint">
              <span class="stat-num">{{ stats.resolved }}</span>
              <span class="stat-label">已和解</span>
            </div>
          </div>
        </div>
      </section>

      <section class="toolbar">
        <button class="btn btn-primary" @click="showForm = !showForm">
          <template v-if="!showForm">＋ 新建吵架记录</template>
          <template v-else>✕ 关闭表单</template>
        </button>
        <div class="filter-chip">
          <button
            :class="{ active: filter === 'all' }"
            @click="filter = 'all'"
          >全部</button>
          <button
            :class="{ active: filter === 'open' }"
            @click="filter = 'open'"
          >未和解</button>
          <button
            :class="{ active: filter === 'resolved' }"
            @click="filter = 'resolved'"
          >已和解</button>
        </div>
      </section>

      <ConflictForm
        v-if="showForm"
        :user="state.user"
        @created="onCreated"
        @cancel="showForm = false"
      />

      <section class="list">
        <p v-if="loading" class="muted center">正在加载甜蜜的回忆…</p>
        <p v-else-if="!visible.length" class="empty-note">
          <span class="empty-emoji">🌸</span>
          <span>
            这里空空如也。点击上方按钮开始新的反思吧。
          </span>
        </p>

        <ConflictCard
          v-for="item in visible"
          :key="item.id"
          :conflict="item"
          :user="state.user"
          @saved="onSaved"
          @delete="onDeleted"
        />
      </section>

      <footer class="home-footer">
        <button
          class="btn btn-ghost btn-danger btn-small"
          @click="onWipe"
        >
          {{ confirmWipe ? '⚠ 再次点击确认删除' : '清除所有本地数据' }}
        </button>
        <p class="privacy-footer">
          🔒 数据仅存储在此设备 · IndexedDB · 无服务器，无追踪。
        </p>
      </footer>
    </main>
  </div>
</template>

<style scoped>
.home-wrap {
  min-height: 100vh;
  background:
    radial-gradient(circle at 15% 10%, rgba(255, 220, 235, 0.55), transparent 45%),
    radial-gradient(circle at 85% 90%, rgba(200, 225, 255, 0.55), transparent 50%),
    linear-gradient(180deg, #fff5f9 0%, #f7f2ff 60%, #eef5ff 100%);
}

.home-main {
  max-width: 1080px;
  margin: 0 auto;
  padding: 16px 16px 32px;
}

.hero-panel {
  position: relative;
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 28px 24px;
  background:
    radial-gradient(ellipse at 20% 30%, rgba(255, 200, 220, 0.4), transparent 60%),
    radial-gradient(ellipse at 80% 70%, rgba(170, 200, 255, 0.35), transparent 60%),
    linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 245, 250, 0.9));
  border-radius: 32px;
  box-shadow:
    0 20px 50px rgba(255, 150, 180, 0.22),
    0 4px 10px rgba(200, 200, 255, 0.15) inset;
  margin-bottom: 20px;
  overflow: hidden;
  border: 2px solid rgba(255, 255, 255, 0.8);
}

/* decorative doodles around the hero */
.hero-doodle {
  position: absolute;
  font-size: 1.8rem;
  opacity: 0.5;
  pointer-events: none;
  animation: hero-float 5s ease-in-out infinite;
  font-weight: 300;
}
.hero-doodle-1 { top: 10%; right: 8%; color: #ff9cb5; font-size: 1.6rem; animation-delay: 0s; }
.hero-doodle-2 { top: 18%; left: 6%; color: #b7a8ff; font-size: 1.4rem; animation-delay: 1s; }
.hero-doodle-3 { bottom: 18%; right: 12%; color: #ffc08a; font-size: 1.3rem; animation-delay: 2s; }
.hero-doodle-4 { bottom: 10%; left: 10%; color: #98bdff; font-size: 2rem; animation-delay: 0.5s; font-weight: 200; }
.hero-doodle-5 { top: 50%; right: 20%; color: #ffb8cb; font-size: 1rem; animation-delay: 3s; }

@keyframes hero-float {
  0%, 100% { transform: translateY(0) rotate(-8deg); opacity: 0.35; }
  50% { transform: translateY(-10px) rotate(10deg); opacity: 0.7; }
}

.hero-avatar-wrap {
  flex-shrink: 0;
  filter: drop-shadow(0 8px 20px rgba(255, 150, 180, 0.25));
}

.hero-text h2 {
  margin: 0 0 8px;
  color: var(--cocoa);
  font-size: 1.8rem;
  font-weight: 600;
}

.wave {
  display: inline-block;
  animation: wave 2s ease-in-out infinite;
  transform-origin: 70% 70%;
  color: var(--pink-strong);
}

@keyframes wave {
  0%, 100% { transform: rotate(0deg); }
  20% { transform: rotate(18deg); }
  40% { transform: rotate(-10deg); }
  60% { transform: rotate(18deg); }
  80% { transform: rotate(-5deg); }
}

.hero-text p {
  margin: 0 0 16px;
  color: #8a7b90;
  font-size: 0.95rem;
  line-height: 1.7;
}

.hero-stats {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.stat {
  flex: 1 1 100px;
  border-radius: 18px;
  padding: 14px 10px 12px;
  text-align: center;
  position: relative;
  box-shadow: 0 6px 16px rgba(180, 150, 200, 0.15);
  border: 2px solid rgba(255, 255, 255, 0.7);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.stat:hover { transform: translateY(-3px); box-shadow: 0 10px 22px rgba(180, 150, 200, 0.25); }

.stat-pink { background: linear-gradient(135deg, #fff0f6, #ffd8e4); }
.stat-peach { background: linear-gradient(135deg, #fff3e8, #ffe0c8); }
.stat-mint { background: linear-gradient(135deg, #e8fff5, #c8f5e5); }

.stat-num {
  display: block;
  font-size: 1.7rem;
  font-weight: 700;
  color: #6b4a6b;
  line-height: 1.1;
}
.stat-peach .stat-num { color: #a6553a; }
.stat-mint .stat-num { color: #2f8a70; }

.stat-label {
  display: block;
  font-size: 0.8rem;
  color: #7a6a82;
  margin-top: 4px;
  font-weight: 500;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.filter-chip {
  display: inline-flex;
  background: rgba(255, 255, 255, 0.8);
  padding: 4px;
  border-radius: 999px;
  box-shadow: 0 6px 16px rgba(180, 190, 255, 0.25);
}

.filter-chip button {
  padding: 7px 14px;
  border-radius: 999px;
  border: none;
  background: transparent;
  color: #8a7b90;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.filter-chip button.active {
  background: linear-gradient(135deg, var(--pink-strong), #b7a8ff);
  color: #fff;
  box-shadow: 0 6px 14px rgba(255, 150, 180, 0.4);
}

.list {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 8px;
}

.empty-note {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 26px;
  background: rgba(255, 255, 255, 0.75);
  border-radius: 22px;
  color: #8a7b90;
}

.empty-emoji {
  font-size: 2rem;
}

.center { text-align: center; }
.muted { color: #a494a8; padding: 20px; }

.home-footer {
  margin-top: 28px;
  text-align: center;
}

.privacy-footer {
  margin-top: 10px;
  font-size: 0.78rem;
  color: #a494a8;
}

@media (max-width: 720px) {
  .hero-panel {
    flex-direction: column;
    text-align: center;
    padding: 24px 18px 22px;
    gap: 14px;
  }
  .hero-avatar-wrap { transform: scale(0.85); margin: -8px 0; }
  .hero-text h2 { font-size: 1.5rem; }
  .hero-text p { font-size: 0.9rem; }
  .toolbar { justify-content: center; }
  .hero-doodle-1 { right: 6%; top: 6%; font-size: 1.3rem; }
  .hero-doodle-2 { left: 4%; font-size: 1.1rem; }
  .hero-doodle-5 { display: none; }
}

@media (max-width: 480px) {
  .home-main { padding: 12px 12px 24px; }
  .stat { flex: 1 1 30%; padding: 12px 6px 10px; }
  .stat-num { font-size: 1.4rem; }
  .stat-label { font-size: 0.72rem; }
  .hero-avatar-wrap { transform: scale(0.75); margin: -12px 0; }
}
</style>
