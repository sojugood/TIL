<template>
  <div class="w-[75%] mx-auto my-8">
    <div class="flex justify-start space-x-4 mt-4">
      <div class="text-2xl">KRX 지수</div>
      <button v-for="category in categories" :key="category"    @click="applyCategory(category)"
        :class="{'bg-green-500 font-extrabold': selectedCategory === category, 'bg-blue-500': selectedCategory !== category}"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        {{ category }}
      </button>
    </div>
    <div class="flex justify-start space-x-4 mt-4">
      <button v-for="period in periods" :key="period.value" @click="applyZoom(period.value)"
        :class="{'bg-green-500 font-extrabold': selectedPeriod === period.value, 'bg-blue-500': selectedPeriod !== period.value}"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        {{ period.label }}
      </button>
    </div>
    <canvas id="krxChart"></canvas>
  </div>
</template>
  
<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue';
import { getKrxData } from '../api/krx';
import { Chart, registerables } from 'chart.js';
import zoomPlugin from "chartjs-plugin-zoom";
import 'chartjs-adapter-date-fns';
import { subDays, subMonths, subYears, format } from 'date-fns';
import { KrxData } from '../api/krx';

Chart.register(...registerables);
Chart.register(zoomPlugin);

const chartRef = ref<Chart>;
const KrxData = ref<KrxData[]>([]);

const selectedCategory = ref('KRX 300')
const selectedPeriod = ref('1M');

const categories = ['KRX 100', 'KRX 300', 'KRX 300 금융', 'KRX 300 산업재', 'KRX 300 소재', 'KRX 300 자유소비재', 'KRX 300 정보기술', 'KRX 300 커뮤니케이션서비스', 'KRX 300 필수소비재', 'KRX 300 헬스케어', 'KRX 건설', 'KRX 경기소비재', 'KRX 기계장비', 'KRX 미디어&엔터테인먼트', 'KRX 반도체', 'KRX 방송통신', 'KRX 보험', 'KRX 에너지화학', 'KRX 운송', 'KRX 유틸리티', 'KRX 은행', 'KRX 자동차', 'KRX 정보기술', 'KRX 증권', 'KRX 철강', 'KRX 필수소비재', 'KRX 헬스케어', 'KTOP 30'];

const periods = reactive([
  { label: '1주일', value: '1W' },
  { label: '1개월', value: '1M' },
  { label: '3개월', value: '3M' },
  { label: '1년', value: '1Y' },
  { label: '전체', value: 'ALL' }
]);

const applyCategory = (Category) => {
  selectedCategory.value = Category
  const filteredData = KrxData.value.filter(data => data.idxNm === Category);
  updateChart(filteredData);
};

const applyZoom = (periodValue) => {
  selectedPeriod.value = periodValue;
  const filteredData = KrxData.value.filter(data => data.idxNm === selectedCategory.value);
  const endDate = new Date(filteredData[0].basDt);
  let startDate;

  switch (periodValue) {
    case '1W':
      startDate = subDays(endDate, 9);
      break;
    case '1M':
      startDate = subMonths(endDate, 1);
      break;
    case '3M':
      startDate = subMonths(endDate, 3);
      break;
    case '1Y':
      startDate = subYears(endDate, 1);
      break;
    case 'ALL':
      startDate = new Date(KrxData.value[KrxData.value.length - 1].basDt); // 가장 오래된 데이터 날짜
      break;
    default:
      startDate = subDays(endDate, 1);
      break;
  }

  if (chartRef.value) {
    chartRef.value.options.scales.x.min = format(startDate, 'yyyy-MM-dd');
    chartRef.value.options.scales.x.max = format(endDate, 'yyyy-MM-dd');
    chartRef.value.update();
  }
};

const updateChart = (filteredData) => {
  if (chartRef.value) {
    chartRef.value.data.labels = filteredData.map(data => data.basDt);
    chartRef.value.data.datasets[0].data = filteredData.map(data => data.clpr);
    chartRef.value.data.datasets[0].label = selectedCategory.value;
    applyZoom('1M'); // 변경할 때 기본적으로 1개월
    chartRef.value.update();
  }
};

onMounted(async () => {
  const ctx = document.getElementById('krxChart') as HTMLCanvasElement;

  if (ctx) {
    try {
      KrxData.value = await getKrxData();

      const chartData = {
        labels: KrxData.value.map(data => data.basDt),
        datasets: [{
          label: selectedCategory.value,
          data: KrxData.value.map(data => data.clpr),
          fill: false,
          borderColor: 'skyblue',
          tension: 0.1
        }]
      };

      chartRef.value = new Chart(ctx, {
        type: 'line',
        data: chartData,
        options: {
          scales: {
            y: {
              beginAtZero: false,
              grace: '5%'
            },
            x: {
              type: 'time',
              time: {
                unit: 'day'
              },
            }
          },
          plugins: {
            zoom: {
              zoom: {
                wheel: {
                  enabled: true,
                },
                pinch: {
                  enabled: true
                },
                mode: 'x',
              },
              pan: {
                enabled: true,
                mode: 'x',
              },
              limits: {
                x: { min: 'original', max: 'original', minRange: 1 },
              }
            }
          }
        }
      });

      // 기본적으로 KRX 300 표시
      applyCategory(selectedCategory.value);
    } catch (error) {
      console.error('There was an error fetching the krx data: ', error);
    }
  }
});
</script>
