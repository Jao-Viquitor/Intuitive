<template>
  <button
      @click="$emit('click')"
      class="w-32 h-10 px-4 py-2 text-sm font-medium text-white border border-slate-800 bg-slate-800 rounded-xl shadow-sm hover:bg-slate-700 transition"
  >
    <slot>Botão</slot>
  </button>
</template>

<script setup>
defineEmits(['click'])
</script>
