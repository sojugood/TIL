<template>
  <div class="w-[75%] mx-auto my-8">
    <div class="flex justify-start space-x-4 mt-4">
      <div class="text-2xl">KOSPI 지수</div>
      <div class="relative">
        <button @click="showDropdown = !showDropdown" class="flex items-center bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          {{ selectedCategory }}
          <svg :class="{ 'rotate-180': showDropdown }" class="w-4 h-4 ml-2" xmlns="http://www.w3.org/2000/svg" fill="none"
            viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
          </svg>
        </button>
        <div v-if="showDropdown"
          class="absolute mt-2 py-1 w-48 bg-white border border-gray-200 rounded shadow-xl overflow-auto max-h-60">
          <a v-for="category in categories" :key="category" @click="selectCategory(category)"
            class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-500 hover:text-white">
            {{ category }}
          </a>
        </div>
      </div>
    </div>
    <div class="flex justify-start space-x-4 mt-4">
      <button v-for="period in periods" :key="period.value" @click="applyZoom(period.value)"
        :class="{ 'bg-green-500 font-extrabold': selectedPeriod === period.value, 'bg-blue-500': selectedPeriod !== period.value }"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        {{ period.label }}
      </button>
    </div>
    <canvas id="kospiChart"></canvas>
  </div>
</template>
  
<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue';
import { getKospiData } from '../api/kospi';
import { Chart, registerables } from 'chart.js';
import zoomPlugin from "chartjs-plugin-zoom";
import 'chartjs-adapter-date-fns';
import { subDays, subMonths, subYears, format } from 'date-fns';
import { KospiData } from '../api/kospi';

Chart.register(...registerables);
Chart.register(zoomPlugin);

const chartRef = ref<Chart>;
const KospiData = ref<KospiData[]>([]);

const selectedCategory = ref('코스피')
const selectedPeriod = ref('1M');
const showDropdown = ref(false);

const categories = ['코스피', '코스피 100', '코스피 200',
  '코스피 200 TOP 10', '코스피 200 건설', '코스피 200 경기소비재', '코스피 200 금융', '코스피 200 비중상한 20%', '코스피 200 비중상한 25%', '코스피 200 비중상한 30%', '코스피 200 산업재', '코스피 200 생활소비재', '코스피 200 에너지/화학', '코스피 200 정보기술', '코스피 200 중공업', '코스피 200 중소형주', '코스피 200 철강/소재', '코스피 200 초대형제외 지수', '코스피 200 커뮤니케이션서비스', '코스피 200 헬스케어', '코스피 50', '코스피 대형주', '코스피 소형주', '코스피 중형주', '코스피200제외 코스피지수', '건설업', '금융업', '기계', '보험', '비금속광물', '서비스업', '섬유의복', '운수장비', '운수창고업', '유통업', '음식료품', '의료정밀', '의약품', '전기가스업', '전기전자', '제조업', '종이목재', '증권', '철강금속', '통신업', '화학'];

const periods = reactive([
  { label: '1주일', value: '1W' },
  { label: '1개월', value: '1M' },
  { label: '3개월', value: '3M' },
  { label: '1년', value: '1Y' },
  { label: '전체', value: 'ALL' }
]);

function selectCategory(category) {
  selectedCategory.value = category;
  showDropdown.value = false;
  applyCategory(category); // 이 함수는 이미 정의되어 있을 것입니다.
};

const applyCategory = (Category) => {
  selectedCategory.value = Category
  const filteredData = KospiData.value.filter(data => data.idxNm === Category);
  updateChart(filteredData);
};

const applyZoom = (periodValue) => {
  selectedPeriod.value = periodValue;
  const filteredData = KospiData.value.filter(data => data.idxNm === selectedCategory.value);
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
      startDate = new Date(KospiData.value[KospiData.value.length - 1].basDt); // 가장 오래된 데이터 날짜
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
  const ctx = document.getElementById('kospiChart') as HTMLCanvasElement;

  if (ctx) {
    try {
      KospiData.value = await getKospiData();

      const chartData = {
        labels: KospiData.value.map(data => data.basDt),
        datasets: [{
          label: selectedCategory.value,
          data: KospiData.value.map(data => data.clpr),
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

      // 기본적으로 첫 번째 유종을 표시
      applyCategory(selectedCategory.value);
    } catch (error) {
      console.error('There was an error fetching the oil data: ', error);
    }
  }
});
</script>
