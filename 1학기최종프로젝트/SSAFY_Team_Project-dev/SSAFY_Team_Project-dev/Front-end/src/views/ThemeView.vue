<template>
  <div class="w-[75%] mx-auto my-8">
    <div class="flex justify-start space-x-4 mt-4">
      <div class="text-2xl">테마 지수</div>
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
    <canvas id="themeChart"></canvas>
  </div>
</template>
  
<script setup lang="ts">
import { onMounted, ref, reactive } from 'vue';
import { getThemeData } from '../api/theme';
import { Chart, registerables } from 'chart.js';
import zoomPlugin from "chartjs-plugin-zoom";
import 'chartjs-adapter-date-fns';
import { subDays, subMonths, subYears, format } from 'date-fns';
import { ThemeData } from '../api/theme';

Chart.register(...registerables);
Chart.register(zoomPlugin);

const chartRef = ref<Chart>;
const ThemeData = ref<ThemeData[]>([]);

const selectedCategory = ref('KRX 2차전지 K-뉴딜지수')
const selectedPeriod = ref('1M');

const categories = ['KRX 2차전지 K-뉴딜지수', 'KRX 300 기후변화지수', 'KRX BBIG K-뉴딜지수', 'KRX ESG Leaders 150', 'KRX ESG 사회책임경영지수(S)', 'KRX Eco Leaders 100', 'KRX FactSet 디지털 인프라 지수', 'KRX FactSet 디지털 헬스케어 지수', 'KRX FactSet 모빌리티 이노베이터 지수', 'KRX FactSet 차세대 에너지 지수', 'KRX Governance Leaders 100', 'KRX 게임 K-뉴딜지수', 'KRX 기후변화 솔루션지수', 'KRX 리츠 TOP 10 지수', 'KRX 리츠인프라 지수', 'KRX 바이오 K-뉴딜지수', 'KRX 반도체 Top 15', 'KRX 블루칩 25', 'KRX 인터넷 K-뉴딜지수', 'KRX 전기차 Top 15', 'KRX 포스트 IPO 지수', 'KRX-IHS Markit 코스피 200 예측 고배당 50', 'KRX-IHS Markit 코스피 200 예측 고배당 50 TR', 'KRX-IHS Markit 코스피 200 예측 배당성장 50', 'KRX-IHS Markit 코스피 200 예측 배당성장 50 TR', 'KRX/S&P ESG 고배당지수', 'KRX/S&P 탄소효율 그린뉴딜지수', '코스닥 150 거버넌스 지수', '코스피 200 ESG 지수', '코스피 200 기후변화지수', '코스피 고배당 50', '코스피 배당성장 50', '코스피 우선주 지수'];

const periods = reactive([
  { label: '1주일', value: '1W' },
  { label: '1개월', value: '1M' },
  { label: '3개월', value: '3M' },
  { label: '1년', value: '1Y' },
  { label: '전체', value: 'ALL' }
]);

const applyCategory = (Category) => {
  selectedCategory.value = Category
  const filteredData = ThemeData.value.filter(data => data.idxNm === Category);
  updateChart(filteredData);
};

const applyZoom = (periodValue) => {
  selectedPeriod.value = periodValue;
  const filteredData = ThemeData.value.filter(data => data.idxNm === selectedCategory.value);
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
      startDate = new Date(ThemeData.value[ThemeData.value.length - 1].basDt); // 가장 오래된 데이터 날짜
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
  const ctx = document.getElementById('themeChart') as HTMLCanvasElement;

  if (ctx) {
    try {
      ThemeData.value = await getThemeData();

      const chartData = {
        labels: ThemeData.value.map(data => data.basDt),
        datasets: [{
          label: selectedCategory.value,
          data: ThemeData.value.map(data => data.clpr),
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

      // 기본적으로 첫 번째 항목 표시
      applyCategory(selectedCategory.value);
    } catch (error) {
      console.error('There was an error fetching the theme data: ', error);
    }
  }
});
</script>
