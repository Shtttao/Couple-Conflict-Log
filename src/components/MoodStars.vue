<script setup>
const props = defineProps({
  modelValue: { type: Number, default: 0 },
  readOnly: { type: Boolean, default: false },
  accent: { type: String, default: 'pink' }, // pink | sky
  small: { type: Boolean, default: false }
})
const emit = defineEmits(['update:modelValue'])

function set (v) {
  if (props.readOnly) return
  emit('update:modelValue', v === props.modelValue ? 0 : v)
}
</script>

<template>
  <div class="mood-stars" :class="[accent, { small, readonly: readOnly }]">
    <button
      v-for="n in 5"
      :key="n"
      type="button"
      class="star"
      :class="{ filled: n <= modelValue }"
      :disabled="readOnly"
      :aria-label="'Rate ' + n"
      @click="set(n)"
    >
      {{ n <= modelValue ? '♥' : '♡' }}
    </button>
  </div>
</template>

<style scoped>
.mood-stars {
  display: inline-flex;
  gap: 4px;
}

.star {
  border: none;
  background: transparent;
  font-size: 1.45rem;
  cursor: pointer;
  color: #e6c9d7;
  transition: transform 0.15s ease, color 0.15s ease;
  padding: 2px 4px;
  line-height: 1;
}

.star.filled.pink { color: #ff7fa8; }
.star.filled.sky { color: #7aa6ff; }

.star:not([disabled]):hover {
  transform: scale(1.2) rotate(-8deg);
}

.small .star { font-size: 1.1rem; }

.readonly .star { cursor: default; }
.readonly .star:not([disabled]):hover { transform: none; }
</style>
