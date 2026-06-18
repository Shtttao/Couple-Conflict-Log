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
        <CoupleAvatar variant="together" size="medium" />
        <div class="hero-text">
          <h2>Hi, {{ state.user.displayName }} ♡</h2>
          <p>
            A soft little place to record disagreements together.
            You write only your own side, and your partner writes theirs.
            Hearts grow when we listen.
          </p>
          <div class="hero-stats">
            <div class="stat">
              <span class="stat-num">{{ stats.total }}</span>
              <span class="stat-label">Memories</span>
            </div>
            <div class="stat">
              <span class="stat-num stat-peach">{{ stats.open }}</span>
              <span class="stat-label">Still to hug</span>
            </div>
            <div class="stat">
              <span class="stat-num stat-mint">{{ stats.resolved }}</span>
              <span class="stat-label">Reconciled</span>
            </div>
          </div>
        </div>
      </section>

      <section class="toolbar">
        <button class="btn btn-primary" @click="showForm = !showForm">
          <template v-if="!showForm">＋ New Conflict Log</template>
          <template v-else>✕ Close Form</template>
        </button>
        <div class="filter-chip">
          <button
            :class="{ active: filter === 'all' }"
            @click="filter = 'all'"
          >All</button>
          <button
            :class="{ active: filter === 'open' }"
            @click="filter = 'open'"
          >Open</button>
          <button
            :class="{ active: filter === 'resolved' }"
            @click="filter = 'resolved'"
          >Resolved</button>
        </div>
      </section>

      <ConflictForm
        v-if="showForm"
        :user="state.user"
        @created="onCreated"
        @cancel="showForm = false"
      />

      <section class="list">
        <p v-if="loading" class="muted center">Loading soft memories…</p>
        <p v-else-if="!visible.length" class="empty-note">
          <span class="empty-emoji">🌸</span>
          <span>
            Nothing here yet. Tap the button above to start a new little reflection.
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
          {{ confirmWipe ? '⚠ Click again to erase everything' : 'Erase all local data' }}
        </button>
        <p class="privacy-footer">
          🔒 Stored only on this device · IndexedDB · no server, no tracking.
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
  display: flex;
  align-items: center;
  gap: 18px;
  padding: 22px;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 26px;
  box-shadow: 0 18px 40px rgba(255, 182, 193, 0.18);
  margin-bottom: 18px;
}

.hero-text h2 {
  margin: 0 0 6px;
  color: var(--cocoa);
}

.hero-text p {
  margin: 0 0 14px;
  color: #8a7b90;
  font-size: 0.95rem;
  line-height: 1.6;
}

.hero-stats {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.stat {
  flex: 1 1 110px;
  background: linear-gradient(135deg, #fff0f6, #eef3ff);
  border-radius: 16px;
  padding: 10px 12px;
  text-align: center;
}

.stat-num {
  display: block;
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--pink-strong);
}

.stat-peach { color: #ef8b6a; }
.stat-mint { color: #4fb19a; }

.stat-label {
  display: block;
  font-size: 0.78rem;
  color: #8a7b90;
  margin-top: 2px;
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
    padding: 18px 16px;
  }
  .hero-text p { font-size: 0.9rem; }
  .toolbar { justify-content: center; }
}

@media (max-width: 480px) {
  .home-main { padding: 12px 12px 24px; }
  .stat { flex: 1 1 30%; }
}
</style>
