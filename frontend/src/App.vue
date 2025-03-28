<template>
  <div>
    <div class="relative m-6">
      <h2 class="relative text-2xl md:text-3xl font-semibold teal-700">
        INTUITIVE CARE
      </h2>
    </div>

    <BuscaOperadoras />
    <TopOperadoras />
  </div>
</template>

<script setup>
import BuscaOperadoras from './components/BuscaOperadoras.vue'
import TopOperadoras from './components/TopOperadoras.vue'
</script>
