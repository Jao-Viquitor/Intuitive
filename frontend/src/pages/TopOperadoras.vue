<template>
  <div class="space-y-6 min-h-screen flex flex-col">
    <Header/>

    <main class="flex-1 space-y-6 m-16">
      <div class="flex flex-wrap gap-4 items-center justify-center">
        <InputSelect v-model="periodo" :options="['Ano', 'Trimestre']"/>
        <InputSelect v-model="ano" :options="anosDisponiveis"/>
        <InputSelect v-if="periodo === 'Trimestre'" v-model="trimestre" :options="trimestres"/>
        <InputSelectUF v-model="uf"/>
        <ButtonPrimary @click="buscar">Consultar</ButtonPrimary>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <OperadoraCard
            v-for="operadora in operadoras"
            :key="operadora.registro_ans"
            :operadora="operadora"
            :mostrarDespesas="true"
        />
      </div>
    </main>

    <Footer/>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import api from '@/services/api.js'

import InputSelect from '@/components/ui/InputSelect.vue'
import InputSelectUF from '@/components/ui/InputSelectUF.vue'
import ButtonPrimary from '@/components/ui/ButtonPrimary.vue'
import OperadoraCard from '@/components/ui/OperadoraCards.vue'
import Header from '@/components/layout/Header.vue'
import Footer from '@/components/layout/Footer.vue'

const anosDisponiveis = [2023, 2024]
const trimestres = ['1T', '2T', '3T', '4T']

const periodo = ref('Ano')
const ano = ref(2024)
const trimestre = ref('4T')
const uf = ref('')
const operadoras = ref([])

const buscar = async () => {
  try {
    const params = new URLSearchParams()
    params.append('periodo', periodo.value)
    params.append('Ano', ano.value)
    if (periodo.value === 'Trimestre') {
      params.append('trimestre', trimestre.value)
    }
    if (uf.value) {
      params.append('uf', uf.value)
    }

    const {data} = await api.get(`/top_operadoras?${params.toString()}`)
    operadoras.value = data
  } catch (e) {
    console.error('Erro ao buscar top operadoras:', e)
  }
}
</script>
