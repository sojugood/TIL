<template>
  <div>
    <h1>장바구니</h1>
    <div v-if="cartItems">
      {{ cartItems }}
    </div>
    <div v-else>
      <strong>장바구니에 담긴 상품이 없습니다.</strong>
    </div>
    
  </div>
</template>

<script setup>
import { ref } from 'vue'

const cartItems = ref(null)

cartItems.value = JSON.parse(localStorage.getItem('cart'))

</script>

<style scoped>

</style>