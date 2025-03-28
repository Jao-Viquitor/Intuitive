<template>
  <div class="space-y-6 backdrop-grayscale-100 min-h-screen flex flex-col">
    <Header />

    <main class="flex-1 space-y-6 m-16">
      <div class="flex flex-wrap gap-4 items-center justify-center">
        <InputText
            v-model="termo"
            placeholder="Buscar operadora..."
            @enter="buscar"
        />
        <InputSelectUF v-model="uf" />
        <ButtonPrimary @click="buscar">Buscar</ButtonPrimary>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <OperadoraCard
            v-for="operadora in operadoras"
            :key="operadora.registro_ans"
            :operadora="operadora"
        />
      </div>
    </main>

    <Footer />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import api from '@/services/api.js'

import InputText from '@/components/ui/InputText.vue'
import InputSelectUF from '@/components/ui/InputSelectUF.vue'
import ButtonPrimary from '@/components/ui/ButtonPrimary.vue'
import OperadoraCard from '@/components/ui/OperadoraCards.vue'
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'

const termo = ref('')
const uf = ref('')
const operadoras = ref([])

const buscar = async () => {
  try {
    const params = new URLSearchParams()
    if (termo.value) params.append('q', termo.value)
    if (uf.value) params.append('uf', uf.value)

    const { data } = await api.get(`/busca_operadoras?${params.toString()}`)
    operadoras.value = data
  } catch (e) {
    console.error('Erro ao buscar:', e)
  }
}
</script>
