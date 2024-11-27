<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="employees"
      item-value="name"
      class="elevation-1"
      hide-default-footer>
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>List of employers</v-toolbar-title>
        </v-toolbar>
      </template>

      <template v-slot:item.name="{ item }">
        <td :key="item.id">{{ item.name }}</td>
      </template>
      <template v-slot:item.age="{ item }">
        <td >{{ item.age }}</td>
      </template>
      <template v-slot:item.department="{ item }">
        <td>{{ item.department }}</td>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { EMPLOYERS_API } from "../constants/api";

import { ref, onMounted } from 'vue';
import axios from 'axios';


export default {
  setup() {
    const headers = [
      { text: 'Name', align: 'start', value: 'name' },
      { text: 'Department', value: 'department' },
      { text: 'Age', align: 'end', value: 'age' },
    ];

    const employers = ref(undefined);

    onMounted(async () => {
      try {
        const response = await axios.get(EMPLOYERS_API);
        employers.value = response.data;
      } catch (error) {
        console.error('Error fetching employee data:', error);
      }
    });

    return {
      headers,
      employees: employers
    };
  }
};
</script>

<style scoped lang="scss">
  .v-data-table {
    max-width: 100%;
  }
</style>
