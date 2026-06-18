<script setup>
import { ref, computed } from 'vue'
import MoodStars from './MoodStars.vue'

const props = defineProps({
  conflict: { type: Object, required: true },
  user: { type: Object, required: true }
})
const emit = defineEmits(['saved', 'delete'])

const editing = ref(false)
const myText = ref(props.conflict.myReflection || '')
const partnerText = ref(props.conflict.partnerReflection || '')
const myMood = ref(props.conflict.myMood || 0)
const partnerMood = ref(props.conflict.partnerMood || 0)

const isMe = computed(() => props.user.role === 'me')

function toggleEdit () {
  editing.value = !editing.value
  if (editing.value) {
    myText.value = props.conflict.myReflection || ''
    partnerText.value = props.conflict.partnerReflection || ''
    myMood.value = props.conflict.myMood || 0
    partnerMood.value = props.conflict.partnerMood || 0
  }
}

function save () {
  const next = {
    ...props.conflict,
    myReflection: isMe.value ? myText.value : props.conflict.myReflection,
    partnerReflection: !isMe.value ? partnerText.value : props.conflict.partnerReflection,
    myMood: isMe.value ? myMood.value : props.conflict.myMood,
    partnerMood: !isMe.value ? partnerMood.value : props.conflict.partnerMood
  }
  emit('saved', next)
  editing.value = false
}

function toggleResolved () {
  emit('saved', { ...props.conflict, resolved: !props.conflict.resolved })
}

function formattedDate (iso) {
  if (!iso) return ''
  const d = new Date(iso)
  return d.toLocaleDateString(undefined, {
    month: 'short',
    day: 'numeric',
    year: 'numeric'
  })
}
</script>

<template>
  <article class="card" :class="{ resolved: conflict.resolved }">
    <div class="card-head">
      <div class="card-head-left">
        <h4 class="card-date">{{ formattedDate(conflict.date) }}</h4>
        <div v-if="conflict.tags && conflict.tags.length" class="tag-row">
          <span
            v-for="tag in conflict.tags"
            :key="tag"
            class="tag"
          >#{{ tag }}</span>
        </div>
      </div>
      <div class="card-head-right">
        <button
          :class="['resolve-btn', conflict.resolved ? 'resolved' : '']"
          @click="toggleResolved"
        >
          {{ conflict.resolved ? '💗 Reconciled' : '✓ Mark as Reconciled' }}
        </button>
      </div>
    </div>

    <div class="dual-col">
      <section class="panel panel-sky">
        <header class="panel-head">
          <span class="avatar">🐻</span>
          <h4>Little Bear</h4>
          <span v-if="!isMe && !editing" class="lock-tag small">Partner only</span>
        </header>
        <textarea
          v-if="editing && isMe"
          v-model="myText"
          rows="6"
          placeholder="Your reflection…"
        ></textarea>
        <p v-else class="panel-text">
          {{ conflict.myReflection || 'Not yet written.' }}
        </p>
        <div class="mood-row">
          <span class="mood-label">Mood:</span>
          <MoodStars
            v-if="editing && isMe"
            v-model="myMood"
            accent="sky"
          />
          <MoodStars
            v-else
            :model-value="conflict.myMood || 0"
            accent="sky"
            read-only
            small
          />
        </div>
      </section>

      <section class="panel panel-pink">
        <header class="panel-head">
          <span class="avatar">🐰</span>
          <h4>Sweet Bunny</h4>
          <span v-if="isMe && !editing" class="lock-tag small">Partner only</span>
        </header>
        <textarea
          v-if="editing && !isMe"
          v-model="partnerText"
          rows="6"
          placeholder="Your reflection…"
        ></textarea>
        <p v-else class="panel-text">
          {{ conflict.partnerReflection || 'Not yet written.' }}
        </p>
        <div class="mood-row">
          <span class="mood-label">Mood:</span>
          <MoodStars
            v-if="editing && !isMe"
            v-model="partnerMood"
            accent="pink"
          />
          <MoodStars
            v-else
            :model-value="conflict.partnerMood || 0"
            accent="pink"
            read-only
            small
          />
        </div>
      </section>
    </div>

    <div class="card-actions">
      <button class="btn btn-ghost btn-danger btn-small" @click="emit('delete', conflict.id)">
        🗑 Delete
      </button>
      <button v-if="!editing" class="btn btn-secondary btn-small" @click="toggleEdit">
        ✎ Edit my side
      </button>
      <template v-else>
        <button class="btn btn-ghost btn-small" @click="toggleEdit">Cancel</button>
        <button class="btn btn-primary btn-small" @click="save">Save my changes ♡</button>
      </template>
    </div>
  </article>
</template>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 24px;
  padding: 18px 18px 16px;
  box-shadow: 0 18px 36px rgba(180, 190, 255, 0.18);
  transition: transform 0.2s, box-shadow 0.2s;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 22px 46px rgba(255, 182, 193, 0.22);
}

.card.resolved {
  background: linear-gradient(135deg, #f0fff7, #fff7f1);
}

.card-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 12px;
  margin-bottom: 14px;
  flex-wrap: wrap;
}

.card-date {
  margin: 0 0 6px;
  color: var(--cocoa);
  font-size: 1.05rem;
}

.tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.tag {
  padding: 3px 10px;
  border-radius: 999px;
  background: linear-gradient(135deg, #fff0f6, #eef3ff);
  color: #8a7b90;
  font-size: 0.78rem;
}

.resolve-btn {
  padding: 8px 14px;
  border-radius: 999px;
  border: 1.5px solid #e9c7d7;
  background: #fffafc;
  color: #8a6a84;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}

.resolve-btn:hover {
  background: #ffeaf3;
}

.resolve-btn.resolved {
  background: linear-gradient(135deg, #ffd9e6, #e6d4ff);
  border-color: #ffb6c1;
  color: #7a4a60;
}

.dual-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
}

.panel {
  padding: 14px;
  border-radius: 18px;
}

.panel-sky { background: linear-gradient(135deg, #eaf3ff, #fdf7ff); }
.panel-pink { background: linear-gradient(135deg, #ffeef5, #fff7f1); }

.panel-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.panel-head h4 {
  margin: 0;
  color: var(--cocoa);
  font-size: 0.95rem;
}

.panel-head .avatar {
  font-size: 1.1rem;
  width: 30px;
  height: 30px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(180, 190, 255, 0.25);
}

.lock-tag.small {
  margin-left: auto;
  padding: 3px 9px;
  border-radius: 999px;
  background: #fff3b8;
  color: #8a6a24;
  font-size: 0.7rem;
}

.panel textarea {
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  border-radius: 12px;
  border: 1.5px solid #fff;
  background: rgba(255, 255, 255, 0.9);
  font-size: 0.92rem;
  line-height: 1.6;
  resize: vertical;
  outline: none;
  color: var(--cocoa);
  font-family: inherit;
}

.panel textarea:focus {
  border-color: #c9b8ff;
}

.panel-text {
  margin: 0;
  padding: 10px;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 12px;
  font-size: 0.92rem;
  line-height: 1.7;
  color: #5a4e64;
  white-space: pre-wrap;
  min-height: 60px;
}

.mood-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
}

.mood-label {
  font-size: 0.8rem;
  color: #7c6d84;
}

.card-actions {
  margin-top: 14px;
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  flex-wrap: wrap;
}

@media (max-width: 720px) {
  .dual-col { grid-template-columns: 1fr; }
  .card-actions .btn { flex: 1; }
}
</style>
