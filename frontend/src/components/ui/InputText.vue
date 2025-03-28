<template>
  <input
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      @keydown.enter="$emit('enter')"
      :placeholder="placeholder"
      class="w-72 h-10 px-4 py-2 border border-gray-300 rounded-xl shadow-sm"
  />
</template>

<script setup>
defineProps({
  modelValue: String,
  placeholder: String
})
defineEmits(['update:modelValue', 'enter'])
</script>
