<template>
  <header class="flex items-center justify-between px-6 md:px-24 py-6 shadow-md bg-slate-100">
    <router-link to="/" class="text-xl font-semibold text-slate-800">
      <Logo class="h-10 w-auto text-indigo-600" />
    </router-link>
    <nav class="flex gap-6 text-sm font-medium text-slate-700">
      <RouterLink to="/top-operadoras" class="hover:text-slate-600">Top Operadoras</RouterLink>
      <RouterLink to="/buscar-operadoras" class="hover:text-text-slate-600">Buscar Operadoras</RouterLink>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import Logo from '@/assets/logo.svg'
</script>
