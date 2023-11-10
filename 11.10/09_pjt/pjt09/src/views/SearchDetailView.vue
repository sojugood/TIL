<template>
  <div class="bg-white shadow overflow-hidden sm:rounded-lg">
    <div class="px-4 py-5 sm:px-6 flex justify-between items-center">
      <h3 class="text-lg leading-6 font-medium text-gray-900">
        동영상 상세 정보
      </h3>
      <div class="flex items-center">
        <button v-if="!isStored" @click="addLater(videoDetail)"
          class="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded mr-2">
          동영상 저장
        </button>
        <button v-else @click="removeLater(videoDetail)"
          class="bg-yellow-500 hover:bg-yellow-700 text-white py-2 px-4 rounded mr-2">
          저장 취소
        </button>
        <button @click="goBack" class="bg-red-500 hover:bg-red-700 text-white py-2 px-4 rounded">
          뒤로 가기
        </button>
      </div>
    </div>
    <div class="border-t border-gray-200">
      <dl>
        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">
            제목
          </dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ videoDetail.title }}
          </dd>
        </div>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">
            설명
          </dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ videoDetail.description }}
          </dd>
        </div>
        <div class="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">
            게시 날짜
          </dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            {{ formatDate(videoDetail.publishedAt) }}
          </dd>
        </div>
        <div class="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
          <dt class="text-sm font-medium text-gray-500">
            동영상
          </dt>
          <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
            <iframe width="700" height="400" :src="videoUrl" title="YouTube video player" frameborder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen></iframe>
          </dd>
        </div>
      </dl>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const videoDetail = ref({});
const route = useRoute();
const router = useRouter();


// 비디오 상세 정보를 가져오는 함수
const fetchVideoDetail = async () => {
  // 라우트 파라미터에서 비디오 ID를 가져옵니다.
  const videoId = route.params.id; // 'id' 파라미터가 있는지 확인하세요.

  try {
    // YouTube API로부터 비디오 상세 정보를 가져옵니다.
    const response = await axios.get(`https://www.googleapis.com/youtube/v3/videos`, {
      params: {
        part: 'snippet',
        id: videoId,
        key: import.meta.env.VITE_YOUTUBE_API_KEY
      }
    });

    // 응답으로부터 비디오 상세 정보를 videoDetail에 저장합니다.
    if (response.data.items && response.data.items.length > 0) {
      videoDetail.value = response.data.items[0].snippet;
    } else {
      console.error('Video not found');
      // 비디오를 찾을 수 없는 경우 사용자에게 알립니다.
    }
  } catch (error) {
    console.error('Error fetching video details:', error);
    // 오류 처리 로직을 추가합니다.
  }
};

// 컴포넌트가 마운트되면 비디오 상세 정보를 가져옵니다.
onMounted(fetchVideoDetail)

onMounted(() => {
  updateIsStored()
})

// 뒤로 가기 기능
const goBack = () => {
  router.back() // 이전 페이지로 돌아갑니다.
};

// 날짜 형식을 지정하는 함수
const formatDate = (value) => {
  if (value) {
    // ISO 8601 형식의 문자열을 Date 객체로 변환
    const date = new Date(value);
    // toLocaleDateString을 사용하여 지역에 맞는 날짜 형식으로 변환
    // 원하는 형식으로 지정할 수 있음 (예: 'ko-KR')
    return date.toLocaleDateString('ko-KR', { year: 'numeric', month: 'long', day: 'numeric' });
  }
  return ''; // 날짜 값이 없는 경우 빈 문자열 반환
};

// 비디오 URL
const videoUrl = `https://www.youtube.com/embed/${route.params.id}`

const isStored = ref(true)

const updateIsStored = () => {
  const existingLater = JSON.parse(localStorage.getItem('later')) || [];
  const videoId = route.params.id;
  isStored.value = existingLater.some(item => item.id === videoId);
}

// 비디오 저장
const addLater = (videoDetail) => {
  // 로컬 스토리지에서 기존에 저장된 데이터를 불러옵니다.
  const existingLater = JSON.parse(localStorage.getItem('later')) || [];

  // 비디오 ID를 가져옵니다. (라우트 파라미터에서 가져올 수도 있습니다.)
  const videoId = route.params.id; // 'id' 파라미터가 있는지 확인하세요.

  alert('동영상이 저장되었습니다!');
  // 새 비디오 객체에 ID를 추가하여 저장합니다.
  existingLater.push({ ...videoDetail, id: videoId });

  // 변경된 데이터를 로컬 스토리지에 저장합니다.
  localStorage.setItem('later', JSON.stringify(existingLater));

  updateIsStored()
}

// 저장된 비디오 삭제
const removeLater = (videoDetail) => {
  let existingLater = JSON.parse(localStorage.getItem('later')) || [];
  const videoId = route.params.id;

  // 선택한 동영상을 로컬 스토리지에서 제거합니다.
  existingLater = existingLater.filter(item => item.id !== videoId);

  localStorage.setItem('later', JSON.stringify(existingLater));

  alert('동영상이 삭제되었습니다.');

  updateIsStored()
}

</script>