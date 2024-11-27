<template>
  <v-app-bar app>
    <v-toolbar-title>Employment Management</v-toolbar-title>
    <v-spacer></v-spacer>
    <v-btn text :to="{ name: ROUTES.EMPLOYERS }" router>
      Employers
    </v-btn>
    <v-btn text :to="{ name: ROUTES.EMPLOYER_ADD }" router>
      Add new employer
    </v-btn>
  </v-app-bar>
</template>

<script setup>
import { ROUTES } from "../constants/routes";
</script>
