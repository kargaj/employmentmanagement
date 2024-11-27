<template>
  <v-container>
    <v-form ref="form">
      <v-text-field
        v-model="newEmployee.name"
        label="Name"
        :error="!!errors.name"
        :error-messages="errors.name"
        required/>
      <v-select
        v-model="newEmployee.department"
        :items="EMPLOYERS_DEPARTMENTS"
        label="Department"
        :error="!!errors.department"
        :error-messages="errors.department"
        clearable/>
      <v-date-input
        v-model="newEmployee.birthDate"
        label="Birth date"
        prepend-icon
        :error="!!errors.birthDate"
        :error-messages="errors.birthDate"
        required/>
        <v-btn @click="submitForm" color="primary">Add Employer</v-btn>
    </v-form>
    <success-dialog 
      :visible.sync="dialogVisible"
      success-message="The employer was added successfully."/>
  </v-container>
</template>

<script>
import { EMPLOYERS_DEPARTMENTS, EMPLOYERS_API } from "../constants/api";

import { ref } from "vue";
import axios from 'axios';


export default {
  setup() {
    const newEmployee = ref({
      name: null,
      birthDate: null,
      department: null
    })

    const errors = ref({
      name: null,
      department: null,
      birthDate: null
    });

    const dialogVisible = ref(false);

    const submitForm = async () => {
      // Clear previous errors
      clearErrors();

      // Validate inputs manually before submission
      if (!newEmployee.value.name) {
        errors.value.name = 'Name is required.';
      }
      if (!newEmployee.value.birthDate) {
        errors.value.birthDate = 'Birth date is required.';
      }

      // If there are errors, abort submission
      if (Object.values(errors.value).some((error) => error)) {
        return;
      }

      // Make the API call
      try {
        const response = await axios.post(EMPLOYERS_API, {
          ...newEmployee.value,
          birth_date: new Date(newEmployee.value.birthDate).toISOString().split('T')[0] // Convert to ISO format
        });

        if (response.status === 201) {
          newEmployee.value = {
            name: '',
            department: null,
            birthDate: null
          };

          dialogVisible.value = true;
        }
      } catch (error) {
        if (error.response) {
          handleApiErrors(error.response.data);
        } else {
          console.error('Unexpected error:', error);
          alert('An unexpected error occurred. Please try again.');
        }
      }
    };

    const clearErrors = () => {
      errors.value = {
        name: null,
        department: null,
        birthDate: null
      };
    };

    const handleApiErrors = (errorData) => {
      for (const key in errorData) {
        if (errors.value[key] !== undefined) {
          errors.value[key] = errorData[key].join(', ');
        }
      }
    };

    return {
      EMPLOYERS_DEPARTMENTS,
      newEmployee,
      submitForm,
      dialogVisible,
      errors
    };
  },
};
</script>

<style scoped>
</style>
