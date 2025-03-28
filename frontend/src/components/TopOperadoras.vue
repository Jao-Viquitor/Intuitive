<template>
  <div class="space-y-6 m-6">
    <div class="flex flex-wrap gap-4 items-center">
      <select
          v-model="periodo"
          class="px-4 py-2 border border-gray-300 rounded-xl text-sm shadow-sm focus:ring-indigo-500 focus:outline-none"
      >
        <option value="ano">Ano</option>
        <option value="trimestre">Trimestre</option>
      </select>

      <select
          v-model="ano"
          class="px-4 py-2 border border-gray-300 rounded-xl text-sm shadow-sm focus:ring-indigo-500 focus:outline-none"
      >
        <option v-for="anoItem in anosDisponiveis" :key="anoItem" :value="anoItem">
          {{ anoItem }}
        </option>
      </select>

      <select
          v-if="periodo === 'trimestre'"
          v-model="trimestre"
          class="px-4 py-2 border border-gray-300 rounded-xl text-sm shadow-sm focus:ring-indigo-500 focus:outline-none"
      >
        <option v-for="tri in trimestres" :key="tri" :value="tri">
          {{ tri }}
        </option>
      </select>

      <button
          @click="buscar"
          class="px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-xl hover:bg-indigo-700 transition"
      >
        Consultar
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div
          v-for="operadora in operadoras"
          :key="operadora.registro_ans"
          class="rounded-2xl border border-gray-200 p-4 shadow-sm bg-white transition hover:shadow-md"
      >
        <div class="flex justify-between items-start">
          <h2 class="text-lg font-semibold text-gray-900">
            {{ operadora.razao_social }}
          </h2>
          <span class="text-xs text-gray-500">#{{ operadora.registro_ans }}</span>
        </div>

        <div class="mt-2 space-y-1 text-sm text-gray-700">
          <p><strong>Nome Fantasia:</strong> {{ operadora.nome_fantasia }}</p>
          <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
          <p><strong>Total de Despesas: </strong>
            <span class="text-green-700 font-semibold">
              {{ formatarValor(operadora.total_despesa) }}
            </span>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const anosDisponiveis = [2023, 2024]
const trimestres = ['1T', '2T', '3T', '4T']

const periodo = ref('ano')
const ano = ref(2024)
const trimestre = ref('4T')
const operadoras = ref([])

const buscar = async () => {
  try {
    const params =
        periodo.value === 'ano'
            ? `periodo=ano&ano=${ano.value}`
            : `periodo=trimestre&trimestre=${trimestre.value}&ano=${ano.value}`

    const { data } = await axios.get(`http://localhost:5000/api/top_operadoras?${params}`)
    operadoras.value = data
  } catch (e) {
    console.error('Erro ao buscar top operadoras:', e)
  }
}

const formatarValor = (valor) => {
  return Number(valor).toLocaleString('pt-BR', {
    style: 'currency',
    currency: 'BRL',
  })
}
</script>
