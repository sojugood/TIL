<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild
      :my-msg="myMsg"
      @update-name="updateName"
    />
    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">클릭</button>
    <button @click="emitArgs">추가 인자 전달</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 1. 문자열 배열 선언 방식
// defineProps(['myMsg'])

// 2. 객체 선언 방식
// defineProps({
//   myMsg: String
// })

// props 데이터를 script에서 사용하려면
// const props = defineProps({
//                 myMsg: String,
//                 dynamicProps: String
//               })

// console.log(props)
// console.log(props.myMsg)

// 3. 다양한 객체 선언 방식
defineProps({
  myMsg: {
    type: String,
    required: true,
    // validator(value) {
    //   return ['success', 'warning', 'danger'].includes(value)
    // }
    // validator(value) {
    //   const validValues = ['success', 'warning', 'danger']
    //   if (!validValues.includes(value)) {
    //     console.error('에러입니다!')
    //     return false
    //   }
    //   return true
    // }
  },

  dynamicProps: {
    type: String,
    required: true
  }
})

// emit 선언 방식
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])
// emit 이벤트 변수 명 생략 가능(권장 X)
// const emit = defineEmits()

const buttonClick = function () {
  emit('someEvent')
}

const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>