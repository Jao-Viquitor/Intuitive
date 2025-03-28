<template>
  <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="w-32 h-10 px-4 py-2 border border-gray-300 rounded-xl shadow-sm text-sm focus:ring-slate-500 focus:outline-none"
  >
    <option v-if="placeholder" disabled value="">{{ placeholder }}</option>
    <option v-for="opt in options" :key="opt" :value="opt">
      {{ opt }}
    </option>
  </select>
</template>

<script setup>

const props = defineProps({
  modelValue: [String, Number],
  options: {
    type: Array,
    required: true
  },
  placeholder: {
    type: String,
    default: ''
  }
})
</script>