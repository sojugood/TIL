<template>
  <div class="w-[75%] mx-auto my-8">
    <div class="flex justify-start space-x-4 mt-4">
      <div class="text-2xl">KOSDAQ 지수</div>
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
    <canvas id="kosdaqChart"></canvas>
  </div>
</template>
  
<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue';
import { getKosdaqData } from '../api/kosdaq';
import { Chart, registerables } from 'chart.js';
import zoomPlugin from "chartjs-plugin-zoom";
import 'chartjs-adapter-date-fns';
import { subDays, subMonths, subYears, format } from 'date-fns';
import { KosdaqData } from '../api/kosdaq';

Chart.register(...registerables);
Chart.register(zoomPlugin);

const chartRef = ref<Chart>;
const KosdaqData = ref<KosdaqData[]>([]);

const selectedCategory = ref('코스닥')
const selectedPeriod = ref('1M');

const categories = ['코스닥', '코스닥 150', '코스닥 150 산업재', '코스닥 150 소재', '코스닥 150 자유소비재', '코스닥 150 정보기술', '코스닥 150 커뮤니케이션서비스', '코스닥 150 필수소비재', '코스닥 150 헬스케어', '코스닥 IT', '코스닥 글로벌', '코스닥 기술성장기업부', '코스닥 대형주', '코스닥 벤처기업부', '코스닥 소형주', '코스닥 우량기업부', '코스닥 중견기업부', '코스닥 중형주', 'IT H/W', 'IT S/W & SVC', 'IT부품', '건설', '금속', '금융', '기계·장비', '기타서비스', '기타제조', '디지털컨텐츠', '반도체', '방송서비스', '비금속', '섬유·의류', '소프트웨어', '오락·문화', '운송', '운송장비·부품', '유통', '음식료·담배', '의료·정밀기기', '인터넷', '일반전기전자', '정보기기', '제약', '제조업', '종이·목재', '출판·매체복제', '컴퓨터서비스', '통신방송서비스', '통신서비스', '통신장비'];

const periods = reactive([
  { label: '1주일', value: '1W' },
  { label: '1개월', value: '1M' },
  { label: '3개월', value: '3M' },
  { label: '1년', value: '1Y' },
  { label: '전체', value: 'ALL' }
]);

const applyCategory = (Category) => {
  selectedCategory.value = Category
  const filteredData = KosdaqData.value.filter(data => data.idxNm === Category);
  updateChart(filteredData);
};

const applyZoom = (periodValue) => {
  selectedPeriod.value = periodValue;
  const filteredData = KosdaqData.value.filter(data => data.idxNm === selectedCategory.value);
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
      startDate = new Date(KosdaqData.value[KosdaqData.value.length - 1].basDt); // 가장 오래된 데이터 날짜
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
  const ctx = document.getElementById('kosdaqChart') as HTMLCanvasElement;

  if (ctx) {
    try {
      KosdaqData.value = await getKosdaqData();

      const chartData = {
        labels: KosdaqData.value.map(data => data.basDt),
        datasets: [{
          label: selectedCategory.value,
          data: KosdaqData.value.map(data => data.clpr),
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

      // 기본적으로 코스닥 표시
      applyCategory(selectedCategory.value);
    } catch (error) {
      console.error('There was an error fetching the kosdaq data: ', error);
    }
  }
});
</script>
