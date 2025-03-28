<template>
  <button
      @click="$emit('click')"
      class="px-4 py-2 text-sm font-medium text-white bg-slate-800 rounded-xl hover:bg-slate-700 transition"
  >
    <slot>Botão</slot>
  </button>
</template>

<script setup>
defineEmits(['click'])
</script>
